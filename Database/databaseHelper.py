from CommonCode.convertPbToJSON import ConvertPbToJSON


class DatabaseHelper:
    m_pbConvertor = ConvertPbToJSON()
    BASE_QUERY = "SELECT * FROM"
    BASE_UPDATE_QUERY = "UPDATE"
    BASE_INSERT_QUERY = 'INSERT INTO'
    BASE_RAW_DATA_QUERY = "SELECT raw_data FROM "

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
        return self.BASE_INSERT_QUERY + ' "' + table + '"' + "( dbid , raw_data) " + " VALUES " + "(" + self.getSingleQuotedString(
            data.dbInfo.id) + " , " + self.m_pbConvertor.converPbtojsonString(
            builder=data) + ");"

    def getRowDataQuery(self, table, id):
        return self.BASE_RAW_DATA_QUERY + ' "' + table + '"' + "WHERE dbid = " + self.getSingleQuotedString(id) + ";"

    def updateRawDataEntityQuery(self, id,newPb,table):
        return self.BASE_UPDATE_QUERY + ' "' + table + '"' + " SET raw_data = " + self.m_pbConvertor.converPbtojsonString(
            builder=newPb) + " WHERE dbid = "+ self.getSingleQuotedString(id)+" ;"
