import psycopg2

from ConstantsProperties import databaseCredentials

connection = None


class DatabaseConnection:

    def getConnection(self):
        try:
            print("Your are Connecting...")
            global connection
            connection = psycopg2.connect(user=databaseCredentials.USER,
                                          password=databaseCredentials.PASSWORD,
                                          host=databaseCredentials.HOST,
                                          port=databaseCredentials.PORT,
                                          database=databaseCredentials.DATABASE_NAME)
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)
        if (connection):
            print("Your are Connected...")
        return connection

    def closeConnection(self,connection):
        connection.close()
