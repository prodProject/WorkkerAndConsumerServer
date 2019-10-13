from RegisrationModule.registrationWorker import RegistrationWorker


class RegistrationWorkerService:
    m_registrationWorker = RegistrationWorker()

    def registration(self,registrationRequestPb):
        self.m_registrationWorker.start(workerPb=registrationRequestPb)
        return self.m_registrationWorker.done()
