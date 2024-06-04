import sys

print("Uruchamian skrypt:", sys.argv[0])
if len(sys.argv) > 1 and sys.argv[1].endswith('.txt'):
    print("Wczytuje z pliku...")
    wejscie = open("produkcja.txt")
    wyjscie = open("produkcja.txt", "w")
else:
    print("Wczytuje ze standardowego wejscia...")
    wejscie = sys.stdin
    wyjscie = sys.stdout

while True:
    tekst = wejscie.readline().strip()
    if not tekst.strip():
        break
    wyjscie.write("==> " + tekst + "\n")

wejscie.close()
