class Moneta:
    def __init__(self, arg, waluta):
        if arg in [1, 2, 5, 10, 20, 50, 100, 200, 500]:
            self._wartosc = arg
        else:
            self._wartosc = 0
        self._waluta = waluta

    def getWart(self):
        return self._wartosc

    def getWaluta(self):
        return self._waluta


class PrzechowywaczMonet:
    sth = 0

    def __init__(self, arg):
        self.sth = 0
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


class Skarbonka(PrzechowywaczMonet):
    def __init__(self, waluta):
        PrzechowywaczMonet.__init__(self, [1, 2, 5, 10, 20, 50, 100, 200, 500])
        self.waluta = waluta

    def addMoneta(self, nMoneta):
        if (not isinstance(nMoneta, Moneta)):
            print("Przesłany obiekt nie jest monetą")
        elif(nMoneta.getWaluta() != self.waluta):
            print("Nieznana waluta dla tej skarbonki")
        else:
            self._zawartosc.append(nMoneta.getWart())


    #def getZawart(self):
    #    print("Nie można wyciągnąć pojedynczej monety")


if __name__ == '__main__':
    prz = PrzechowywaczMonet(2)
    skarbonka = Skarbonka("PLN")
    skarbonka.addMoneta(Moneta(10, "PLN"))
    print(skarbonka.getZawart())
    skarbonka.addMoneta(Moneta(10, "PLN"))
    print(skarbonka.getZawart())
    skarbonka.addMoneta(Moneta(10, "EUR"))
    print(skarbonka.getZawart())
