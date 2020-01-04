from Services.consumerService import ConsumerService
from protobuff.consumer_pb2 import ConsumerPb, ConsumerSearchRequestPb
from protobuff.entity_pb2 import ACTIVE
from protobuff.mobile_pb2 import ISD_91
from protobuff.persontypeenum_pb2 import CONSUMER

consumerService = ConsumerService()

consumer = ConsumerSearchRequestPb();
consumer.lifeTime=ACTIVE
#consumer.contactDetails.primaryMobile.number = '9876543210'
print(consumer)
print(consumerService.search(builder=consumer))
