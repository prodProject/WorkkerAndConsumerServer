import os
import smtplib
from urllib import parse

from flask import Flask, request, redirect, url_for, json
from flask_mail import Mail
from google.protobuf.json_format import MessageToJson

from Handlers.loginHandler import LoginHandler
from Handlers.pushNotificationServiceHandler import PushNotificationServiceHandler
from Handlers.registrationHandler import RegistrionHandler
from Handlers.sendPushNotificationHandler import SendPushNotificationHandler
from Handlers.workerHandler import WorkerHandler
from Handlers.workerTypeHandler import WorkerTypeHandler

app = Flask(__name__)
mail = Mail(app)


@app.route('/', methods=['GET', 'POST'])
def getServerStatus():
    environment = "ENVIRONMENT :" + os.environ.get('SERVER_ENVIRONMENT', 3)
    url = "URL :" + os.environ.get('URL', 2)
    status = "STATUS :" + os.environ.get('STATUS', 3)
    response = environment + "<br>" + url + "<br>" + status
    return response


@app.route('/workerMain', methods=['GET'])
def getWorker():
    data = parse.parse_qs(parse.urlparse(request.url).query)['query'][0]
    print(data)
    assert data is not '', "Invalid id"
    return WorkerHandler.getWorker(data)


@app.route('/workerMain', methods=['POST'])
def createWorker():
    assert request.json is not None, "WorkerPb is invalid"
    return WorkerHandler.createWorker(builder=request.json)


@app.route('/workerMain', methods=['PUT'])
def updateWorker():
    assert request.json is not None, "WorkerPb is invalid"
    return WorkerHandler.updateWorker(builder=request.json)


@app.route('/pushNotificationMain', methods=['GET'])
def getPushNotification():
    data = parse.parse_qs(parse.urlparse(request.url).query)['query'][0]
    print(data)
    assert data is not '', "Invalid id"
    return PushNotificationServiceHandler.getPushNotification(data)


@app.route('/pushNotificationMain', methods=['POST'])
def createPushNotification():
    assert request.json is not None, "pushNotificationPb is invalid"
    return MessageToJson(PushNotificationServiceHandler.createPushNotification(builder=request.json))


@app.route('/pushNotificationMain', methods=['PUT'])
def updatePushNotification():
    assert request.json is not None, "pushNotificationPb is invalid"
    return PushNotificationServiceHandler.updatePushNotification(builder=request.json)


@app.route('/sendNotificationMain', methods=['POST'])
def sendPushNotification():
    assert request.json is not None, "pushNotificationRequestPb is invalid"
    return SendPushNotificationHandler.snedNotification(builder=request.json)


@app.route('/registrationWorkerMain', methods=['POST'])
def registration():
    print(request.json)
    assert request.json is not None, "RegistrationRequestPb is invalid"
    return RegistrionHandler.createRegistrationworker(builder=request.json)


@app.route('/loginMain', methods=['POST'])
def login():
    print(request.json)
    assert request.json is not None, "LoginRequestPb is invalid"
    return LoginHandler.getLogin(builder=request.json)


@app.route('/workerTypeMain', methods=['GET'])
def getWorkerType():
    data = parse.parse_qs(parse.urlparse(request.url).query)['query'][0]
    if ("{" in str(data)):
        assert data is not '', "Invalid Query"
        return MessageToJson(WorkerTypeHandler.searchWorkerType(builder=json.loads(data)))
    else:
        print(data)
        assert data is not '', "Invalid Query"
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
