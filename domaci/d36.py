a=int(input("Unesi broj: \n"))
c=1
i=1
for i in range(1, a+1):
        c*=i
        i+=1

print(f"Faktorijal od {a} je: {c}")

