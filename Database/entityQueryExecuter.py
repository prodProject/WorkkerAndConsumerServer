import psycopg2
from more_itertools import seekable

from CommonCode.intigerToStringIdConvertor import IntigerToStringIdConverter
from Database.databaseConnection import DatabaseConnection
from Database.databaseHelper import DatabaseHelper
from Enums.databaseTables import Tables


class EntityQueryExecuter:
    m_helper = DatabaseHelper()
    m_dbConnection = DatabaseConnection()
    m_encoder = IntigerToStringIdConverter()
    id = None

    def execute(self):
        try:
            query = self.m_helper.getEntityQuery(data=Tables.ENTITY_DATA.name)
            print(query)
            conn = self.m_dbConnection.getConnection()
            cursor = conn.cursor()
            cursor.execute(query)
            row = cursor.fetchall()[0]
            self.id = row[1]
            conn.close()
            return self.m_encoder.convert(id=int(row[1]))
        except (Exception, psycopg2.Error) as error:
            print("Error in update operation", error)

    def update(self):

        try:
            query = self.m_helper.updateEntityQuery(data=Tables.ENTITY_DATA.name, value=str(int(self.id) + 1))
            print(query)
            conn = self.m_dbConnection.getConnection()
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            count = cursor.rowcount
            print(count, "Record Updated successfully ")
            conn.close()
        except (Exception, psycopg2.Error) as error:
            print("Error in update operation", error)
