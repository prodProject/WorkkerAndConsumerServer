from protobuff.time_pb2 import TimeZoneEnum


class TimeZomeFormattor:

    def format(self,timezone):
        return {
            TimeZoneEnum.IST: "Asia/Kolkata",
            TimeZoneEnum.UTC: "UTC",
            TimeZoneEnum.UNKNOWN_TIME_ZONE : ""
        }.get(timezone)
