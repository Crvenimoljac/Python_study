
lista=[] # prazna lista
lista_prevoznih_sredstava=["auto", "kamion", "avion", "traktor", "auto"]
print(lista_prevoznih_sredstava) # STAMPANJE LISTE
print(lista_prevoznih_sredstava[2]) # stampanje odredjenog elementa liste
lista_prevoznih_sredstava.append("kombi") # dodavanje elemenata u listu
lista_brojeva = [2024,1999,1945,1918,1389,1318,1055,33,1]
lista_brojeva.sort() # sortiranje elementata u listi
lista_prevoznih_sredstava.remove("avion") # izbacuje iz liste element
print(lista_prevoznih_sredstava.count("auto")) #prebrojava broje elemenata koji se ponavljaju u listi

# 45. Napiši Python program koji traži od korisnika da unese 5 brojeva i smesti ih u listu, a zatim ispisuje tu listu.
list_num=[]

for i in range(1,6):
    num=int(input(f"Unesi {i}. broj: "))
    list_num.append(num)
list_num.sort()
print(list_num)