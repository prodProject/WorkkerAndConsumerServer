from enum import Enum

from CommonCode.convertJSONTOPb import ConvertJSONToPb
from CommonCode.queryExecutor import QueryExecuter
from Counter.consumerCounter import ConsumerCounter
from protobuff.consumer_pb2 import ConsumerSearchRequestPb, ConsumerSearchResponsePb


class States(Enum):
    START = 0,
    GET_COUNT = 1,
    DONE = 2,


class CountConsumerEntity:
    m_queryExecutor = QueryExecuter()
    m_consumerserchreqPb = ConsumerSearchRequestPb()
    m_converterJsonToPb = ConvertJSONToPb()
    m_consumerserchresPb = ConsumerSearchResponsePb()
    m_countHandler = ConsumerCounter()

    builder = None

    def start(self, consumerSearchPb):
        self.builder = consumerSearchPb
        self.controlFlow(currentState=States.GET_COUNT)

    def done(self):
        return self.m_consumerserchresPb

    def getCount(self):
        consumerPb = self.m_countHandler.handle(consumerpb=self.builder)
        if (consumerPb != None):
            self.m_consumerserchresPb.summary.totalHits=consumerPb
        # self.m_queryExecutor.count(table, subquery)
        self.controlFlow(currentState=States.DONE)

    def controlFlow(self, currentState):
        if (currentState == States.GET_COUNT):
            self.getCount()
        elif (currentState == States.DONE):
            self.done()
