from PrzechowywaczMonet import *
from Exceptions import *
import random

class Skarbonka(PrzechowywaczMonet):
    def __init__(self, waluta):
        PrzechowywaczMonet.__init__(self, [1, 2, 5, 10, 20, 50, 100, 200, 500])
        self._rozbita = False
        self._dozwWaluty = ["PLN", "GP", "EUR"]
        if waluta not in self._dozwWaluty:
            raise WalutaSkarbonkiException(waluta)
        self.waluta = waluta

    def addMoneta(self, nMoneta):
        if (not isinstance(nMoneta, Moneta)):
            print("Przesłany obiekt nie jest monetą")
        elif (nMoneta.getWaluta() != self.waluta):
            raise NieznanaWalutaException(nMoneta.getWaluta())
        else:
            self._zawartosc.append(nMoneta.getWart())

    def rozbij(self):
        if random.randint(1, 10) != 1:
            self._rozbita = True
            self._zwracanaZawartosc = self._zawartosc[:]
            self._zawartosc.clear()
            return self._zwracanaZawartosc
        else:
            raise UderzylesSieWPalecException()

    def getRozbita(self):
        return self._rozbita
    # def getZawart(self):
    #    print("Nie można wyciągnąć pojedynczej monety")