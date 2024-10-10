prosek=float(input("Unesi svoj prosek ocena: "))

if prosek >9:
    print("Tvoj prosek je odlican")
elif prosek>7 or prosek <8:
    print("Tvoj prosek je vrlo dobar")
elif prosek>5 or prosek <6:
    print("Tvoj prosek je dobar")
elif prosek <5:
    print("Tvoj prosek je odlican")