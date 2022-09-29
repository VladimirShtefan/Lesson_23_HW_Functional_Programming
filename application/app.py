from pathlib import Path

from flask import Flask, request, abort

from application.exeptions import BaseAppException
from application.service.commands import RunCommands
from application.service.datafile import DataFile
from application.service.request import RequestParser

app = Flask(__name__)


CURRENT_PATH = Path(__file__).parent.parent
DATA_PATH = Path.joinpath(CURRENT_PATH, 'data')


@app.route("/perform_query/", methods=['POST'])
def perform_query():
    try:
        parser = RequestParser(dict(request.values.items()))
        file_name = Path.joinpath(DATA_PATH, parser.file_name)
        query = parser.query
    except BaseAppException as e:
        abort(400, e.message)
    else:
        file = DataFile(file_name)
        if not file.check_file():
            abort(400, 'Не верный путь к файлу')
        user_request = RunCommands(file.read())
        try:
            [getattr(user_request, command)(data) for command, data in query.items()]
        except BaseAppException as e:
            abort(400, e.message)
        result = user_request.run()
        return app.response_class('\n'.join(result), content_type="text/plain")
