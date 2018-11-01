from flask import Flask
from flask import request
from flask import render_template
from flask import json

from chatter.chatbot.chat import Chat

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/reply/<question>", methods=['GET'])
def reply(question):
    data = {'reply': Chat().reply(question)}
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response