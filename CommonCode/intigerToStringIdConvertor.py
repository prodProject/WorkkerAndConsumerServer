import numpy
import math

class IntigerToStringIdConverter:

    def convert(self,id):
        ALPHABET = numpy.array(
            ["G", "k", "v", "s", "y", "4", "g", "3", "j", "b", "x", "r", "A", "o", "l", "6", "R", "f", "0", "F", "m",
             "B", "U", "p", "D", "i", "t", "7", "8", "S", "L", "2", "w", "d", "Z", "u", "n", "q", "Y", "O", "E", "V",
             "h", "H", "Q", "5", "W", "C", "1", "J", "X", "M", "e", "9", "T", "I", "K", "c", "a", "z", "N", "P"])
        ENCODE_LENGTH = ALPHABET.size
        list = []
        while True:
            list.append(ALPHABET[id % ENCODE_LENGTH])
            id = math.floor(id / ENCODE_LENGTH)
            if id <= 0:
                break
        list.reverse()
        return ''.join(list)
