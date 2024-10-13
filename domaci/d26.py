a=input("Napisi mi nesto: \n")
b=input("Napisi rec koja se nalazi u tvojoj recenici: \n")
c=0
d=a.split()
e=len(d)
f=0
while f!=e:
    if (a.find(b)!=-1):
        c=c+1
    else :
        exit
    
    f=f+1
print(c)
    