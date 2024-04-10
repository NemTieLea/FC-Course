
szablon = """{}, wszystkiego najlepszego z okazji {} urodzin!

{}

{}"""

imie_odbiorcy = input("Podaj imie odbiorcy: ")
data_urodzenia = input("Podaj date urodzenia: ")
spersonalizowana_wiadomosc = input("Napisz spersalizowana wiadomosc: ")
imie_nadawcy = input("Podaj swoje imie: ")

wiek = 2024 - int(data_urodzenia)

print(szablon.format(imie_odbiorcy, wiek, spersonalizowana_wiadomosc, imie_nadawcy))
