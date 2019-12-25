from protobuff.pushnotification_pb2 import PushNotificationSearchRequestPb, PushNotifiactionBuilderPb, MULTIPLE, SINGLE


class SendPushNotificationHelper:

    def getPushNotificationSearchRequest(self, pushNotificationRequestPb):
        pushNotificationSearchRequest = PushNotificationSearchRequestPb()
        pushNotificationSearchRequest.workerRef.CopyFrom(pushNotificationRequestPb.workerRef)
        return pushNotificationSearchRequest

    def getPushNotificationBuilder(self, searchResponse):
        tokenList = list()
        pushNotifiactionBuilder = PushNotifiactionBuilderPb()
        if (len(tokenList) > 1):
            for pushNotificationPb in searchResponse:
                tokenList.append(pushNotificationPb.tokenId)
            pushNotifiactionBuilder.registrationIds.extend(tokenList)
            pushNotifiactionBuilder.sendType = MULTIPLE
        else:
            pushNotifiactionBuilder.registrationId = searchResponse[0].tokenId
            pushNotifiactionBuilder.sendType = SINGLE
        pushNotifiactionBuilder.subject = 'Hello'
        pushNotifiactionBuilder.body = 'This is Test'
        return pushNotifiactionBuilder
