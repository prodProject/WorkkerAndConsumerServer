import os

from flask import Flask, render_template, request, redirect, url_for, Response
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


@app.route('/workerMain', methods=['GET'])
def index():
    print(request.url.rsplit('/workerMain', 1)[-1])
    return Response("Hello")


@app.route('/user', methods=['POST'])
def user():
    return redirect(url_for('index'))
