from pathlib import Path

from flask import Flask


app = Flask(__name__)


CURRENT_PATH = Path(__file__).parent.parent
DATA_PATH = Path.joinpath(CURRENT_PATH, 'data')


@app.route("/perform_query/", methods=['POST'])
def perform_query():
    user_request = []
    return app.response_class('\n'.join(user_request), content_type="text/plain")
