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
        return "'" + string + "'"

    @staticmethod
    def getFormattedEmail(builder):
        return builder.localPart + '@' + builder.domain

    @staticmethod
    def getTittleCaseStringMaker(data):
        Char1 = '^'
        Char2 = '^^'
        resultString = ''
        counter = 1
        for x in data.split(' '):
            if (counter == 1):
                resultString = resultString + Char2 + x.lower()
            else:
                resultString = resultString + Char1 + x.lower()
            counter = counter+1
        return resultString
