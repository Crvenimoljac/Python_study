#48.	Napiši Python program koji traži od korisnika da unese 5 brojeva u listu, a zatim pronalazi i ispisuje maksimalni i minimalni element iz te liste.
num_lis=[]
for i in range(1,6):
    dig=int(input(f"Unesi {i}. broj"))
    num_lis.append(dig)
print(f"Minimalni broj u nizu je: {min(num_lis)}, a maksmalni broj je: {max(num_lis)}.")