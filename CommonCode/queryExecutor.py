import psycopg2

from CommonCode.intigerToStringIdConvertor import IntigerToStringIdConverter
from Database.databaseConnection import DatabaseConnection
from Database.databaseHelper import DatabaseHelper


class QueryExecuter:
    m_helper = DatabaseHelper()
    m_dbConnection = DatabaseConnection()
    m_encoder = IntigerToStringIdConverter()
    id = None

    def create(self, builder, table):
        try:
            query = self.m_helper.getInsertQuery(table=table, data=builder)
            print(query)
            conn = self.m_dbConnection.getConnection()
            cursor = conn.cursor()
            cursor.execute(query)
            if (cursor.rowcount == 1):
                conn.commit()
                conn.close()
                conn.close()
                return builder
            else:
                conn.commit()
                conn.close()
                conn.close()
                return None
        except (Exception, psycopg2.Error) as error:
            print("Error in update operation", error)

    def update(self, id, builder, table):
        try:
            query = self.m_helper.updateRawDataEntityQuery(id=id, newPb=builder, table=table)
            print(query)
            conn = self.m_dbConnection.getConnection()
            cursor = conn.cursor()
            cursor.execute(str(query))
            if (cursor.rowcount > 0):
                conn.commit()
                conn.close()
                cursor.close()
                return builder
            else:
                conn.commit()
                conn.close()
                cursor.close()
                return None
        except (Exception, psycopg2.Error) as error:
            print("Error in update operation", error)

    def get(self, id, table):
        try:
            query = self.m_helper.getRowDataQuery(table=table, id=id)
            print(query)
            conn = self.m_dbConnection.getConnection()
            cursor = conn.cursor()
            cursor.execute(query)
            if (cursor.rowcount == 1):
                row = cursor.fetchall()
                data = row[0]
                conn.commit()
                conn.close()
                cursor.close()
                return data[0]
            else:
                conn.commit()
                conn.close()
                cursor.close()
                return None
        except (Exception, psycopg2.Error) as error:
            print("Error in update operation", error)

    def search(self, query, table):
        try:
            query = self.m_helper.getSearchQuery(table=table, subquery=query)
            print(query)
            conn = self.m_dbConnection.getConnection()
            cursor = conn.cursor()
            cursor.execute(query)
            if (cursor.rowcount > 0):
                row = cursor.fetchall()
                conn.commit()
                conn.close()
                cursor.close()
                return row
            else:
                conn.commit()
                conn.close()
                cursor.close()
                return None
        except (Exception, psycopg2.Error) as error:
            print("Error in update operation", error)

    def count(self, table, query):
        try:
            query = self.m_helper.getCountQuery(table= table, subquery=query)
            print(query)
            conn = self.m_dbConnection.getConnection()
            cursor = conn.cursor()
            cursor.execute(query)
            if (cursor.rowcount > 0):
                row = cursor.fetchall()
                conn.commit()
                conn.close()
                cursor.close()
                data=row[0]
                return data[0]
            else:
                conn.commit()
                conn.close()
                cursor.close()
                return None
        except(Exception, psycopg2.Error) as error:
            print("Error in update operation", error)
