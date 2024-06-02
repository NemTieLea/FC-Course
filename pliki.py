from helpers import zamien_przecinki_na_spacje

# plik = open("test.txt")
# zawartosc_pliku = plik.readlines()
# plik.close()

with open("test.txt", "r") as plik:
    # zawartosc_pliku = plik.read().strip()
    zawartosc_pliku = []
    for linia in plik:
        zawartosc_pliku.append(linia.strip())

print(zawartosc_pliku)

# dane_do_zapisu = []
# for linia in zawartosc_pliku:
#     dane_do_zapisu.append(
#         zamien_przecinki_na_spacje(linia) + "\n"
#     )
#
# with open("nowy_tekst.txt", "w") as plik:
#     plik.writelines(dane_do_zapisu)
#
# with open("nowy_tekst_2.txt", "w") as plik:
#     for linia in zawartosc_pliku:
#         nowa_linia = zamien_przecinki_na_spacje(linia) + "\n"
#         plik.write(nowa_linia)
