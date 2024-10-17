import json # ukljucenje biblioteke

# citanje iz json fajla se vrsi na isti nacin kao i iz obicnih datoteka
# samo sto se poziva kljucna rec dump()
file="json.json"
data=json.load(file)

# upisivanje u json
data="tekst"
json.dump(data)