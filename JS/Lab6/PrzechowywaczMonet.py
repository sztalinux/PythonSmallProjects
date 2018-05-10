from Moneta import *

class PrzechowywaczMonet:

    def __init__(self, arg):
        self._nominaly = arg
        self._zawartosc = []

    def addMoneta(self, nMoneta):
        if (isinstance(nMoneta, Moneta)):
            self._zawartosc.append(nMoneta.getWart())
        else:
            print("Przesłany obiekt nie jest monetą!")

    def getZawart(self):
        suma = 0
        for i in self._zawartosc:
            suma = suma + i
        return suma