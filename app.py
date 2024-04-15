LIMIT_OSOB_W_KLUBIE = 3
liczba_osob_w_klubie = 0

# Iteracja petli

# while True:
#     wiek = int(input("Podaj wiek: "))
#     if 18 <= wiek <= 110:
#         print("Dobry wiek, Zapraszamy!")
#         liczba_osob_w_klubie += 1
#         print(f"Liczba osob w klubie: {liczba_osob_w_klubie}")
#     if liczba_osob_w_klubie >= LIMIT_OSOB_W_KLUBIE:
#         break
#
# print("Klub jest pelny :(")

# ilosc_przywitan = int(input("Ile razy sie przywitac?"))
#
# for idx in range(ilosc_przywitan):
#     print("Hej!")
#
# print("-" * 20)
#
# licznik = 0
# while licznik < ilosc_przywitan:
#     print("Hej!")
#     licznik += 1

# ---------------
# continue
# break
# for idx in range(5):
#     if idx > 3:
#         break
#     print(idx)
#     if idx % 2 == 0:
#         print(f"Parzysta {idx}")
#         continue
#     print(f"Liczba: {idx}")

# ---------------
suma_ocen = 0
liczba_przedmiotow = 0

while True:
    ocena = input("Podaj ocene: ")
    if not ocena:
        print("Koniec wpisywania")
        break
    ocena = int(ocena)
    if ocena < 1 or ocena > 6:
        print(f"Bledna ocena: {ocena}, sprobuj ponownie")
        continue
    suma_ocen += ocena
    liczba_przedmiotow += 1

if liczba_przedmiotow == 0:
    print("nie ma przedmiotow, nie ma sredniej")
else:
    print(f"Srednia to: {suma_ocen / liczba_przedmiotow}")

# for numer_przedmiotu in range(10):
#     ocena = int(input("Podaj ocene: "))
#     suma_ocen += ocena
# print(f"Srednia to: {suma_ocen / liczba_przedmiotow}")
