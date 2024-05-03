# Listy
"""
1. Elementy roznego typu
2. Mozna je zmieniac (dokladac i odejmowac elementy) - mutable
"""

# print("Element o indeksie 0 w liscie:")
# print(animals_2[0])
# print("\nElement o indeksie 1 w liscie:")
# print(animals_2[1])
# print("\nElement o indeksie -1 w liscie:")
# print(animals_2[-1])
#
# print("Pierwsze 6 elementow z listy:")
# print(animals[:6])
# print("Elementy listy od drugiego do szostego (rozlacznie - bez szostego):")
# print(animals[1:6])
# print("Elementy listy od pierwszego do ostatniego, co 3")
# print(animals[1::3])

animals_2 = [
    ["pies", "Azor", 12],
    ["kot", "Pat", 10],
    ["ryba", "Balbinka", 2],
]

example = ["a", "b", "c", "d"]
print("Przed dodaniem litery:", example)

example.append("e")
print("Po dodaniu litery:", example)

example.insert(2, "wstawka")
example.insert(2, "wstawka")
print("Po insert:", example)

cyfry = [1, 2, 3, 4, 5]
nowa_lista = example + cyfry
print("Wynik dodawania list:", nowa_lista, '\n\n')

print("example:", example)
while "wstawka" in example:
    example.remove("wstawka")
print("example po metodzie remove:", example, '\n\n')

example.append("c")
print("Example po dodaniu c:", example)
print("Element 'c' znajduje sie na indeksie:", example.index('c'), '\n')

print("'c' w example:", 'c' in example)
pusta_lista = []
nie_pusta_lista = [1, 2]
print("Pusta lista:", bool(pusta_lista))
print("Nie-pusta lista:", bool(nie_pusta_lista), '\n')

if nie_pusta_lista:
    print("Lista nie jest pusta")
else:
    print("Lista jest pusta\n")

print("nie_pusta_lista:", nie_pusta_lista)
nie_pusta_lista.extend([3, 4])
print("nie_pusta_lista po dodaniu:", nie_pusta_lista)


# Tuple, Krotka


krotka = (1, 2, 3, 4, )
print("Przykladowa krotka:", krotka)

krotka += ('a', 'b')
print("krotka po dodaniu:", krotka)

krotka_jednoelementowa = (1, ['a', 'b'])
print("Krotka jednoelementowa:", krotka_jednoelementowa, '\n')

# NIE NAZYWAMY ZMIENNYCH list, tuple

lista = ['a', 'b', 'c']
print("Lista:", lista)
krotka = tuple(lista)
print("Tuple:", krotka)
lista = list(krotka)
print("Lista:", lista)

var_1, var_2, var_3 = lista
print("Var 1:", var_1)
print("Var 2:", var_2)
print("Var 3:", var_3)

print()

animals = [
    ["pies", "Azor", 12],
    ["kot", "Pat", 10],
    ["ryba", "Balbinka", 2],
]

for (gatunek, imie, wiek) in animals:
    print(f"{imie} to {gatunek}, ma {wiek} lat.")

print()

# ZBIORY - set()
przykladowy_zbior = {"a", "abc", 1, True, None, False}
print(przykladowy_zbior)

print("Zbior:", przykladowy_zbior)
print("True w zbiorze:", True in przykladowy_zbior)
print("'abc' w zbiorze", 'abc' in przykladowy_zbior)
print()

# SLOWNIKI - dictionary - dict()
# print(id('abc')) - sprawdzanie id
slownik = {
    "Graniczna 1": ["Adam Nowak"],
    "Graniczna 2": ["Szlemek zero", "Sztabowy Jakub"],
    "Graniczna 4": [],
}

#adres = input("Jaki adres chcesz sprawdzic: ")
#print("Pod tym adresem mieszka:")
#print(slownik[adres])

slownik["Graniczna 5"] = ["Jan Nowak"]

for element in slownik:
    print("Klucz:", element, "Wartosc:", slownik[element])

print()

for klucz2, wartosc2 in slownik.items():
    print("Klucz:", klucz2, " | Wartosc:", wartosc2)

