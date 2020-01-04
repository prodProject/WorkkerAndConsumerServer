from CommonCode.queryExecutor import QueryExecuter
from CommonCode.strings import Strings
from Enums.databaseTables import Tables
from Searcher.searcherHelper import SearcherHelper
from Searcher.sercherConfig import SearcherConfig
from protobuff.entity_pb2 import StatusEnum


class WorkerSearchConfig():
    LIFETIME = "raw_data -> 'dbInfo' ->> 'lifeTime'"
    EMAIL_LOCAL_PART = "raw_data -> 'contactDetails'->'email' ->> 'localPart'"
    EMAIL_DOMAIN_PART = "raw_data -> 'contactDetails'->'email' ->> 'domain'"
    PRIMARY_MOBILE_NO = "raw_data -> 'contactDetails'->'primaryMobile' ->> 'number'"


class WorkerSearcher:
    m_queryExecutor = QueryExecuter()
    m_helper = SearcherHelper()
    typeConfig = list()

    def handle(self, workerpb):
        assert workerpb is not None, "WorkerPb cannot be empty"
        self.validate(workerpb)
        self.typeConfig.clear();
        subquery = self.getWokerConfig()
        return self.m_queryExecutor.search(query=subquery, table=Tables.WORKER_DATA.name)

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

    def validate(self, workerpb):
        if (workerpb.lifeTime != StatusEnum.UNKNOWN_STATUS):
            self.typeConfig.append(
                self.m_helper.getCondition(cond=WorkerSearchConfig.LIFETIME, value=StatusEnum.Name(workerpb.lifeTime)))
        if (Strings.notEmpty(workerpb.contactDetails.email.localPart) and Strings.notEmpty(
                workerpb.contactDetails.email.domain)):
            self.typeConfig.append(self.m_helper.getCondition(cond=WorkerSearchConfig.EMAIL_LOCAL_PART,
                                                              value=workerpb.contactDetails.email.localPart))
            self.typeConfig.append(self.m_helper.getCondition(cond=WorkerSearchConfig.EMAIL_DOMAIN_PART,
                                                              value=workerpb.contactDetails.email.domain))
        if (Strings.notEmpty(workerpb.contactDetails.primaryMobile.number)):
            self.typeConfig.append(self.m_helper.getCondition(cond=WorkerSearchConfig.PRIMARY_MOBILE_NO,
                                                              value=workerpb.contactDetails.primaryMobile.number))
        if (len(workerpb.contactDetails.secondryMobile) > 0):
            self.typeConfig.append(
                self.m_helper.getConditionForCheckingInJsonArray(listKey='contactDetails', fieldKey='secondryMobile',
                                                                 key='number',
                                                                 value=workerpb.contactDetais.primaryMobile.number))
        if (Strings.notEmpty(workerpb.mobileNo.number)):
            self.typeConfig.append(
                self.m_helper.getOrCond(cond1=self.m_helper.getCondition(cond=WorkerSearchConfig.PRIMARY_MOBILE_NO,
                                                                         value=workerpb.mobileNo.number),
                                             cond2=self.m_helper.getConditionForCheckingInJsonArray(listKey='contactDetails',
                                                                                               fieldKey='secondryMobile',
                                                                                               key='number',
                                                                                               value=workerpb.mobileNo.number)))
