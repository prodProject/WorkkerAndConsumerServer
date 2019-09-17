from CommonCode.convertJSONTOPb import ConvertJSONToPb
from Services.workerService import WorkerService
from protobuff import worker_pb2, workersearch_pb2
from protobuff.workersearch_pb2 import WorkerSearchRequestPb


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

    @staticmethod
    def updateWorker(builder):
        service = WorkerService()
        m_converter = ConvertJSONToPb()
        builder = m_converter.converjsontoPBProper(response=builder,instanceType=worker_pb2.WorkerPb())
        return service.update(id=builder.dbInfo.id,builder=builder)

    @staticmethod
    def searchWorker(builder):
        service = WorkerService()
        m_converter = ConvertJSONToPb()
        builder = m_converter.converjsontoPBProper(response=builder,instanceType=workersearch_pb2.WorkerSearchRequestPb())
        return service.search(builder=builder)
