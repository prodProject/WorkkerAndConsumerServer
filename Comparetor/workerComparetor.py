from google.protobuf.json_format import MessageToJson

from Comparetor.addressComparetor import AddressComparetor
from Comparetor.contactDetailsComparetor import ContactDetailsComapretor
from Comparetor.deviceComparetor import DeviceInfoComaretor
from Comparetor.entityComparetor import EntityComparetor
from Comparetor.genderComparetor import GenderComparetor
from Comparetor.genericRefComparetor import GenericRefComparetor
from Comparetor.namesComparetor import NamesComparetor
from Comparetor.personTypeComparetor import PersonTypeComparetor
from Comparetor.timeComparetor import TimeComparetor
from protobuff.workertype_pb2 import UNKNOWN_WORKER_TYPE


class WorkerRefComparetor(EntityComparetor, NamesComparetor):

    def compareWorkerRef(self, oldPb, newPb):
        self.campareEntityPb(oldPb=oldPb.dbInfo, newPb=newPb.dbInfo)
        self.compareNamesPb(oldPb=oldPb.name, newPb=newPb.name)


class WorkerTypeConfigComapretor:

    def comapreWorkerTypeConfig(self, oldPb, newPb):
        if (oldPb.workerType != UNKNOWN_WORKER_TYPE):
            if (newPb.workerType != UNKNOWN_WORKER_TYPE):
                None  # nothing
            else:
                assert False, "Status Cannot be UNKNOWN type" + MessageToJson(newPb)

        if (len(oldPb.categories) <= len(newPb.categories)):
            None
        else:
            assert False, "New Pb has less number of secondry mobile " + MessageToJson(newPb)


class WorkerComparetor(EntityComparetor, NamesComparetor, ContactDetailsComapretor, TimeComparetor, GenderComparetor,
                       AddressComparetor, WorkerTypeConfigComapretor, PersonTypeComparetor, DeviceInfoComaretor):
    m_genericRef = GenericRefComparetor()

    def compareWorkerPb(self, oldPb, newPb):
        self.campareEntityPb(oldPb=oldPb.dbInfo, newPb=newPb.dbInfo)
        self.compareNamesPb(oldPb=oldPb.name, newPb=newPb.name)
        self.compareContactDetails(oldPb=oldPb.contactDetails, newPb=newPb.contactDetails)
        self.compareTimePb(oldPb=oldPb.dob, newPb=newPb.dob)
        self.comapreGenderPb(oldPb=oldPb.gender, newPb=newPb.gender)
        self.compareAddressPb(oldPb=oldPb.address, newPb=newPb.address)
        self.comapreWorkerTypeConfig(oldPb=oldPb.workerTypeConfig, newPb=newPb.workerTypeConfig)
        self.comaprePersonTypePb(oldPb=oldPb.type, newPb=newPb.type)
        self.compareDeviceInfoPb(oldPb=oldPb.device, newPb=newPb.device)
        self.m_genericRef.compareGenericRef(oldPb=oldPb.pushNotificationRef, newPb=newPb.pushNotificationRef)
