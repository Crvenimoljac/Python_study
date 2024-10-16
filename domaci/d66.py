#66.Napiši Python program koji kreira rečnik sa studentima i njihovim ocenama, 
# a zatim traži od korisnika da unese ocenu i ispisuje imena svih studenata koji su dobili tu ocenu.
studenti_ocene = {
    "Marko": 8,
    "Ana": 10,
    "Petar": 6,
    "Milica": 10,
    "Jovan": 7,
}
ocene=[]
ime=[]
ocena=int(input("Unesi ocenu studenta"))
for i,o in studenti_ocene.items():
    ime.append(i)
    ocene.append(o)

for x in ocene:
    if(x ==ocena):
        print(x)