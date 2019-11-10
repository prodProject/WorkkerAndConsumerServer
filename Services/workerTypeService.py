from WorkerTypeEntity.createWorkerTypeEntity import CreateWorkerTypeEntity
from WorkerTypeEntity.getWorkerTypeEntity import GetWorkerTypeEntity
from WorkerTypeEntity.searchWorkerTypeEntity import WorkerTypeSearchEntity


class WorkerTypeService:
    m_getWorkerTypeEntity = GetWorkerTypeEntity()
    m_createWorkerEntity = CreateWorkerTypeEntity()
    m_searchWorkerEntity = WorkerTypeSearchEntity()

    def create(self, builder):
        assert builder is not None, "WorkerTypePb Cannot be empty"
        assert builder.dbInfo.id is not '', "DbInfo id cannot be empty"
        self.m_createWorkerEntity.start(builder=builder)
        return self.m_createWorkerEntity.done()

    def get(self, id):
        assert id is not '', "id cannot be empty"
        self.m_getWorkerTypeEntity.start(id=id)
        return self.m_getWorkerTypeEntity.done()

    def update(self, id, builder):
        return

    def search(self, builder):
        assert builder is not None, "WorkerTypeRequestPb Cannot be empty"
        self.m_searchWorkerEntity.start(workerTypePb=builder)
        return self.m_searchWorkerEntity.done()

    def delete(builder):
        assert builder.dbInfo.id is not '', "DbInfo id cannot be empty"
        print(builder)
