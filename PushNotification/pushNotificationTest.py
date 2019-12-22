from pyfcm import FCMNotification

push_service = FCMNotification(
    api_key="AAAAltGCeGs:APA91bElD5bksaGH4oLKIvCSPLvzpVZMX3UxuMII1LkOyVzJ_D7xA53XCQt-n4pI1rkRc10VnZuHgJKvHx_M-0yXkI9pIouhZvQHfsRMmrmo3T84y-YTfbTcuez3-lxGBcDBKOBRpMH1")
registration_id = "eos8TWsI1Ag:APA91bH29FNU55vqq6KaeijzFl8A1DxysFgqPmVtBg6BzY0t1237xlVeEpv2fJUi0fsHf0IZ02KzbcrAcguREXO0TMfOMGsUCT_n7JV69Kj_S8aGwaKGPdWA9h8UGeI37GJJEs43xshe"
message_title = "Prod update"
message_body = "Hi john, your customized news for today is ready"
result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)
