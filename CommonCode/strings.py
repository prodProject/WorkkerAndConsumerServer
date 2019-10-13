class Strings:

    @staticmethod
    def isEmpty(string):
        if string == '':
            return True
        elif string == None:
            return True
        else:
            return False

    @staticmethod
    def notEmpty(string):
        return not Strings.isEmpty(string)

    @staticmethod
    def length(string):
        return len(string)

    @staticmethod
    def qoutedString(string):
        return "'"+string+"'"

    @staticmethod
    def getFormattedEmail(builder):
        return builder.localPart+'@'+builder.domain
