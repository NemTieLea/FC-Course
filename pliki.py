import csv
import os

plik_csv = os.path.join("dane", "test.csv")
plik_csv_out = os.path.join("dane", "test-out.csv")

zawartosc = []

with open(plik_csv) as f:
    reader = csv.reader(f)
    for line in reader:
        zawartosc.append(line)

nowy_samochod = (5, "citroen", "c3", "bialy")
# zawartosc.append(nowy_samochod)

with open(plik_csv_out, "w") as f:
    writer = csv.writer(f)
    writer.writerow(nowy_samochod)

import json

plik_in_json = os.path.join("dane", "test.json")
plik_out_json = os.path.join("dane", "test-out.json")

with open(plik_in_json) as f:
    zawartosc = json.load(f)


nowy_samochod = {
    "id": 4,
    "marka": "ranault",
    "model": "kangoo",
    "kolor": "bialy"
}

zawartosc.append(nowy_samochod)

with open(plik_out_json, "w") as f:
    json.dump(zawartosc, f, indent=2)


import pickle

plik_in_pickle = os.path.join("dane", "test.pickle")
plik_out_pickle = os.path.join("dane", "test-out.pickle")

with open("test-out.pickle", "wb") as f:
    pickle.dump(zawartosc, f)

with open(plik_out_pickle, "rb") as f:
    zawartosc = pickle.load(f)

from pprint import pprint

pprint(zawartosc)
