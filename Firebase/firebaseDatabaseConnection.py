from firebase import firebase


class FireBaseDatabaseConnection:
    BASE_URL = "https://prod-project-c3a7b.firebaseio.com/"
    connection = None

    def __init__(self):
        self.connection = firebase.FirebaseApplication(self.BASE_URL, None)

    def getConnection(self):
        if (self.connection is not None):
            return self.connection;
        else:
            self.__init__()
            return self.connection;
