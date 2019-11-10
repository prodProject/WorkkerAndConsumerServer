from CommonCode.convertJSONTOPb import ConvertJSONToPb
from CommonCode.convertPbToJSON import ConvertPbToJSON
from Services.workerTypeService import WorkerTypeService
from protobuff import workertype_pb2


class WorkerTypeHandler:



    @staticmethod
    def getWorkerType(id):
        service = WorkerTypeService()
        m_convertPbtoJson = ConvertPbToJSON()
        return m_convertPbtoJson.converPbtojson(service.get(id=id))

    @staticmethod
    def createWorkerType(builder):
        service = WorkerTypeService()
        m_converter = ConvertJSONToPb()
        builder = m_converter.converjsontoPBProper(response=builder,instanceType=workertype_pb2.WorkertypePb())
        return service.create(builder=builder)

    @staticmethod
    def updateWorkerType(builder):
        service = WorkerTypeService()
        m_converter = ConvertJSONToPb()
        builder = m_converter.converjsontoPBProper(response=builder,instanceType=workertype_pb2.WorkertypePb())
        return service.update(id=builder.dbInfo.id,builder=builder)

    @staticmethod
    def searchWorkerType(builder):
        service = WorkerTypeService()
        m_converter = ConvertJSONToPb()
        builder = m_converter.converjsontoPBProper(response=builder,instanceType=workertype_pb2.WorkerTypeSearchRequestPb())
        return service.search(builder=builder)
