#61.Napiši Python program koji definiše funkciju spoji_liste, 
# koja prima dve liste i vraća novu listu koja je kombinacija prvih i drugih. 
# Program zatim traži od korisnika da u
# nese elemente za dve liste, poziva funkciju i ispisuje rezultat.
def spoji_liste(lista1:list, lista2:list)->list:
    return lista1 + lista2

l1=[]
l2=[]
while True:
    el=input("unesi za l1:")
    if el=="kraj":
        break
    l1.append(el)

while True:
    el=input("unesi za l2:")
    if el=="kraj":
        break
    l2.append(el)

print(spoji_liste(l1,l2))