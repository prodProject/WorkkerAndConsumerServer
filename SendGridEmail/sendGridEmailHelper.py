from sendgrid.helpers.mail import Mail

from CommonCode.strings import Strings


class SendGridEmailHelper:
    def builderToMail(self,emailBuilder):
        fromId = Strings.getFormattedEmail(builder=emailBuilder.fromId);
        toids = list()
        for ids in emailBuilder.toId:
            toids.append(Strings.getFormattedEmail(builder=ids))
        subject = emailBuilder.subject
        content = emailBuilder.content
        return Mail(from_email=fromId,
            to_emails=toids,
            subject=subject,
            html_content=content)
