#54.	Napiši Python program koji definiše funkciju celsius_u_fahrenheit, 
# koja prima temperaturu u stepenima Celzijusa i vraća temperaturu u stepenima Farenhajta. 
# Program zatim traži od korisnika da unese temperaturu u Celzijusima, 
# poziva funkciju i ispisuje rezultat.
def celsius_u_fahrenheit(c:int):
    f=(c*(9/5))+32
    return f
cl=int(input("Unesi temperaturu u celzijusima: \n"))
print(f"Temperatura u farenhajtima je{celsius_u_fahrenheit(cl)}")