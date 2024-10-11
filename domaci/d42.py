a=1
i=""
while i=="":
    i=input("Unesi do kog broja zelis da proveris neparnost, akohoces da izadjes napisi izlaz: \n")
    if i=="izlaz":
        print("izlaz is programa, cao")
        exit()
    if not i.isnumeric():
        print("Morate uneti samo ceo broj")
        i=""
    
while a<=int(i):
    if a%2!=0:
        print (a)
    a+=1
