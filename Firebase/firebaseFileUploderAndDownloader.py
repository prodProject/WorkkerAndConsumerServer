import pyrebase as pyrebase

from Firebase.firebaseConfigCredentials import FirebaseConfigCredenrials


class FirebaseFileUploaderAndDownloader:
    m_filebaseConfigCredentials = FirebaseConfigCredenrials();
    m_storage = None

    def getConnection(self):
        firebase = pyrebase.initialize_app(self.m_filebaseConfigCredentials.getConfig())
        self.m_storage = firebase.storage();

    def upload(self, uploadPath, filePath):
        if (self.m_storage is None):
            self.getConnection();
        else:
            self.m_storage.child(uploadPath).put(filePath)
