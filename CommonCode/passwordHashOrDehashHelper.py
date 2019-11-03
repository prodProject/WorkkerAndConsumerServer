import bcrypt


class PasswordHasherOrDeHasher:

    def getHashFromPassword(self, password):
        pass_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        return pass_hash.decode('utf-8')

    def getPasswordFromHash(self, actualPassword, hashedPassword):
        return bcrypt.checkpw(actualPassword.encode('utf-8'), hashedPassword.encode('utf-8'))
