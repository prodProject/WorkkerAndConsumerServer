import os
import smtplib
from urllib import parse

from flask import Flask, request, redirect, url_for
from flask_mail import Mail
from google.protobuf.json_format import MessageToJson

from Handlers.loginHandler import LoginHandler
from Handlers.registrationHandler import RegistrionHandler
from Handlers.workerHandler import WorkerHandler
from Handlers.workerTypeHandler import WorkerTypeHandler

app = Flask(__name__)
mail = Mail(app)

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
    data = parse.parse_qs(parse.urlparse(request.url).query)['query'][0]
    print(data)
    assert data is not '',"Invalid id"
    return WorkerHandler.getWorker(data)

@app.route('/workerMain', methods=['POST'])
def createWorker():
    assert  request.json is not None,"WorkerPb is invalid"
    return  WorkerHandler.createWorker(builder=request.json)

@app.route('/workerMain', methods=['PUT'])
def updateWorker():
    assert  request.json is not None,"WorkerPb is invalid"
    return  WorkerHandler.updateWorker(builder=request.json)

@app.route('/registrationWorkerMain', methods=['POST'])
def registration():
    print(request.json)
    assert  request.json is not None,"RegistrationRequestPb is invalid"
    return  RegistrionHandler.createRegistrationworker(builder=request.json)

@app.route('/loginMain', methods=['POST'])
def login():
    print(request.json)
    assert  request.json is not None,"LoginRequestPb is invalid"
    return  LoginHandler.getLogin(builder=request.json)

@app.route('/workerTypeMain', methods=['GET'])
def getWorkerType():
    if(request.json is not None):
        return MessageToJson(WorkerTypeHandler.searchWorkerType(builder=request.json))
    else:
        data = parse.parse_qs(parse.urlparse(request.url).query)['query'][0]
        print(data)
        assert data is not '',"Invalid id"
        return WorkerTypeHandler.getWorkerType(id=data)


@app.route('/user', methods=['POST'])
def user():
    return redirect(url_for('index'))


@app.route('/mail', methods=['GET'])
def mailSend():
    sender = 'no_reply@mydomain.com'
    receivers = ['person@otherdomain.com']

    message = "hi"

    try:
        smtpObj = smtplib.SMTP('localhost')
        smtpObj.sendmail(sender, receivers, message)
        return "Successfully sent email"
    except smtplib.SMTPException:
        return "Error: unable to send email"
