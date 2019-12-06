import psycopg2

from ConstantsProperties import databaseCredentials
from Database.databaseConnectionListner import DatabaseConnectionListner

connection = None


class DatabaseConnection(DatabaseConnectionListner):

    def getConnection(self):
        try:
            print("Your are Connecting...")
            global connection
            connection = psycopg2.connect(user=self.getEnvironment().getUser(),
                                          password=self.getEnvironment().getPassword(),
                                          host=self.getEnvironment().getHost(),
                                          port=self.getEnvironment().getPort(),
                                          database=self.getEnvironment().getDatabaseName())
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)
        if (connection):
            print("Your are Connected...")
        return connection

    def closeConnection(self, connection):
        connection.close()
