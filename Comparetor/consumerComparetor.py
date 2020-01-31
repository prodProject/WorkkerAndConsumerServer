from Comparetor.addressComparetor import AddressComparetor
from Comparetor.contactDetailsComparetor import ContactDetailsComapretor
from Comparetor.entityComparetor import EntityComparetor
from Comparetor.genderComparetor import GenderComparetor
from Comparetor.namesComparetor import NamesComparetor
from Comparetor.personTypeComparetor import PersonTypeComparetor
from Comparetor.timeComparetor import TimeComparetor


class ConsumerRefComparetor(EntityComparetor, NamesComparetor):

    def compareConsumerRef(self, oldPb, newPb):
        self.campareEntityPb(oldPb=oldPb.dbInfo, newPb=newPb.dbInfo)
        self.compareNamesPb(oldPb=oldPb.name, newPb=newPb.name)


class ConsumerComparetor(EntityComparetor, NamesComparetor, ContactDetailsComapretor, TimeComparetor, GenderComparetor,
                        AddressComparetor, PersonTypeComparetor):
    def compareConsumerPb(self, oldPb, newPb):
        self.campareEntityPb(oldPb=oldPb.dbInfo, newPb=newPb.dbInfo)
        self.compareNamesPb(oldPb=oldPb.name, newPb=newPb.name)
        self.compareContactDetails(oldPb=oldPb.contactDetails, newPb=newPb.contactDetails)
        self.compareTimePb(oldPb=oldPb.dob, newPb=newPb.dob)
        self.comapreGenderPb(oldPb=oldPb.gender, newPb=newPb.gender)
        self.compareAddressPb(oldPb=oldPb.address, newPb=newPb.address)
        self.comaprePersonTypePb(oldPb=oldPb.type, newPb=newPb.type)
