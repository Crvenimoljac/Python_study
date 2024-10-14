# Napiši Python program koji definiše funkciju saberi, koja prima dva broja kao argumente i vraća njihov zbir. 
# Program zatim traži od korisnika da unese dva broja, poziva funkciju saberi, i ispisuje rezultat.

def saberi(a:int,b:int)->int: # saberi naziv fje, a i b su argumenti(ulazni), a c je izlazni argument
    c=a+b
    return c #return kljucna rec vraca podatak



x=int(input("prvi broj: "))
y=int(input("unesi drugi broj: "))
sum=saberi(x,y) #pozivanje fje saberi
print(sum)