from VerificationEntity.createVerificationEntity import VerificationCreateEntity
from VerificationEntity.getVerificationEntity import VerificationGetEntity
from VerificationEntity.updateVerificationEntity import VerificationUpdateEntity


class VerificationService:
    m_create = VerificationCreateEntity()
    m_get = VerificationGetEntity()
    m_update = VerificationUpdateEntity()

    def create(self, data):
        assert data is not None, "data Cannot be empty"
        self.m_create.start(data=data)
        return self.m_create.done()

    def get(self, id):
        assert id is not '', "id cannot be empty"
        self.m_get.start(id=id)
        return self.m_get.done()

    def update(self, data):
        assert data is not None, "data Cannot be empty"
        self.m_update.start(data=data)
        return self.m_update.done()
