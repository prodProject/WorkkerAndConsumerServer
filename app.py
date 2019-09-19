import os
import smtplib

from flask import Flask,request, redirect, url_for
from flask_mail import Message
from flask_mail import Mail

from CommonCode.strings import Strings
from Handlers.workerHandler import WorkerHandler

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
    data = request.url.rsplit('/workerMain', 1)[-1]
    assert data is not '',"Invalid id"
    return WorkerHandler.getWorker(data[Strings.length(data)-1])

@app.route('/workerMain', methods=['POST'])
def createWorker():
    assert  request.json is not None,"WorkerPb is invalid"
    return  WorkerHandler.createWorker(builder=request.json)

@app.route('/workerMain', methods=['PUT'])
def updateWorker():
    assert  request.json is not None,"WorkerPb is invalid"
    return  WorkerHandler.updateWorker(builder=request.json)

@app.route('/user', methods=['POST'])
def user():
    return redirect(url_for('index'))


@app.route('/mail', methods=['GET'])
def mailSend():
    sender = 'no_reply@mydomain.com'
    receivers = ['person@otherdomain.com']

    message = """From: No Reply <no_reply@mydomain.com>
To: Person <person@otherdomain.com>
Subject: Test Email

This is a test e-mail message.
"""

    try:
        smtpObj = smtplib.SMTP('localhost')
        smtpObj.sendmail(sender, receivers, message)
        return "Successfully sent email"
    except smtplib.SMTPException:
        return "Error: unable to send email"
