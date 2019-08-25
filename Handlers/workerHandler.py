from CommonCode.convertJSONTOPb import ConvertJSONToPb
from Services.workerService import WorkerService
from protobuff import worker_pb2


class WorkerHandler:



    @staticmethod
    def getWorker(id):
        service = WorkerService()
        return service.get(id=id)

    @staticmethod
    def createWorker(builder):
        service = WorkerService()
        m_converter = ConvertJSONToPb()
        builder = m_converter.converjsontoPBProper(response=builder,instanceType=worker_pb2.WorkerPb())
        return service.create(builder=builder)
