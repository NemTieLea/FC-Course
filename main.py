WIEK_WEJSCIA_DO_KLUBU = 21

wiek_osoby = int(input("Podaj swoj wiek: "))

if wiek_osoby >= WIEK_WEJSCIA_DO_KLUBU:
    print("-> Moze wejsc do klubu.")
    print("-> Zapraszamy!")
elif wiek_osoby >= 18:
    print("-> Moze wejsc, ale nie pije alkoholu")
    print("-> Zapraszamy!")
elif wiek_osoby >= 16:
    print("-> Moze wejsc do strefy dla mlodych")
    print("-> Zapraszamy!")
else:
    print("-> Nie moze wejsc do klubu.")
    print("-> Pa pa!")

print("Koniec programu...")
