#58.	Napiši Python program koji definiše funkciju fibonacijev_niz,
#  koja prima broj n i vraća listu prvih n brojeva iz Fibonacijevog niza. 
# Program zatim traži od korisnika da unese broj, 
# poziva funkciju i ispisuje rezultat.
# Svaki novi član niza se dobija kao zbir prethodna 2.
def fibonacijev_niz(n:int):
    a,b=0,1
    r=[]
    for b in range(n):
        r.append(a)
        a,b=b,a+b
    return r
a=int(input("Unesi broj do kog zelis da izracunas fibonacijev niz: \n"))
print(f"Fibonacijev niz do {a} broja je:{fibonacijev_niz(a)} ")