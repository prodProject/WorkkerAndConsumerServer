from CommonCode.queryExecutor import QueryExecuter
from CommonCode.strings import Strings
from Enums.databaseTables import Tables
from Searcher.searcherHelper import SearcherHelper
from Searcher.sercherConfig import SearcherConfig
from protobuff.entity_pb2 import StatusEnum


class ConsumerSearchConfig():
    LIFETIME = "raw_data -> 'dbInfo' ->> 'lifeTime'"
    EMAIL_LOCAL_PART = "raw_data -> 'contactDetails'->'email' ->> 'localPart'"
    EMAIL_DOMAIN_PART = "raw_data -> 'contactDetails'->'email' ->> 'domain'"
    PRIMARY_MOBILE_NO = "raw_data -> 'contactDetails'->'primaryMobile' ->> 'number'"


class ConsumerCounter:
    m_queryExecutor = QueryExecuter()
    m_helper = SearcherHelper()
    typeConfig = list()

    def handle(self, consumerpb):
        #assert workerpb is not None, "WorkerPb cannot be empty"

        if(consumerpb != None ):
            self.validate(consumerpb)
            self.typeConfig.clear();
            subquery = self.getConsumerConfig()
        else:
            subquery=""

        return self.m_queryExecutor.count(query=subquery, table=Tables.CONSUMER_DATA.name)

    def getConsumerConfig(self):
        subQuery = '';
        i = 0
        for data in self.typeConfig:
            subQuery = " " + subQuery + " " + data
            if len(self.typeConfig) - 1 == i:
                continue
            subQuery = " " + subQuery + " " + SearcherConfig.AND
            i = i + 1
        return subQuery

    def validate(self, consumerpb):
        if (consumerpb.lifeTime != StatusEnum.UNKNOWN_STATUS):
            self.typeConfig.append(
                self.m_helper.getCondition(cond=ConsumerSearchConfig.LIFETIME, value=StatusEnum.Name(consumerpb.lifeTime)))
        if (Strings.notEmpty(consumerpb.contactDetails.email.localPart) and Strings.notEmpty(
                consumerpb.contactDetails.email.domain)):
            self.typeConfig.append(self.m_helper.getCondition(cond=ConsumerSearchConfig.EMAIL_LOCAL_PART,
                                                              value=consumerpb.contactDetails.email.localPart))
            self.typeConfig.append(self.m_helper.getCondition(cond=ConsumerSearchConfig.EMAIL_DOMAIN_PART,
                                                              value=consumerpb.contactDetails.email.domain))
        if (Strings.notEmpty(consumerpb.contactDetails.primaryMobile.number)):
            self.typeConfig.append(self.m_helper.getCondition(cond=ConsumerSearchConfig.PRIMARY_MOBILE_NO,
                                                              value=consumerpb.contactDetails.primaryMobile.number))
        if (len(consumerpb.contactDetails.secondryMobile) > 0):
            self.typeConfig.append(
                self.m_helper.getConditionForCheckingInJsonArray(listKey='contactDetails', fieldKey='secondryMobile',
                                                                 key='number',
                                                                 value=consumerpb.contactDetais.primaryMobile.number))
        if (Strings.notEmpty(consumerpb.mobileNo.number)):
            self.typeConfig.append(
                self.m_helper.getOrCond(cond1=self.m_helper.getCondition(cond=ConsumerSearchConfig.PRIMARY_MOBILE_NO,
                                                                         value=consumerpb.mobileNo.number),
                                             cond2=self.m_helper.getConditionForCheckingInJsonArray(listKey='contactDetails',
                                                                                               fieldKey='secondryMobile',
                                                                                               key='number',
                                                                                               value=consumerpb.mobileNo.number)))
