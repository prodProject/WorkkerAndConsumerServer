from CommonCode.queryExecutor import QueryExecuter
from CommonCode.strings import Strings
from Enums.databaseTables import Tables
from Searcher.searcherHelper import SearcherHelper
from Searcher.sercherConfig import SearcherConfig
from protobuff.persontypeenum_pb2 import PersonTypeEnum


class PushNotificationSearchConfig():
    WORKER_REF = "raw_data -> 'workerRef' -> 'dbInfo' ->> 'id'"
    PERSON_TYPE = "raw_data -> 'type'->>'personType'"


class PushNotificationSearcher:
    m_queryExecutor = QueryExecuter()
    m_helper = SearcherHelper()
    typeConfig = list()

    def handle(self, pushNotificationSearchPb):
        assert pushNotificationSearchPb is not None, "PushNotificationSearchReq cannot be empty"
        self.typeConfig.clear();
        self.validate(pushNotificationSearchPb)
        subquery = self.getWokerConfig()
        return self.m_queryExecutor.search(query=subquery, table=Tables.PUSH_NOTIFICATON.name)

    def getWokerConfig(self):
        subQuery = '';
        i = 0
        for data in self.typeConfig:
            subQuery = " " + subQuery + " " + data
            if len(self.typeConfig) - 1 == i:
                continue
            subQuery = " " + subQuery + " " + SearcherConfig.AND
            i = i + 1
        return subQuery

    def validate(self, pushNotificationSearchPb):
        if (pushNotificationSearchPb.type.personType != PersonTypeEnum.UNKNOWN_PERSON_TYPE):
            self.typeConfig.append(
                self.m_helper.getEqualToCondition(cond=PushNotificationSearchConfig.PERSON_TYPE, value=PersonTypeEnum.Name(pushNotificationSearchPb.type.personType)))
        if(Strings.notEmpty(pushNotificationSearchPb.workerRef.dbInfo.id)):
            self.typeConfig.append(
                self.m_helper.getEqualToCondition(cond=PushNotificationSearchConfig.WORKER_REF, value=pushNotificationSearchPb.workerRef.dbInfo.id))
