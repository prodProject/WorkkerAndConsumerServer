from google.protobuf.json_format import MessageToJson

from Comparetor.emailComparetor import EmailComparetor
from Comparetor.mobileComparetor import MobileComparetor


class ContactDetailsComapretor(EmailComparetor, MobileComparetor):

    def compareContactDetails(self, oldPb, newPb):
        self.compareEmailPb(oldPb=oldPb.email, newPb=newPb.email)
        self.comapreMobilePb(oldPb=oldPb.primaryMobile, newPb=newPb.primaryMobile)
        if (len(oldPb.secondryMobile) <= len(newPb.secondryMobile)):
            None
        else:
            assert False, "New Pb has less number of secondry mobile " + MessageToJson(newPb)
