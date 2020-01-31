from CommonCode.convertJSONTOPb import ConvertJSONToPb
from CommonCode.convertPbToJSON import ConvertPbToJSON
from Services.consumerService import ConsumerService


class ConsumerHandler:



    @staticmethod
    def getConsumer(id):
        service = ConsumerService()
        m_convertPbtoJson = ConvertPbToJSON()
        return m_convertPbtoJson.converPbtojson(service.get(id=id))

    @staticmethod
    def createConsumer(builder):
        service = ConsumerService()
        m_converter = ConvertJSONToPb()
        builder = m_converter.converjsontoPBProper(response=builder,instanceType=consumer_pb2.ConsumerPb())
        return service.create(builder=builder)

    @staticmethod
    def updateConsumer(builder):
        service = ConsumerService()
        m_converter = ConvertJSONToPb()
        builder = m_converter.converjsontoPBProper(response=builder,instanceType=consumer_pb2.ConsumerPb())
        return service.update(id=builder.dbInfo.id,builder=builder)

    @staticmethod
    def searchConsumer(builder):
        service = ConsumerService()
        m_converter = ConvertJSONToPb()
        builder = m_converter.converjsontoPBProper(response=builder,instanceType=consumersearch_pb2.ConsumerSearchRequestPb())
        return service.search(builder=builder)

    @staticmethod
    def countConsumer(builder):
        if (builder != None):
            m_converter = ConvertJSONToPb()
            builder = m_converter.converjsontoPBProper(response=builder,instanceType=consumersearch_pb2.ConsumerSearchRequestPb())

        service = ConsumerService()
        return service.count(builder=builder)

