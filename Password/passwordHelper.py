class PasswordHelper:

    def getPasswordFromLoginPb(self, loginPb):
        return str(loginPb.workerRef.name.firstName + '@' + loginPb.password)
