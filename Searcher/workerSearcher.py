from email._header_value_parser import get_quoted_string

from CommonCode.queryExecutor import QueryExecuter
from CommonCode.strings import Strings
from Enums.databaseTables import Tables
from Searcher.sercherConfig import SearcherConfig
from protobuff.entity_pb2 import StatusEnum


class WorkerSearchConfig():
     LIFETIME = "raw_data -> 'dbInfo' ->> 'lifeTime'"

class WorkerSearcher:

    m_queryExecutor = QueryExecuter()

    typeConfig = list()

    def handle(self,workerpb):
        assert workerpb is not None, "WorkerPb cannot be empty"
        self.validate(workerpb)
        subquery = self.getWokerConfig()
        return self.m_queryExecutor.search(query=subquery,table=Tables.WORKER_DATA.name)


    def getWokerConfig(self):
        subQuery = '';
        i=0
        for data in self.typeConfig:
            subQuery=subQuery.join(str(data))
            if len(self.typeConfig)-1 == i:
                continue
            subQuery=subQuery.join(str(SearcherConfig.AND))
            i=i+1
        return subQuery


    def validate(self,workerpb):
        if(workerpb.lifeTime != StatusEnum.UNKNOWN_STATUS):
            self.typeConfig.append(WorkerSearchConfig.LIFETIME+'='+Strings.qoutedString(StatusEnum.Name(workerpb.lifeTime)))
