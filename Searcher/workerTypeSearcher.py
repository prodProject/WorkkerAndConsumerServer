from CommonCode.queryExecutor import QueryExecuter
from CommonCode.strings import Strings
from Enums.databaseTables import Tables
from Searcher.searcherHelper import SearcherHelper
from Searcher.sercherConfig import SearcherConfig
from protobuff.entity_pb2 import StatusEnum
from protobuff.workertype_pb2 import UNKNOWN_WORKER_TYPE, WorkerTypeEnum


class WorkerTypeSearchConfig():
    LIFETIME = "raw_data -> 'dbInfo' ->> 'lifeTime'"
    WORKER_TYPE = "raw_data ->> 'workerType'"


class WorkerTypeSearcher:
    m_queryExecutor = QueryExecuter()
    m_helper = SearcherHelper()
    typeConfig = list()

    def handle(self, workerTypepb):
        assert workerTypepb is not None, "WorkerPb cannot be empty"
        self.typeConfig.clear();
        self.validate(workerTypepb)
        subquery = self.getWokerTypeConfig()
        return self.m_queryExecutor.search(query=subquery, table=Tables.WORKER_TYPE.name)

    def getWokerTypeConfig(self):
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
        if (workerpb.dbInfo.lifeTime != StatusEnum.UNKNOWN_STATUS):
            self.typeConfig.append(
                self.m_helper.getEqualToCondition(cond=WorkerTypeSearchConfig.LIFETIME, value=StatusEnum.Name(workerpb.dbInfo.lifeTime)))

        if (workerpb.workerType != UNKNOWN_WORKER_TYPE):
            self.typeConfig.append(
                self.m_helper.getEqualToCondition(cond=WorkerTypeSearchConfig.WORKER_TYPE, value=WorkerTypeEnum.Name(workerpb.workerType)))
