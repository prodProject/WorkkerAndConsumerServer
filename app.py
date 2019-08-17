import os

from flask import Flask, render_template, request, redirect, url_for, Response, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def getServerStatus():
    database = os.environ.get('DATABASE_URL',0)
    environment = os.environ.get('ENVIRONMENT',1)
    url = os.environ.get('URL',2)
    status = os.environ.get('STATUS',3)
    response = database+"\n"+environment+"\n"+url+"\n"+status
    return response


@app.route('/workerMain', methods=['GET'])
def getWorker():
    data =request.get_json(silent=True)
    return str(request.json)


@app.route('/user', methods=['POST'])
def user():
    return redirect(url_for('index'))
