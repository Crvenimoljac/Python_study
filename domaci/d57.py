#57.Napiši Python program koji definiše funkciju stepen, 
# koja prima osnovu i eksponent i vraća rezultat stepenovanja.
#  Program zatim traži od korisnika da unese osnovu i eksponent,
#  poziva funkciju i ispisuje rezultat.
def stepen(base:int,exp:int):
    return base**exp
base=int(input("Unesi broj koji zelis da stepenujes: \n"))
exp=int(input("Unesi stepen: \n"))
print(f"{base}^{exp}={stepen(base,exp)}")
    