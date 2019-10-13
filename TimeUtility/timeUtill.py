import time

from protobuff.time_pb2 import TimePb


class TimeUtil:
    def getTimePb(self, timeZone):
        timepb = TimePb()
        millis = self.getCurrentMillis()
        timepb.milliseconds = millis
        timepb.timezone = timeZone
        return self.getTimePbWithCurrentTime(timepb=timepb,
                                             formattedDate=self.getCurrentTimethroughMillis(millis=millis))

    def getCurrentMillis(self):
        return int(time.time() * 1000.0)

    def getCurrentTimethroughMillis(self, millis):
        return time.strftime('%Y-%m-%d  %H:%M:%S', time.localtime(millis / 1000.0))

    def getTimePbWithCurrentTime(self, timepb, formattedDate):
        list = formattedDate.split()
        list2 = list[0].split('-')
        timepb.year = list2[0]
        timepb.month = list2[1]
        timepb.date = list2[2]
        timepb.formattedDate = formattedDate
        return timepb
