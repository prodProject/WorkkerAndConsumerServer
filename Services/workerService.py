from Helper.workerEntityHelper import WorkerEntityHelper
from WorkerEntity.createWorkerEntity import CreateWorkerEntity
from WorkerEntity.getWorkerEntity import GetWorkerEntity
from WorkerEntity.updateWorkerEntity import UpdateWorkerEntity


class WorkerService:
    m_createWorker = CreateWorkerEntity()
    m_getWorkerEntity = GetWorkerEntity()
    m_updateWorkerEntity = UpdateWorkerEntity()
    m_workerEntityHelper = WorkerEntityHelper()

    def create(self, builder):
        assert builder is not None, "WorkerPb Cannot be empty"
        self.m_createWorker.start(builder=builder)
        return self.m_createWorker.done()

    def get(self, id):
        assert id is not '', "id cannot be empty"
        self.m_getWorkerEntity.start(id=id)
        return self.m_getWorkerEntity.done()

    def update(self, id, builder):
        assert builder.dbInfo.id is not '', "DbInfo id cannot be empty"
        assert id is not '', "id cannot be empty"
        assert builder is not None, "builder cannot be empty"
        if (self.m_workerEntityHelper.comapreIds(id1=id, id2=builder.dbInfo.id)):
            assert True ,"Upadting Wrong Entity"
        self.m_updateWorkerEntity.start(id=id, builder=builder)
        return self.m_updateWorkerEntity.done()

    def delete(builder):
        assert builder.dbInfo.id is not '', "DbInfo id cannot be empty"
        print(builder)
