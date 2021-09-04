from flask import Flask
from flask_talisman import Talisman

from rq import Queue

from helpers import send_prediction_email
from redis_worker import conn


app = Flask(__name__)
Talisman(app)
q = Queue(connection=conn)


@app.route('/', methods=['GET', 'POST'])
def main():
    return 'app is running :-)'


@app.route('/run', methods=['GET', 'POST'])
def run():
    job = q.enqueue_call(
        func=send_prediction_email, result_ttl=5000
    )
    with open('file.txt', 'r') as file:
        return file.read()
