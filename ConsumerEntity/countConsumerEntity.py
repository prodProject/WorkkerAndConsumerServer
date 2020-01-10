# start
# get count
# done
from enum import Enum

from CommonCode.queryExecutor import QueryExecuter


class States(Enum):
    Start = 0,
    GET_COUNT = 1,
    DONE = 2,


class CountConsumerEntity:
    m_queryExecutor = QueryExecuter()
    builder = None

    def start(self, consumerserchPb):
        self.builder = consumerserchPb
        self.controlFlow(currentState=States.GET_COUNT)

    def done(self):
        return self.consumerCountResponse

    def getCount(self):
        getCount = self.m_queryExecutor.count(table="CONSUMER_DATA", subquery="raw_data IS NOT NULL")
        print(getCount)

    def controlFlow(self, currentState):
        if (currentState == States.GET_COUNT):
            self.getCount()
        elif (currentState == States.DONE):
            self.done()
