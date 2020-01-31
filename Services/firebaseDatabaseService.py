from FirebaseModuleEntity.firebaseCreateEntity import FirebaseCreateEntity
from FirebaseModuleEntity.firebaseGetEntity import FirebaseGetEntity
from FirebaseModuleEntity.firebaseUpdateEntity import FirebaseUpdateEntity


class FirebaseDatabaseService:
    m_create = FirebaseCreateEntity()
    m_get = FirebaseGetEntity()
    m_update = FirebaseUpdateEntity()

    def create(self, firebaseEnum, id, data):
        assert firebaseEnum is not None, "Enum Cannot be empty"
        assert id is not None, "id Cannot be empty"
        assert data is not None, "data Cannot be empty"
        self.m_create.start(firebaseEnum=firebaseEnum,id=id,data=data)
        return self.m_create.done()

    def get(self, firebaseEnum, id):
        assert id is not '', "id cannot be empty"
        assert firebaseEnum is not '', "id cannot be empty"
        self.m_get.start(firebaseEnum=firebaseEnum,id=id)
        return self.m_get.done()

    def update(self, firebaseEnum, id, data):
        assert firebaseEnum is not None, "Enum Cannot be empty"
        assert id is not None, "id Cannot be empty"
        assert data is not None, "data Cannot be empty"
        self.m_update.start(firebaseEnum=firebaseEnum,id=id,data=data)
        return self.m_update.done()
