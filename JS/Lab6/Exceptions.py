class ZlyNominalException(Exception):
    def __init__(self, wyr):
        self._expression = wyr
        self._message = "Wprowadzony nominal {} nie istnieje".format(self._expression)
        # print(self.message)
        super().__init__(self._message)

    def getMessage(self):
        return self._message

class WalutaSkarbonkiException(Exception):
    def __init__(self, wyr):
        self._expression = wyr
        self._message = "{} jest nieznana waluta".format(self._expression)

    def getMessage(self):
        return self._message


class NieznanaWalutaException(Exception):
    def __init__(self, wyr):
        self._expression = wyr
        self._message = "{} nie pasuje do utworzonej skarbonki".format(self._expression)

    def getMessage(self):
        return self._message

class UderzylesSieWPalecException(Exception):
    def __init__(self):
        self._message = "Trafiles w palec zamiast w skarbonke"

    def getMessage(self):
        return self._message