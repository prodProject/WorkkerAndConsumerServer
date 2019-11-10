import hashlib

import bcrypt


class PasswordHasherOrDeHasher:

    def getHashFromPassword(self, password):
        pass_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        return pass_hash.decode('utf-8')

    def getPasswordFromHash(self, actualPassword, hashedPassword):
        return bcrypt.checkpw(actualPassword.encode('utf-8'), hashedPassword.encode('utf-8'))

    def getMd5hashFromPassWord(self, password):
        result = hashlib.md5(password.encode())
        return result.hexdigest()

    def getMd5PasswordMatch(self, actualPassword, hashedPassword):
        return self.getMd5hashFromPassWord(password=actualPassword) == hashedPassword
