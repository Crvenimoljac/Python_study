#46.	Napiši Python program koji traži od korisnika da unese 5 brojeva u listu i zatim izračunava i ispisuje njihov zbir.
num_lista=[]
for i in range(1,6):
    num=int(input(f"Unesi {i}.broj koji zelis da dodas."))
    num_lista.append(num)
r=sum(num_lista)
print(num_lista, r)