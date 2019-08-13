from Entity.createEntity import CreateEntity


class EntityService:
    m_entity = CreateEntity()

    def get(self):
        self.m_entity.start()
        return self.m_entity.done()
