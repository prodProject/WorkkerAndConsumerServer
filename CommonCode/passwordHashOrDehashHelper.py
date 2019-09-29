import bcrypt


class PasswordHasherOrDeHasher:

    def getHashFromPassword(self, password):
        return bcrypt.hashpw(password, bcrypt.gensalt())

    def getPasswordFromHash(self, actualPassword, hashedPassword):
        return bcrypt.checkpw(actualPassword, hashedPassword)
