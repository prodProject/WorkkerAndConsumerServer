class PasswordHelper:

    def getPasswordFromLoginPb(self, loginPb):
        return loginPb.workerRef.name.firstName + '@' + loginPb.password
