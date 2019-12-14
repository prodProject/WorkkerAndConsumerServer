import os

from ConstantsProperties.databaseCredentials import ServerTypeEnvironment
from Enums.serverTypeEnum import ServerTypeEnvironmentEnum


class DatabaseConnectionListner:
    m_serverTypeEnvironment = ServerTypeEnvironment()

    def __init__(self):
        self.getConnectionListner()

    def getConnectionListner(self):
        environment = os.environ.get('SERVER_ENVIRONMENT', 3)
        if (environment == 3):
            self.m_serverTypeEnvironment.setEnvironment(environmentType=ServerTypeEnvironmentEnum.DEVEL_4)
        else:
            self.m_serverTypeEnvironment.setEnvironment(environmentType=ServerTypeEnvironmentEnum.getEnum(environment))

    def getEnvironment(self):
        return self.m_serverTypeEnvironment
