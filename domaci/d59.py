#59.Napiši Python program koji definiše funkciju faktorijel, koja prima celobrojni broj i vraća njegov faktorijel.
#  Program zatim traži od korisnika da unese broj, poziva funkciju i ispisuje rezultat.
def faktorijel(n:int):
    #faktorijel od 5!=5*4*3*2*1 = 1*2*3*4*5
    a=1
    for i in range(1, n+1):
        a*=i
    return a
f=int(input("Unesi br ciji faktorijel zels da izracunas: "))
print(f"faktorijel od {f} je {faktorijel(f)}")
