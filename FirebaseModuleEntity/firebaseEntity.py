import json

from google.protobuf.json_format import MessageToJson
from Firebase.firebaseDatabaseConnection import FireBaseDatabaseConnection


class FirebaseEntity:
    m_firebaseConnection = FireBaseDatabaseConnection()

    def create(self, firebaseEntityEnum, id, data):
        connection = self.m_firebaseConnection.getConnection()
        return connection.patch(self.getPartitionedUrl(firebaseEntityEnum=firebaseEntityEnum, id=id), json.loads(MessageToJson(data)))

    def get(self, firebaseEntityEnum, id):
        connection = self.m_firebaseConnection.getConnection()
        self.getPartitionedUrl(firebaseEntityEnum=firebaseEntityEnum,id=id)
        return connection.get(firebaseEntityEnum, id)

    def update(self, firebaseEntityEnum, id, data):
        connection = self.m_firebaseConnection.getConnection()
        return connection.patch(self.getPartitionedUrl(firebaseEntityEnum=firebaseEntityEnum, id=id), json.loads(MessageToJson(data)))

    def delete(self, firebaseEntityEnum, id):
        connection = self.m_firebaseConnection.getConnection()
        return connection.delete(firebaseEntityEnum, id)

    def getPartitionedUrl(self, firebaseEntityEnum, id):
        print(self.m_firebaseConnection.BASE_URL+ firebaseEntityEnum + "/" + id)
        return firebaseEntityEnum + "/" + id
