from CommonCode.convertPbToJSON import ConvertPbToJSON
from CommonCode.strings import Strings
from Enums.databaseTables import Tables
from protobuff.workertype_pb2 import WorkerTypeEnum


class DatabaseHelper:
    m_pbConvertor = ConvertPbToJSON()
    BASE_QUERY = "SELECT * FROM"
    BASE_UPDATE_QUERY = "UPDATE"
    BASE_INSERT_QUERY = 'INSERT INTO'
    BASE_RAW_DATA_QUERY = "SELECT raw_data FROM "
    BASE_COUNT_RAW_DATA_QUERY = "SELECT count(raw_data) FROM "

    def getBaseQuery(self):
        return self.BASE_QUERY

    def getQuotedString(self, data):
        return '"' + data + '"'

    def getSingleQuotedString(self, data):
        return "'" + data + "'"

    def getEntityQuery(self, data):
        return self.BASE_QUERY + ' "' + data + '"'

    def updateEntityQuery(self, data, value):
        return self.BASE_UPDATE_QUERY + ' "' + data + '"' + " SET dbid = " + value + " WHERE id = 1"

    def getInsertQuery(self, table, data):
        if(table == Tables.WORKER_TYPE.name):
            print(type(data.workerType))
            return self.BASE_INSERT_QUERY + ' "' + table + '"' + "( dbid ,workertype, raw_data) " + " VALUES " + "(" + self.getSingleQuotedString(
                data.dbInfo.id) + " , " + self.getSingleQuotedString(
                str(WorkerTypeEnum.Name(data.workerType))) + " , " + self.m_pbConvertor.converPbtojsonString(
                builder=data) + ");"
        else:
            return self.BASE_INSERT_QUERY + ' "' + table + '"' + "( dbid , raw_data) " + " VALUES " + "(" + self.getSingleQuotedString(
                data.dbInfo.id) + " , " + self.m_pbConvertor.converPbtojsonString(
                builder=data) + ");"

    def getRowDataQuery(self, table, id):
        return self.BASE_RAW_DATA_QUERY + ' "' + table + '"' + "WHERE dbid = " + self.getSingleQuotedString(id) + ";"

    def updateRawDataEntityQuery(self, id, newPb, table):
        return self.BASE_UPDATE_QUERY + ' "' + table + '"' + " SET raw_data = " + self.m_pbConvertor.converPbtojsonString(
            builder=newPb) + " WHERE dbid = " + self.getSingleQuotedString(id) + " ;"

    def getAllTableQuery(self):
        return "SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'"

    def getCreateTableQuery(self, table):
        return 'CREATE TABLE'+'"'+table+'"'+'(id serial PRIMARY KEY,dbid VARCHAR (255) UNIQUE NOT NULL,raw_data json NOT NULL);'

    def getCreateEntityTableQuery(self, table):
        return 'CREATE TABLE '+'"'+table+'"'+' (id serial PRIMARY KEY,dbid VARCHAR (255) UNIQUE NOT NULL);'

    def getWorkerTypeTableQuery(self,table):
       return 'CREATE TABLE'+'"'+table+'"'+'(id serial PRIMARY KEY,dbid VARCHAR (255) UNIQUE NOT NULL,workertype VARCHAR (255) UNIQUE NOT NULL,raw_data json NOT NULL);'

    def getSearchQuery(self,table,subquery):
       return self.BASE_RAW_DATA_QUERY +'"'+table+'" WHERE '+ subquery + ';'

    def getCountQuery(self,table,subquery):
        if(Strings.isEmpty(subquery)):
            return self.BASE_COUNT_RAW_DATA_QUERY +'"'+table+'" WHERE '+ 'true' + ';'
        else:
            return self.BASE_COUNT_RAW_DATA_QUERY +'"'+table+'" WHERE '+ subquery + ';'
