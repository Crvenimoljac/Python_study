prosek=float(input("Unesi svoj prosek ocena: "))

if prosek >=9:
    print("Tvoj prosek je odlican")
elif prosek>=7 and prosek <9:
    print("Tvoj prosek je vrlo dobar")
elif prosek>5 and prosek <7:
    print("Tvoj prosek je dobar")
elif prosek <=5:
    print("Tvoj prosek je nedovoljan")