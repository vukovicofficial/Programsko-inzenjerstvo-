from vjezba_3.Multiskup import MultiSkup

print("Zadatak 3.1 - MultiSkup")
dict = MultiSkup([1,1,2,2,2,3,3,4])

print(dict)

print("-------------------------------------------------------------------------------------\n")

print("Zadatak 3.2 - MultiSkup")

for el in dict:
    print(el)

print(repr(dict))

print("-------------------------------------------------------------------------------------\n")

print("Zadatak 3.3 - MultiSkup")

dict.add(1)
print("Dodavanje samo sa key-em: ", dict)

dict.add(1, 3)
print("Za key '1' value nadodajemo 3: ", dict)

dict.remove(1, 2)
print("Za key '1' value oduzimamo 2: ", dict)

print("-------------------------------------------------------------------------------------")






