from enum import Enum


class Tables(Enum):
    UNKNOWN = 0;
    ENTITY_DATA = 1;
    WORKER_DATA = 2;
    WORKER_TYPE = 3;
    LOGIN=4

    @staticmethod
    def getEnum(name):
       return Tables.__getattr__(name=name)
