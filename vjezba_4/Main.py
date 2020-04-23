from vjezba_4.Trokut import Trokut
from vjezba_4.JednakokracniTrokut import JednakokracniTrokut
from vjezba_4.JednakostranicniTrokut import JednakostranicniTrokut

print("Zadatak 4.1\n")

'''
Zadatak 4.1 - TrokutStvori datoteku trokut.py
Napravi klasu Trokut i specijalnu metodu __init__() koja će primiti stranice trokuta a, b, c i spremiti ih uprivatni atribut __stranice.
Pri tome će se provjeravati jesu li sve stranice >= 0 i da li zadovoljavaju uvjettrokuta (zbroj dviju stranica je veći od treće stranice).
U jednom i u drugom slučaju podignut će se iznimka sporukom "Nije Trokut".
Napravi stringovnu reprezentaciju __str__() koja će za trokut sa stranicama 3,4,5 vratiti string "trokut 3 4 5".
Napravi reprezentaciju __repr__() koja će za trokut sa stranicama 3,4,5 vratiti string "Trokut(3,4,5)"
'''
lista_stranica =[(1,2,3),(3,4,5),(3,4,4),(3,3,3)]

for stranice in lista_stranica:
    try:
        t = Trokut(*stranice)
        print(repr(t))
    except Exception as e:
        print(e, stranice)

print("-------------------------------------------------------------------------------------\n")


print("Zadatak 4.2\n")

'''
Napravi metodu opseg() koja će vratiti opseg trokuta.
Napravi metodu povrsina() koja će vratiti površinu trokuta po Heronovoj formuli P=(s−a)(s−b)(s−c)√gdje je s polupseg.
'''

lista_stranica =[(3,4,5),(3,4,4),(3,3,3)]
for stranice in lista_stranica:
    t =Trokut(*stranice)
    print('%r ima opseg %.3f i povrsinu %.3f'%(t, t.opseg(), t.povrsina()))

print("-------------------------------------------------------------------------------------\n")

print("Zadatak 4.3\n")

'''
Napravi podklasu JednakokracniTrokut klase Trokut koja će u specijalnoj metodi __init__() koristiti__init__() od svoje nadklase. __init__() prima dva parametra koji predstavljaju duljinu baze i duljinukraka.
Na sličan način napravi podklasu JednakostranicniTrokut klase JednakokracniTrokut koji će uspecijalnoj metodi __init__() primati samo jednu stranicu.
'''

trokuti =[Trokut(3,4,5),JednakokracniTrokut(3,4),JednakostranicniTrokut(5)]
for t in trokuti:
    print(t)

print("-------------------------------------------------------------------------------------\n")