from enum import Enum


class ServerTypeEnvironmentEnum(Enum):
    UNKNOWN_ENV = 0
    DEVEL_1 = 1,
    DEVEL_2 = 2,
    DEVEL_3 = 3,
    DEVEL_4 = 4,
    PROD = 5,

    @staticmethod
    def getEnum(name):
       return ServerTypeEnvironmentEnum.__getattr__(name=name)
