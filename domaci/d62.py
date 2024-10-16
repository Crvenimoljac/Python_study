#Napiši Python program koji kreira rečnik sa imenom, prezimenom i godinama korisnika. 
# Program treba da traži od korisnika da unese svoje podatke, a zatim da ispiše rečnik.
Mojipodac={}
ime=input("Unesi ime koje zelis da se nalazi u nizu: ")
prezime=input("Unesi prezime koje zelis da se nalazi u nizu: ")
godine=input("Unesi koliko ima godina: ")
Mojipodac["ime"]=ime
Mojipodac["prezime"]=prezime
Mojipodac["Godine"]=godine
print(Mojipodac)