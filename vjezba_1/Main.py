from vjezba_1.Razlomak import Razlomak

#Vježba 1.0
'''
Stvori datoteku razlomak.py
Napravi klasu Razlomak koja će imati dva atributa brojnik i nazivnik.
Brojnik i nazivnik se šalju kao argumenti tijekom inicijalizacije klase
Napravi svojstva za čitanje i pisanje brojnika i nazivnika.
Napravi metodu skrati() koja će skratiti razlomak, na primjer. razlomak 3/12 se može skratiti na 1/4.
'''

print("Zadatak 1:\n")

r1 = Razlomak(3, 12)

print("Brojnik razlomka = ", r1.brojnik, ", nazivnik razlomka =", r1.nazivnik)
print("To string metoda:", repr(r1))

print(" --------------------------- ")

r1.brojnik = 4
r1.nazivnik = 20

print("Brojnik razlonka = ", r1.brojnik, ", nazivnik razlomka =", r1.nazivnik)
print("To string metoda:", repr(r1))

print(" --------------------------- ")

r1.skrati
#---------------------------------------------------------------------

print("\n---------------------------\n")

'''
U klasi razlomak napravi specijalnu metodu __str__() koja će služiti za ispis razlomka u oblikubrojnik|nazivnik i specijalnu metodu __repr__() za reprezentaciju razlomka.
Napravi specijalne metode za operacije usporedbe razlomaka.
'''

print("Zadatak 2:\n")

r2 = Razlomak(5, 30)

print("Novokreirani razlomak:", str(r2) + " ili " + repr(r2))

print(" --------------------------- ")

print(repr(r1) + " == " + repr(r2) + " ->", r1 == r2)
print(repr(r1) + " >= " + repr(r2) + " ->", r1 >= r2)
print(repr(r1) + " < " + repr(r2) + " ->", r1 < r2)
#---------------------------------------------------------------------

print("\n---------------------------\n")

'''
klasi razlomak napravi specijalnu metode za zbrajanje, oduzimanje, množenje i dijeljenje razlomaka.
'''

print("Zadatak 3:\n")

r3 = Razlomak(3, 4)
r4 = Razlomak(5, 2)

'''
r3 = r1
r4 = r2
'''

#Zbrajanje
print("Zbrajanje:", repr(r3), "+", repr(r4), "=", r3 + r4)

#Oduzimanje
print("\nOduzimanje:", repr(r3), "+", repr(r4), "=", r3 - r4)

#Množenje
print("\nMnoženje:", repr(r3), "*", repr(r4), "=", r3 * r4)

#Djeljenje
print("\nDjeljenje:", repr(r3), "/", repr(r4), "=", r3 / r4)

print("\n---------------------------\n")
