import os

from flask import Flask, render_template, request, redirect, url_for, Response, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def getServerStatus():
    # database = "DATABASE_URL :"+os.environ.get('DATABASE_URL',0)
    environment = "ENVIRONMENT :" + os.environ.get('ENVIRONMENT', 1)
    url = "URL :" + os.environ.get('URL', 2)
    status = "STATUS :" + os.environ.get('STATUS', 3)
    response = environment + "<br>" + url + "<br>" + status
    return response


@app.route('/workerMain', methods=['GET'])
def getWorker():
    if (request.json == None):
        return str(request.url.rsplit('/workerMain', 1)[-2])
    else:
        return str(request.json)


@app.route('/user', methods=['POST'])
def user():
    return redirect(url_for('index'))
