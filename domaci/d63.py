#63.Napiši Python program koji kreira rečnik sa imenima i telefonima.
#  Program treba da traži od korisnika da unese ime i da ispiše broj telefona za to ime, ako postoji.
imenik={
    "Lazar":4856,
    "ilija":35436,
    "jovan":7548,
    "marta":4756
}
ime=input("Unesi ime: ")
if ime in imenik:
    print(f"Broj telefona {ime} je {imenik[ime]}")
else:
    print("Korisnik se ne nalazi u recniku.")
    