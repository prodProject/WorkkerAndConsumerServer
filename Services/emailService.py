from SendGridEmail.sendEmailFromSendgrid import SendMail


class EmailService:
    m_service = SendMail()

    def send(self,emailbuilder):
        assert emailbuilder is not None, "Email Cannot be empty"
        self.m_service.start(emailBuilder=emailbuilder)
        return self.m_service.done()
