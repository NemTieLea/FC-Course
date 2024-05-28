from game.constants import PI
# from ..constants import  PI

print("jestem w models.py")

class Rekord:
    def __init__(self, identyfikator, imie, miasto, panstwo, pi=PI):
        self.id = identyfikator
        self.imie = imie
        self.miasto = miasto
        self.panstwo = panstwo
        self.pi = pi

    def dlugosc_imienia(self):
        return len(self.imie)

    def __str__(self):
        return f"{self.id},{self.imie},{self.miasto},{self.panstwo}"


class Gracz:
    def __init__(self, identyfikator, imie, nazwisko):
        self.id = identyfikator
        self.imie = imie
        self.nazwisko = nazwisko
