from SendGridEmail.sendEmailFromSendgrid import SendMail
from protobuff.email_pb2 import EmailBuilderPb

email = EmailBuilderPb()
email.fromId.localpart="no-reply"
email.fromId.domain="prod.com"
tobu=email.toId.add()
tobu.localpart = "shubhamtiwaricr07"
tobu.domain = "gmail.com"
email.subject = "Hello"
email.content = "hi"
mail = SendMail()
mail.start(builder=email)
print(mail.done().headers)
