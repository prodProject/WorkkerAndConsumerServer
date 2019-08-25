import os


from flask import Flask,request, redirect, url_for


from CommonCode.strings import Strings
from Handlers.workerHandler import WorkerHandler

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
    data = request.url.rsplit('/workerMain', 1)[-1]
    assert data is not '',"Invalid id"
    return WorkerHandler.getWorker(data[Strings.length(data)-1])

@app.route('/workerMain', methods=['POST'])
def createWorker():
    assert  request.json is not None,"WorkerPb is invalid"
    return  WorkerHandler.createWorker(builder=request.json)

@app.route('/workerMain', methods=['PUT'])
def createWorker():
    assert  request.json is not None,"WorkerPb is invalid"
    return  WorkerHandler.update(builder=request.json)

@app.route('/user', methods=['POST'])
def user():
    return redirect(url_for('index'))
