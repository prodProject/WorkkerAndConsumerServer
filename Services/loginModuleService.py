from LoginModule.loginControlFlow import Login


class LoginModuleService:
    m_login = Login()

    def login(self, loginRequestPb):
        self.m_login.start(loginReq=loginRequestPb)
        return self.m_login.done()
