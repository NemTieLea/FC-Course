wiek = int(input("Twoj wiek: "))
wzrost = int(input("Twoj wzrost w cm: "))

# if 18 <= wiek <= 110:
#     print(f"Podany wiek: {wiek}")
# else:
#     if wiek < 18:
#         print("Jestes za mlody(-a)")
#     if wiek > 100:
#         print("Czy na pewno podano dobry wiek?")

# if wiek < 14 and wzrost < 140:
#     print("Nie mozna wejsc do sklepu!")
# elif wiek <14 and wzrost >= 140:
#     print("Mozna wejsc do sklepu")
# elif wiek > 16 and wzrost < 140:
#     print("Nie mozna wejsc do sklepu")
# elif wiek > 18 and wzrost < 120:
#     print("Nie mozna wejsc do sklepu")
# else:
#     print("Mozna wejsc do sklepu")

if wiek < 14:
    if wzrost < 140:
        print("Nie mozna wejsc do sklepu!")
    else:
        print("Mozna wejsc do sklepu")
elif wiek > 14:
    if wzrost < 140:
        print("Nie mozna wejsc do sklepu")
    else:
        print("Mozna wejsc do sklepu")
elif wiek > 18:
    if wzrost < 120:
        print("Nie mozna wejsc do sklepu")
    else:
        print("Mozna wejsc do sklepu")
else:
    print("Mozna wejsc do sklepu")
