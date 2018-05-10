from Exceptions import *

class Moneta:
    def __init__(self, wartosc, waluta):
        if wartosc in [1, 2, 5, 10, 20, 50, 100, 200, 500]:
            self._wartosc = wartosc
        else:
            raise ZlyNominalException(wartosc)
        self._waluta = waluta

    def getWart(self):
        return self._wartosc

    def getWaluta(self):
        return self._waluta