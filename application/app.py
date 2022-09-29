from pathlib import Path

from flask import Flask, request, abort

from application.service.commands import RunCommands
from application.service.datafile import DataFile
from application.service.request import RequestParser

app = Flask(__name__)


CURRENT_PATH = Path(__file__).parent.parent
DATA_PATH = Path.joinpath(CURRENT_PATH, 'data')


@app.route("/perform_query/", methods=['POST'])
def perform_query():
    parser = RequestParser(dict(request.values.items()))
    file_name = Path.joinpath(DATA_PATH, parser.file_name)
    query = parser.query
    file = DataFile(file_name)
    if not file.check_file():
        abort(400, 'Не верный путь к файлу')
    user_request = []
    try:
        user_request = list(RunCommands(file.read(), **query).run())
    except IndexError:
        abort(400, f'При использовании команды map выбран не существующий столбец')
    return app.response_class('\n'.join(user_request), content_type="text/plain")
