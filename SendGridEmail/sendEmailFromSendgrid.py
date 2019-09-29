from enum import Enum

from sendgrid import SendGridAPIClient

from ConstantsProperties import sendGridEmailProperties
from SendGridEmail.sendGridEmailHelper import SendGridEmailHelper


class States(Enum):
    START = 0,
    SEND_MAIL = 1,
    DONE = 2,


class SendMail:
    m_helper = SendGridEmailHelper()
    response = None
    builder = None

    def start(self, builder):
        self.builder = builder
        self.controlFlow(currentState=States.SEND_MAIL)

    def done(self):
        return self.response

    def sendMail(self):
       mailContent = self.m_helper.builderToMail(emailBuilder=self.builder)
       try:
           sg = SendGridAPIClient(sendGridEmailProperties.SENDGRID_API_KEY)
           self.response = sg.send(mailContent)
       except Exception as e:
           print(e.message)
       self.controlFlow(currentState=States.DONE)

    def controlFlow(self, currentState):
        if (currentState == States.SEND_MAIL):
            self.sendMail()
        elif (currentState == States.DONE):
            self.done()
