from CommonCode.queryExecutor import QueryExecuter
from CommonCode.strings import Strings
from Enums.databaseTables import Tables
from Searcher.searcherHelper import SearcherHelper
from Searcher.sercherConfig import SearcherConfig
from protobuff.entity_pb2 import StatusEnum


class loginSearchConfig():
    LIFETIME = "raw_data -> 'dbInfo' ->> 'lifeTime'"
    EMAIL_LOCAL_PART = "raw_data -> 'contactDetails'->'email' ->> 'localPart'"
    EMAIL_DOMAIN_PART = "raw_data -> 'contactDetails'->'email' ->> 'domain'"
    PRIMARY_MOBILE_NO = "raw_data -> 'contactDetails'->'primaryMobile' ->> 'number'"


class LoginSearcher:
    m_queryExecutor = QueryExecuter()
    m_helper = SearcherHelper()
    typeConfig = list()

    def handle(self, loginpb):
        assert loginpb is not None, "loginpb cannot be empty"
        self.validate(loginpb)
        self.typeConfig.clear();
        subquery = self.getLoginConfig()
        return self.m_queryExecutor.search(query=subquery, table=Tables.LOGIN.name)

    def getLoginConfig(self):
        subQuery = '';
        i = 0
        for data in self.typeConfig:
            subQuery = " " + subQuery + " " + data
            if len(self.typeConfig) - 1 == i:
                continue
            subQuery = " " + subQuery + " " + SearcherConfig.AND
            i = i + 1
        return subQuery

    def validate(self, loginpb):
        if (loginpb.lifeTime != StatusEnum.UNKNOWN_STATUS):
            self.typeConfig.append(
                self.m_helper.getCondition(cond=loginSearchConfig.LIFETIME, value=StatusEnum.Name(loginpb.lifeTime)))
        if (Strings.notEmpty(loginpb.login.contactDetails.email.localPart) and Strings.notEmpty(
                loginpb.login.contactDetails.email.domain)):
            self.typeConfig.append(self.m_helper.getCondition(cond=loginSearchConfig.EMAIL_LOCAL_PART,
                                                              value=loginpb.login.contactDetails.email.localPart))
            self.typeConfig.append(self.m_helper.getCondition(cond=loginSearchConfig.EMAIL_DOMAIN_PART,
                                                              value=loginpb.login.contactDetails.email.domain))
        if (Strings.notEmpty(loginpb.login.contactDetails.primaryMobile.number)):
            self.typeConfig.append(self.m_helper.getCondition(cond=loginSearchConfig.PRIMARY_MOBILE_NO,
                                                              value=loginpb.login.contactDetails.primaryMobile.number))

        
