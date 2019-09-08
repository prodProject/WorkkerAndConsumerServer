from enum import Enum

from Database.databaseConnection import DatabaseConnection
from Database.databaseHelper import DatabaseHelper
from Enums.databaseTables import Tables


class States(Enum):
    START = 0,
    GET_TABLES_FROM_DB = 1,
    CREATE_IF_NOT_EXISTS = 2,
    DONE = 3,


class CreateTableIfNotExists:
    m_dbConnection = DatabaseConnection()
    m_helper = DatabaseHelper()

    response = None

    def start(self):
        self.controlFlow(currentState=States.GET_TABLES_FROM_DB)

    def getTablesFromDb(self):
        query = self.m_helper.getAllTableQuery()
        conn = self.m_dbConnection.getConnection()
        cursor = conn.cursor()
        cursor.execute(query)
        self.response = cursor.fetchall()
        conn.close()
        conn.close()
        self.controlFlow(currentState=States.CREATE_IF_NOT_EXISTS)

    def createTable(self):
        print(type(self.response))
        if (len(self.response) == 0):
            for table in Tables:
                if (table == Tables.UNKNOWN):
                    continue
                if (Tables.ENTITY_DATA not in table):
                    try:
                        query = self.m_helper.getCreateEntityTableQuery(table=table.name)
                        conn = self.m_dbConnection.getConnection()
                        cursor = conn.cursor()
                        cursor.execute(query)
                        conn.commit()
                        conn.close()
                        conn.close()
                    except:
                        print()
                elif (table == Tables.WORKER_TYPE):
                    try:
                        query = self.m_helper.getWorkerTypeTableQuery(table=table.name)
                        conn = self.m_dbConnection.getConnection()
                        cursor = conn.cursor()
                        cursor.execute(query)
                        conn.commit()
                        conn.close()
                        conn.close()
                    except:
                        print()
                else:
                    try:
                        query = self.m_helper.getCreateTableQuery(table=table.name)
                        conn = self.m_dbConnection.getConnection()
                        cursor = conn.cursor()
                        cursor.execute(query)
                        conn.commit()
                        conn.close()
                        conn.close()
                    except:
                        print()
        else:
            for table in Tables:
                if (table == Tables.UNKNOWN):
                    continue
                if (table not in self.response and table == Tables.ENTITY_DATA):
                    try:
                        query = self.m_helper.getCreateEntityTableQuery(table=table.name)
                        conn = self.m_dbConnection.getConnection()
                        cursor = conn.cursor()
                        cursor.execute(query)
                        conn.commit()
                        conn.close()
                        conn.close()
                    except:
                        print()
                elif (table not in self.response and table == Tables.WORKER_TYPE):
                    try:
                        query = self.m_helper.getWorkerTypeTableQuery(table=table.name)
                        conn = self.m_dbConnection.getConnection()
                        cursor = conn.cursor()
                        cursor.execute(query)
                        conn.commit()
                        conn.close()
                        conn.close()
                    except:
                        print()
                elif (table not in self.response):
                    try:
                        query = self.m_helper.getCreateTableQuery(table=table.name)
                        conn = self.m_dbConnection.getConnection()
                        cursor = conn.cursor()
                        cursor.execute(query)
                        conn.commit()
                        conn.close()
                        conn.close()
                    except:
                        print()

    def controlFlow(self, currentState):
        if (currentState == States.GET_TABLES_FROM_DB):
            self.getTablesFromDb()
        elif (currentState == States.CREATE_IF_NOT_EXISTS):
            self.createTable()
        elif (currentState == States.DONE):
            self.done()
