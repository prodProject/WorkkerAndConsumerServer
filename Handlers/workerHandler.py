from CommonCode.convertJSONTOPb import ConvertJSONToPb
from CommonCode.convertPbToJSON import ConvertPbToJSON
from Services.workerService import WorkerService
from protobuff import worker_pb2, workersearch_pb2


class WorkerHandler:



    @staticmethod
    def getWorker(id):
        service = WorkerService()
        m_convertPbtoJson = ConvertPbToJSON()
        return m_convertPbtoJson.converPbtojson(service.get(id=id))

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

    @staticmethod
    def countWorker(builder):
        if (builder != None):
            m_converter = ConvertJSONToPb()
            builder = m_converter.converjsontoPBProper(response=builder,instanceType=workersearch_pb2.WorkerSearchRequestPb())

        service = WorkerService()
        return service.count(builder=builder)

