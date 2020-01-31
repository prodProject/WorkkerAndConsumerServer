from ConsumerEntity.countConsumerEntity import CountConsumerEntity
from ConsumerEntity.createConsumerEntity import CreateConsumerEntity
from ConsumerEntity.getConsumerEntity import GetConsumerEntity
from ConsumerEntity.searchConsumerEntity import ConsumerSearchEntity
from ConsumerEntity.updateConsumerEntity import UpdateConsumerEntity
from Helper.entityHelper import EntityHelper


class ConsumerService:
    m_createConsumer = CreateConsumerEntity()
    m_getConsumerEntity = GetConsumerEntity()
    m_updateConsumerEntity = UpdateConsumerEntity()
    m_consumerSearchEntity = ConsumerSearchEntity()
    m_consumerEntityHelper = EntityHelper()
    m_consumerCountEntity = CountConsumerEntity()

    def create(self, builder):
        assert builder is not None, "ConsumerPb Cannot be empty"
        self.m_createConsumer.start(builder=builder)
        return self.m_createConsumer.done()

    def get(self, id):
        assert id is not '', "id cannot be empty"
        self.m_getConsumerEntity.start(id=id)
        return self.m_getConsumerEntity.done()

    def update(self, id, builder):
        # assert builder.dbInfo.id is not '', "DbInfo id cannot be empty"
        assert id is not '', "id cannot be empty"
        assert builder is not None, "builder cannot be empty"
        if (self.m_consumerEntityHelper.comapreIds(id1=id, id2=builder.dbInfo.id)):
            assert True, "Upadting Wrong Entity"
        self.m_updateConsumerEntity.start(id=id, builder=builder)
        return self.m_updateConsumerEntity.done()

    def search(self, builder):
        assert builder is not None, "ConsumerSearchRequest Cannot be empty"
        self.m_consumerSearchEntity.start(consumersearchreqPb=builder)
        return self.m_consumerSearchEntity.done()

    def count(self, builder):
         #assert builder is not None, "WorkerSearchRequest Cannot be empty"
         self.m_consumerCountEntity.start(consumerSearchPb=builder)
         return self.m_consumerCountEntity.done()

    def delete(builder):
        assert builder.dbInfo.id is not '', "DbInfo id cannot be empty"
        print(builder)

