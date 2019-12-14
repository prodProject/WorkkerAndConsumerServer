from Enums.serverTypeEnum import ServerTypeEnvironmentEnum


class ServerTypeEnvironment():
    environment = ServerTypeEnvironmentEnum.UNKNOWN_ENV
    HOST = "";
    DATABASE_NAME = "";
    USER = "";
    PORT = "";
    PASSWORD = "";
    URL = "";

    def setEnvironment(self, environmentType):
        self.environment = environmentType
        if (environmentType == ServerTypeEnvironmentEnum.DEVEL_4):
            self.HOST = "ec2-54-235-114-242.compute-1.amazonaws.com"
            self.DATABASE_NAME = "dd6edd764lms8p"
            self.USER = "xtqyijfiggpgjo"
            self.PORT = "5432"
            self.PASSWORD = "b12965e42cc95a4908ae1ddbe7b82ec159c6bbfe3ceee48ebb7e5d8042ac40bc"
            self.URL = "postgres://xtqyijfiggpgjo:b12965e42cc95a4908ae1ddbe7b82ec159c6bbfe3ceee48ebb7e5d8042ac40bc@ec2-54-235-114-242.compute-1.amazonaws.com:5432/dd6edd764lms8p"
        elif (environmentType == ServerTypeEnvironmentEnum.DEVEL_1):
            self.HOST = "ec2-54-243-198-191.compute-1.amazonaws.com"
            self.DATABASE_NAME = "d4h6ni1grvaic4"
            self.USER = "nonvvuuxoqypbo"
            self.PORT = "5432"
            self.PASSWORD = "af3708ecf7c5983d4442a20e4281fb2e61de9a1ce1ec9f6da7d2939c96221e12"
            self.URL = "postgres://nonvvuuxoqypbo:af3708ecf7c5983d4442a20e4281fb2e61de9a1ce1ec9f6da7d2939c96221e12@ec2-54-243-198-191.compute-1.amazonaws.com:5432/d4h6ni1grvaic4"
        elif (environmentType == ServerTypeEnvironmentEnum.DEVEL_2):
            self.HOST = "ec2-54-227-249-108.compute-1.amazonaws.com"
            self.DATABASE_NAME = "d3cuv0e9io634"
            self.USER = "bmcjergbxijjzr"
            self.PORT = "5432"
            self.PASSWORD = "e8555097cbff0b9162e4bdef2260cadf55fb37f52b55a714acad6f7d9a85aa1c"
            self.URL = "postgres://bmcjergbxijjzr:e8555097cbff0b9162e4bdef2260cadf55fb37f52b55a714acad6f7d9a85aa1c@ec2-54-227-249-108.compute-1.amazonaws.com:5432/d3cuv0e9io634"
        elif (environmentType == ServerTypeEnvironmentEnum.DEVEL_3):
            self.HOST = "ec2-174-129-214-193.compute-1.amazonaws.com"
            self.DATABASE_NAME = "d38k0vjb88v0ul"
            self.USER = "pxhbqeivkcbqtt"
            self.PORT = "5432"
            self.PASSWORD = "3566b47063e01eb1ba758cd7a71aebdeb7b728aaf0141b3328bd0b14923a22bf"
            self.URL = "postgres://pxhbqeivkcbqtt:3566b47063e01eb1ba758cd7a71aebdeb7b728aaf0141b3328bd0b14923a22bf@ec2-174-129-214-193.compute-1.amazonaws.com:5432/d38k0vjb88v0ul"
        elif (environmentType == ServerTypeEnvironmentEnum.PROD):
            self.HOST = "ec2-75-101-128-10.compute-1.amazonaws.com"
            self.DATABASE_NAME = "d1f19masnqpvta"
            self.USER = "qplcbhjxqmkqnq"
            self.PORT = "5432"
            self.PASSWORD = "8ce3f23aec9a8d66467e8469d8d7c0eb30e26039f121838acd3ab560d8fdfcfd"
            self.URL = "postgres://qplcbhjxqmkqnq:8ce3f23aec9a8d66467e8469d8d7c0eb30e26039f121838acd3ab560d8fdfcfd@ec2-75-101-128-10.compute-1.amazonaws.com:5432/d1f19masnqpvta"

    def getHost(self):
        return self.HOST

    def getDatabaseName(self):
        return self.DATABASE_NAME

    def getUser(self):
        return self.USER

    def getPort(self):
        return self.PORT

    def getPassword(self):
        return self.PASSWORD

    def getUrl(self):
        return self.URL

    def getServerEnvironment(self):
        return self.environment
