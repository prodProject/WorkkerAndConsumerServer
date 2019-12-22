from Comparetor.entityComparetor import EntityComparetor
from Comparetor.namesComparetor import NamesComparetor


class GenericRefComparetor(EntityComparetor, NamesComparetor):

    def compareGenericRef(self, oldPb, newPb):
        self.campareEntityPb(oldPb=oldPb.dbInfo, newPb=newPb.dbInfo)
        self.compareNamesPb(oldPb=oldPb.name, newPb=newPb.name)

