from CommonCode.strings import Strings

# (select json_array_elements(json_extract_path(json_extract_path(raw_data,'contactDetails'),'secondryMobile'))->> 'number')= '8687598496'
from Searcher.sercherConfig import SearcherConfig
from Searcher.workerSearcher import WorkerSearcher, WorkerSearchConfig


class SercherHelper:

    def getCondition(self, cond, value):
        return cond + '=' + Strings.qoutedString(value)

    def getConditionForCheckingInJsonArray(self, listKey, fieldKey, key, value):
        return "(select json_array_elements(json_extract_path(json_extract_path(raw_data," + Strings.qoutedString(
            listKey) + ")," + Strings.qoutedString(fieldKey) + "))->>" + Strings.qoutedString(
            key) + ")=" + Strings.qoutedString(value)

    def getOrCond(self, cond1, cond2):
        return cond1 + SearcherConfig.OR + cond2
