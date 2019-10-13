from CommonCode.queryExecutor import QueryExecuter
from CommonCode.strings import Strings
from Enums.databaseTables import Tables
from Searcher.searcherHelper import SearcherHelper
from Searcher.sercherConfig import SearcherConfig
from protobuff.entity_pb2 import StatusEnum


class loginSearchConfig():
    LIFETIME = "raw_data -> 'dbInfo' ->> 'lifeTime'"
    EMAIL_LOCAL_PART = "'raw_data -> contactDetails'->'email' ->> 'localPart'"
    EMAIL_DOMAIN_PART = "'raw_data -> contactDetails'->'email' ->> 'domain'"
    PRIMARY_MOBILE_NO = "'raw_data -> contactDetails'->'primaryMobile' ->> 'number'"


class LoginSearcher:
    m_queryExecutor = QueryExecuter()
    m_helper = SearcherHelper()
    typeConfig = list()

    def handle(self, loginpb):
        assert loginpb is not None, "loginpb cannot be empty"
        self.validate(loginpb)
        subquery = self.getLoginConfig()
        return self.m_queryExecutor.search(query=subquery, table=Tables.WORKER_DATA.name)

    def getLoginConfig(self):
        subQuery = '';
        i = 0
        for data in self.typeConfig:
            subQuery = subQuery.join(str(data))
            if len(self.typeConfig) - 1 == i:
                continue
            subQuery = subQuery.join(str(SearcherConfig.AND))
            i = i + 1
        return subQuery

    def validate(self, loginpb):
        if (loginpb.lifeTime != StatusEnum.UNKNOWN_STATUS):
            self.typeConfig.append(
                self.m_helper.getCondition(cond=loginSearchConfig.LIFETIME, value=StatusEnum.Name(loginpb.lifeTime)))
        if (Strings.notEmpty(loginpb.contactDetais.email.localPart) and Strings.notEmpty(
                loginpb.contactDetais.email.domain)):
            self.typeConfig.append(self.m_helper.getCondition(cond=loginSearchConfig.EMAIL_LOCAL_PART,
                                                              value=loginpb.contactDetais.email.localPart))
            self.typeConfig.append(self.m_helper.getCondition(cond=loginSearchConfig.EMAIL_DOMAIN_PART,
                                                              value=loginpb.contactDetais.email.domain))
        if (Strings.notEmpty(loginpb.contactDetais.primaryMobile.number)):
            self.typeConfig.append(self.m_helper.getCondition(cond=loginSearchConfig.PRIMARY_MOBILE_NO,
                                                              value=loginpb.contactDetais.primaryMobile.number))

        
