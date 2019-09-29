from SendGridEmail.sendEmailFromSendgrid import SendMail


class EmailService:
    m_service = SendMail()

    def send(self,builder):
        assert builder is not None, "Email Cannot be empty"
        self.m_service.start(builder=builder)
        return self.m_service.done()
