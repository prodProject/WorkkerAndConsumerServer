from VerificationModule.verification import CreateVerification


class CreateVerificationService:
    m_service = CreateVerification()

    def craeteVerification(self,builder):
        assert builder is not None, "Email Cannot be empty"
        assert builder.workerRef.dbInfo.id is not '', "id Cannot be empty"
        self.m_service.start(builder=builder)
        return self.m_service.done()
