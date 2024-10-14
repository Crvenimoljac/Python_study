#47.	Napiši Python program koji traži od korisnika da unese nekoliko brojeva u listu, a zatim ispisuje prvi i poslednji element te liste. Prekid unosa izvrsiti recju kraj.
num_list=[]
while True:
    a=(input("Unesi neki broj: "))
    if a=="kraj":
        break
    num_list.append(a)
if len(num_list)>0:
    print(f"Prvi broj u nizu je {num_list[0]}, a zadnji je {num_list[-1]}")
else:
    print("Niz je prazan.")
    
