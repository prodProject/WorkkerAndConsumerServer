class WorkerEntityHelper:

    def createWorkerEntity(self, id, builder):
        builder.dbInfo.id = id
        return builder

    def comapreIds(self, id1, id2):
        if (id1 == id2):
            return False
        else:
            return True
