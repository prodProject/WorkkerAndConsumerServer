from Services.createVerificationService import CreateVerificationService
from Services.verificationService import VerificationService
from protobuff.verification_pb2 import VerificationPb

m_service = VerificationService()

m_verificationPb  = VerificationPb()
m_verificationPb.workerRef.dbInfo.id = "G"
m_verificationPb.workerRef.name.firstName = "Shubham"
m_verificationPb.workerRef.name.lastName = "Tiwari"
m_verificationPb.code = "1111"

print(m_service.update(data=m_verificationPb))
