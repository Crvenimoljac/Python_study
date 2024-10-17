
# ukoliko datoteka ne postoji, python ce da kreira datoteku
with open('primer.txt','w') as file: # r-za citanje, w-za pisanje u datoteku, a-za dodavanje
    file.write("tekst\n")

# citanje iz datoteke
with open('primer.txt', 'r') as file: 
    data = file.read()  # Čitanje cijelog sadržaja
    print(data)  # Ispis sadržaja

# dodavanje u datoteku na kraju
with open('primer.txt','a') as file:
    file.write("nova linija")

file.close()# zatvara datoteku