# class Pracownik:
#     def __init__(self, imie_nazwisko, stanowisko):
#         self.imie_nazwisko = imie_nazwisko
#         self.stanowisko = stanowisko
#
#
# nowy_pracownik = Pracownik(imie_nazwisko='Adam Kowalski', stanowisko='Programista')


class Samochod:
    def __init__(self, marka, kolor, model, max_poziom_paliwa, przyciemniane_szyby=False):
        self.marka = marka
        self.kolor = kolor
        self.model = model
        self.poziom_paliwa = 0
        self.przycemniane_szyby = przyciemniane_szyby
        self.max_poziom_paliwa = max_poziom_paliwa

    def wyswietl_parametry(self):
        print(f"Marka: {self.marka} | Model: {self.model} | Kolor: {self.kolor}")

    def dolej_paliwo(self, liczba_litrow):
        if self.poziom_paliwa + liczba_litrow > self.max_poziom_paliwa:
            print("Przelewa sie!")
            self.poziom_paliwa = self.max_poziom_paliwa
        else:
            self.poziom_paliwa += liczba_litrow

    def wyswietl_poziom_paliwa(self):
        print(f"W baku jest {self.poziom_paliwa}l paliwa.")


fiat_500 = Samochod(marka='Fiat', kolor='czerwony', model='500', max_poziom_paliwa=35)
fiat_500.wyswietl_poziom_paliwa()
fiat_500.dolej_paliwo(5)
fiat_500.wyswietl_poziom_paliwa()


# mazda_mx5 = Samochod(marka='Mazda', kolor='czarny', model='MX-5')
#
#
# for s in [fiat_500, mazda_mx5]:
#     # print(f"{s.marka} koloru {s.kolor}")
#     s.wyswietl_parametry()
