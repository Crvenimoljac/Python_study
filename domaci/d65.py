#65.Napiši Python program koji kreira rečnik sa imenima i godinama,
# a zatim omogućava korisniku da unese ime koje želi da obriše iz rečnika.

dummy_recnik = {
    "Marko": 31,
    "Ana": 25,
    "Petar": 22,
    "Milica": 28,
    "Jovan": 35,
    "Sara": 27,
    "Toma": 33,
    "Lana": 29,
    "Nikola": 31,
    "Katarina": 24,
}
ime=input("Unesi ime koje zelis da obrises: ").capitalize()
if ime in dummy_recnik:
    dummy_recnik.pop(ime)
    print(dummy_recnik)