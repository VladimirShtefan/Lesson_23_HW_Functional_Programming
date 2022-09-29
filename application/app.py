from pathlib import Path

from flask import Flask, request

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
    user_request = []
    return app.response_class('\n'.join(user_request), content_type="text/plain")
