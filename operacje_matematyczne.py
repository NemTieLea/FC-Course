zmienna_1 = 120
zmienna_2 = 6

suma = zmienna_1 + zmienna_2
print("Suma:", suma)

roznica = zmienna_1 - zmienna_2
print("Roznica:", roznica)

iloczyn = zmienna_1 * zmienna_2
print("iloczyn:", iloczyn)

iloraz = zmienna_1 / zmienna_2
print("iloraz:", iloraz)

potega = zmienna_1 ** zmienna_2
print("potega:", potega)

print(3 % 2)    # 1
print (4 % 2)   # 0
print(6 % 3)    # 0
print(5 % 3)    # 2

print(50 * '-')

zmienna_1 = 10
zmienna_2 = 20

print("10 < 20:", zmienna_1 < zmienna_2)
print("10 > 20:", zmienna_1 > zmienna_2)
print("100 == 100:", 100 == 100)
print("123 != 123:", 123 != 123)    #czy sa rozne
# <=     mniejszy rowny
# >=     wiekszy rowny

print(50 * '-')

a = True
b = False

print("a lub b:", a or b)
print("a i b:", a and b)
print("Nie-b:", a and not b)

print(50 * '-')

liczba_w_tekscie = "10"
print(int(liczba_w_tekscie) * 5)

print(50 * '-')

# Sprawdzanie czy wartosc jest pusta
print(bool(1))
print(bool(-10))
print(bool(0))
print(bool(0.0))

print("Pusty tekst:", bool(""))
print("Niepusty tekst:", bool("teeeekssstttt"))

print("None:", bool(None))

print(50 * '-')

# Sprawdzanie typów
a = "Ciąg znaków"
print(type(a) is str)
print(type(a) is not int)

print(50 * '-')

a = "123"
print(int(a) * 2)

print(a + str(5))
