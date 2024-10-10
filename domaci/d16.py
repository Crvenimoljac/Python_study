import math
c=float(input("Unesi cenu proizvoda: "))
a=int(input("Unesi da li si clan kluba ili ne, 0 za ne a 1 za da: "))
b=c-((c*10)/100)
if a==True:
    print(f"Ti si clan kluba i cena za tebe je{b}")
else:
    print("Ti nisi clan kluba")


