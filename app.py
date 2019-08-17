import os

from flask import Flask, render_template, request, redirect, url_for, Response, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


@app.route('/workerMain', methods=['GET'])
def getWorker():
    data =request.get_json(silent=True)
    return str(request.json)


@app.route('/user', methods=['POST'])
def user():
    return redirect(url_for('index'))
