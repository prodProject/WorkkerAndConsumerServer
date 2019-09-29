from Helper.entityHelper import EntityHelper
from LoginEntity.createLoginEntity import CreateLoginEntity
from LoginEntity.getLoginEntity import GetLoginEntity
from LoginEntity.searchLoginEntity import LoginSearchEntity
from LoginEntity.updateLoginEntity import UpdateLoginEntity
from WorkerEntity.createWorkerEntity import CreateWorkerEntity
from WorkerEntity.getWorkerEntity import GetWorkerEntity
from WorkerEntity.searchWorkerEntity import WorkerSearchEntity
from WorkerEntity.updateWorkerEntity import UpdateWorkerEntity


class LoginService:
    m_createLogin = CreateLoginEntity()
    m_getLoginEntity = GetLoginEntity()
    m_updateLoginEntity = UpdateLoginEntity()
    m_loginSearchEntity = LoginSearchEntity()
    m_entityHelper = EntityHelper()

    def create(self, builder):
        assert builder is not None, "WorkerPb Cannot be empty"
        self.m_createLogin.start(builder=builder)
        return self.m_createLogin.done()

    def get(self, id):
        assert id is not '', "id cannot be empty"
        self.m_getLoginEntity.start(id=id)
        return self.m_getLoginEntity.done()

    def update(self, id, builder):
       # assert builder.dbInfo.id is not '', "DbInfo id cannot be empty"
        assert id is not '', "id cannot be empty"
        assert builder is not None, "builder cannot be empty"
        if (self.m_entityHelper.comapreIds(id1=id, id2=builder.dbInfo.id)):
            assert True ,"Upadting Wrong Entity"
        self.m_updateLoginEntity.start(id=id, builder=builder)
        return self.m_updateLoginEntity.done()

    def search(self, builder):
        assert builder is not None, "LoginSearchRequest Cannot be empty"
        self.m_loginSearchEntity.start(builder=builder)
        return self.m_loginSearchEntity.done()

    def delete(builder):
        assert builder.dbInfo.id is not '', "DbInfo id cannot be empty"
        print(builder)
