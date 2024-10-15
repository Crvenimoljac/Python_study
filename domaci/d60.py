#60.Napiši Python program koji definiše funkciju generisi_kvadrate, 
# koja prima broj n i vraća listu kvadrata svih brojeva od 1 do n.
#  Program zatim traži od korisnika da unese broj,
#  poziva funkciju i ispisuje rezultat.
def generisi_kvadrate(n:int)->list:
    lis_kvad=[]
    for i in range (1,n):
        lis_kvad.append(i**2)
    return lis_kvad
kvad=int(input("unesi broj do kog zelis da izracunas kvadrate; \n"))
print(generisi_kvadrate(kvad))
