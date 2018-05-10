from Skarbonka import *


def rozbicieSkarbonki():
    czyUderzyl = True
    while czyUderzyl:
        czyUderzyl = False
        try:
            czyRozbic = input("Aby rozbic skarbonke wcisnij T, aby kontynuowac wcisnij inny klawisz")
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


def czyUtworzycNowaSkarbonke(zawartoscRozbitej):
    utworzono = True
    print("Rozbito skarbonke, oto Twoje monety: {}".format(zawartoscRozbitej))
    nowaSkarbonka = input("Aby utworzyc nowa wcisnij U")
    if nowaSkarbonka == "U":
        utworzono = False
    else:
        pass
    return utworzono

if __name__ == '__main__':

    zawartoscRozbitej = []
    utworzono = False
    while not utworzono:
        utworzono, skarbonka = utworzenieSkarbonki()
        if not utworzono:
            continue
        else:
            pass
        for i in range(10):
            if not skarbonka.getRozbita():

                wprowadzenieMonety()
                zawartoscRozbitej = rozbicieSkarbonki()

            else:
                utworzono = czyUtworzycNowaSkarbonke(zawartoscRozbitej)
                break
