from game.constants import PI as PI_DOBRE
from game.panstwa_miasta.models import PI as PI_BLEDNE
from game.panstwa_miasta.models import Rekord
from game.panstwa_miasta.models import Gracz
from helpers import zamien_przecinki_na_spacje
from settings import env_settings

r = Rekord(identyfikator=1, imie="Anna", miasto="Berlin", panstwo="Niemcy")
# print(r.dlugosc_imienia())

g = Gracz(identyfikator=1, imie="Anna", nazwisko="Nowak")

tekst_r = str(r)
tekst_r = zamien_przecinki_na_spacje(tekst_r)
# print(tekst_r)


print("Wartosc pi:", PI_DOBRE)
print("wartosc pi zla:", PI_BLEDNE)

