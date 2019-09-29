from Password.genereateAndVerifyPassword import GenereateAndVerifyPassword


class PasswordService:
    m_service = GenereateAndVerifyPassword()

    def getOrVerifyPassword(self,loginpb,mode):
        self.m_service.start(pb=loginpb,mode=mode)
        return self.m_service.done()
