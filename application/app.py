from pathlib import Path
from typing import Generator

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
        parser: RequestParser = RequestParser(dict(request.values.items()))
        file_name: Path = Path.joinpath(DATA_PATH, parser.file_name)
        query: dict = parser.query
    except BaseAppException as e:
        abort(400, e.message)
    else:
        file: DataFile = DataFile(file_name)
        if not file.check_file():
            abort(400, 'Не верный путь к файлу')
        user_request: RunCommands = RunCommands(file.read())
        for command, data in query.items():
            try:
                user_request.run_mapping(command, data)
            except BaseAppException as e:
                abort(400, e.message)
        result: Generator | set | list = user_request.get_result()
        return app.response_class('\n'.join(result), content_type="text/plain")
