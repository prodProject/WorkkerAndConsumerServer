from enum import Enum


class PasswordMode(Enum):
    UNKNOWN_PASSWORD = 0;
    GENERATE_PASSWORD = 1;
    VERIFY_PASSWORD = 2;
    GENEREATE_NEW_PASSWORD = 3;

    @staticmethod
    def getEnum(name):
       return PasswordMode.__getattr__(name=name)
