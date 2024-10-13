a=int(input("Unesi broj: \n"))
b=1 
c=a
for i in range(a):
        b*=c
        c-=1
        i+=1

print(f"Faktorijal od {a} je: {b}")

