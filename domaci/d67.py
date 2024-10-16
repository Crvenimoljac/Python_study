#67.	Napiši Python program koji kreira rečnik sa proizvodima i njihovim cenama. 
# Program treba da omogući korisniku da unese naziv proizvoda i novu cenu,
#  a zatim da ažurira cenu u rečniku
proizvodi_cene = {
    "Mleko": 120,
    "Hleb": 60,
    "Jaja": 150,
    "Sir": 400,
    "Jogurt": 80,
}
print(proizvodi_cene)
pr=(input("Unesi naziv proizvoda:")).capitalize()
cena=int(input("Unesi novu cenu proizvoda:"))
proizvodi_cene[pr]=cena
print(proizvodi_cene)
