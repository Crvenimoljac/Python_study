# SINTAX
naziv_recnika={
   "kljuc1":"vrednost1",
   "kljuc2":"vrednost2",
   "kljuc3":"vrednost3",
   "kljuc_n":"vrednost_n"
}
# stampanje
print(naziv_recnika["kljuc1"]) # stampa samo gde je kljuc ->[value]
print(naziv_recnika) # stampa ceo recnik ->[dict]
x = naziv_recnika.get("kljuc2") # dodeljuje promenljivoj vrednost kljuca ->[value]
print(x)
keys=naziv_recnika.keys() # dodeljuje promenljivoj kljuceve recnika -> [list]
print(keys)
values=naziv_recnika.values() #dodeljuje promenljivoj vrednosti recnika ->[list]
print(values)
items=naziv_recnika.items() # dodeljuje promenljivoj parove ->[list]
print(items)
