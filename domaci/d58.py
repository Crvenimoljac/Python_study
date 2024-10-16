#58.	Napiši Python program koji definiše funkciju fibonacijev_niz,
#  koja prima broj n i vraća listu prvih n brojeva iz Fibonacijevog niza. 
# Program zatim traži od korisnika da unese broj, 
# poziva funkciju i ispisuje rezultat.
# Svaki novi član niza se dobija kao zbir prethodna 2.

def fibonacijev_niz(n:int):
    a,b=0,1
    r=[]
    for b in range(n):
        a,b=b,a+b
        r.append(a)
    return r

#Ispravljen kod
def fibonacci(n:int)->list:
    arr=[0,1]
    for i in range(2,n+1):
        next_fib=arr[-1]+arr[-2]
        if next_fib>n:
            break
        arr.append(next_fib)
    return arr

a=int(input("Unesi broj do kog zelis da izracunas fibonacijev niz: \n"))
print(f"\n\nFibonacijev niz do {a} broja je: {fibonacci(a)}")

#arr=[0,1]
#next_fib=1+0 (1)
#arr=[0,1,1]
#next_fib=1+1 (2)
#arr=[0,1,1,2]
#next_fin=2+1 (3)
#arr=[0,1,1,2,3]
#next_fin=3+2 (5)
#arr=[0,1,1,2,3,5]
#next_fin=5+3 (8)
#arr=[0,1,1,2,3,5,8]