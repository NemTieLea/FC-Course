
szablon = """Czesc, {}! 
Za 2 lata bedziesz mial {} lat."""

imie = input("Podaj swoje imie: ")
wiek = input("Podaj swoj wiek: ")
wiek_za_2_lata = int(wiek) + 2

print(szablon.format(imie, wiek_za_2_lata))
