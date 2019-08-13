class WorkerEntityHelper:

    def createWorkerEntity(self, id, builder):
        builder.dbInfo.id = id
        return builder
