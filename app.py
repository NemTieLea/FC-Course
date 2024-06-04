import os


def skopiuj_plik_tekstowy(src, dst):
    with open(src) as fr:
        with open(dst, "w") as fw:
            for line in fr:
                fw.write(line)


pid = os.getpid()
print(f"Aktualny proces ma id: {pid}")
with open("run.pid", "w") as f:
    f.write(f"{pid}")


folder_backup = input("podaj nazwe folderu backup: ")
print(f"Backup w folderze: {folder_backup}")

if not os.path.exists(folder_backup):
    os.mkdir(folder_backup)

folder_oryginalny = "dane"
if not os.path.isdir(folder_oryginalny):
    print(f"Folder oryginalny {folder_oryginalny} nie jest folderem.")
else:
    for nazwa_pliku in os.listdir(folder_oryginalny):
        if nazwa_pliku.endswith(".txt"):
            poczatkowa_sciezka = os.path.join(folder_oryginalny, nazwa_pliku)
            docelowa_sciezka = os.path.join(folder_backup, nazwa_pliku)
            skopiuj_plik_tekstowy(poczatkowa_sciezka, docelowa_sciezka)

os.remove("run.pid")
