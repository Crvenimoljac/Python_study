a=input("Napisi mi svoju sifru: \n")
b=0
c=a
print("Unesi sifru ponovo.\n")
while b!=3:
    a=input()
    if c==a:
        print("Uneli ste ispravnu sifru.")
        exit()
    else:
        print("Pokusaj ponovo.")
    b=b+1
