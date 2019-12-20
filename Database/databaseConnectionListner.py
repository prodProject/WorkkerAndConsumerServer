from ConstantsProperties.databaseCredentials import ServerTypeEnvironment
from Enums.serverTypeEnum import ServerTypeEnvironmentEnum


class DatabaseConnectionListner:
    m_serverTypeEnvironment = ServerTypeEnvironment()

    def __init__(self):
        self.getConnectionListner()

    def getConnectionListner(self):
        self.m_serverTypeEnvironment.setEnvironment(environmentType=ServerTypeEnvironmentEnum)

    def getEnvironment(self):
        return self.m_serverTypeEnvironment
