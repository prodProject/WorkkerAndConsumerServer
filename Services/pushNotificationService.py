from Helper.entityHelper import EntityHelper
from PushNotifiactionEntity.createPushNotificationEntity import CreatePushNotificationEntity
from PushNotifiactionEntity.getPushNotificationEntity import GetPushNotificationEntity
from PushNotifiactionEntity.searchPushNotificationEntity import PushNotificationSearchEntity
from PushNotifiactionEntity.updatePushNotificationEntity import UpdatePushNotificationEntity


class PushNotificationService:
    m_createPushNotification = CreatePushNotificationEntity()
    m_getPushNotificationEntity = GetPushNotificationEntity()
    m_updatePushNotificationEntity = UpdatePushNotificationEntity()
    m_pushNotificationSearchEntity = PushNotificationSearchEntity()
    m_workerEntityHelper = EntityHelper()

    def create(self, builder):
        assert builder is not None, "PushNotificationPb Cannot be empty"
        self.m_createPushNotification.start(builder=builder)
        return self.m_createPushNotification.done()

    def get(self, id):
        assert id is not '', "id cannot be empty"
        self.m_getPushNotificationEntity.start(id=id)
        return self.m_getPushNotificationEntity.done()

    def update(self, id, builder):
        assert id is not '', "id cannot be empty"
        assert builder is not None, "builder cannot be empty"
        if (self.m_workerEntityHelper.comapreIds(id1=id, id2=builder.dbInfo.id)):
            assert True ,"Upadting Wrong Entity"
        self.m_updatePushNotificationEntity.start(id=id, builder=builder)
        return self.m_updatePushNotificationEntity.done()

    def search(self, builder):
        assert builder is not None, "PushNotificationSearchRequest Cannot be empty"
        self.m_pushNotificationSearchEntity.start(pushNotificationSearchReqPb=builder)
        return self.m_pushNotificationSearchEntity.done()

    def delete(builder):
        assert builder.dbInfo.id is not '', "DbInfo id cannot be empty"
        print(builder)
