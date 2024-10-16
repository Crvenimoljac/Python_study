#Napiši Python program koji kreira prazan rečnik i omogućava korisniku da dodaje imena i godine. 
# Program treba da se završi kada korisnik unese "kraj", a zatim da ispiše ceo rečnik.
recnik={}
while  True:
    ime=input("Unesi ime: ")
    if ime=="kraj":
        print(recnik)
        break
    godine=input("Unesi godine: ")
    recnik[ime]=godine
