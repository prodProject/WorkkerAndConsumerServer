import os

from flask import Flask, render_template, request, redirect, url_for, Response, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


@app.route('/workerMain', methods=['GET'])
def getWorker():
    print(request.url.rsplit('/workerMain', 1)[-1])
    data =request.get_json(silent=True)
    return request.json


@app.route('/user', methods=['POST'])
def user():
    return redirect(url_for('index'))
