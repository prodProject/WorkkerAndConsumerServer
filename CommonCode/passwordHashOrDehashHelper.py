import bcrypt


class PasswordHasherOrDeHasher:

    def getHashFromPassword(self, password):
        return bcrypt.hashpw(password, bcrypt.gensalt()).decode('utf-8')

    def getPasswordFromHash(self, actualPassword, hashedPassword):
        return bcrypt.checkpw(actualPassword.encode('utf-8'), hashedPassword)
