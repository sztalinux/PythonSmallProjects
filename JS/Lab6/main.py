from Skarbonka import *


def rozbicieSkarbonki():
    czyUderzyl = False
    while not czyUderzyl:
        try:
            czyRozbic = input("Aby rozbic skarbonke wcisnij T")
            if czyRozbic == "T":
                zawartoscRozbitej = skarbonka.rozbij()
                return zawartoscRozbitej
            else:
                pass
        except UderzylesSieWPalecException as uderz:
            print(uderz.getMessage())
            czyUderzyl = True


def wprowadzenieMonety():
    try:
        walMonety = str.strip((input("Podaj walute")))
        try:
            wartMonety = int(input("Podaj wartosc monety w groszach"))
            skarbonka.addMoneta(Moneta(wartMonety, walMonety))
        except ValueError:
            print("Podales nieprawidlowa postac grosza")

    except ZlyNominalException as zly:
        print(zly.getMessage())
    except NieznanaWalutaException as niezn:
        print(niezn.getMessage())


def utworzenieSkarbonki():
    utworzono = False
    try:
        walSkarbonki = str.strip((input("Podaj walute jaka ma przechowywac skarbonka (PLN, GP, EUR)")))
        skarbonka = Skarbonka(walSkarbonki)
    except WalutaSkarbonkiException as wal:
        print(wal.getMessage(), end='\t')
        print("Sprobuj ponownie!")
        return (utworzono, 0)
    else:
        utworzono = True
        return (utworzono, skarbonka)


if __name__ == '__main__':

    zawartoscRozbitej = []
    utworzono = False
    while not utworzono:
        utworzono, skarbonka = utworzenieSkarbonki()
        print(utworzono)
        print(skarbonka)
        for i in range(10):
            if not skarbonka.getRozbita():

                wprowadzenieMonety()

                zawartoscRozbitej = rozbicieSkarbonki()

            else:
                print("Rozbito skarbonke, oto Twoje monety: {}".format(zawartoscRozbitej))
                print(skarbonka._zawartosc)
                nowaSkarbonka = input("Aby utworzyc nowa wcisnij U")
                if nowaSkarbonka == "U":
                    utworzono = False
                else:
                    pass
                break
