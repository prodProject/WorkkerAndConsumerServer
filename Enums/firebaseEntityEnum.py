from enum import Enum


class FirebaseEntityEnum(Enum):
    UNKNOWN_ENITY = 0
    VERIFICATIONCODE = 1,

    @staticmethod
    def getEnum(name):
        return FirebaseEntityEnum.__getattr__(name=name)
