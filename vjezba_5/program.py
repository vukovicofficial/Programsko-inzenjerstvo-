from vjezba_5.likovi import *
from vjezba_5.funkcije import *

# Zadatak 5.3

'''
U istom direktoriju gdje su moduli likovi i funkcije stvori datoteku program.py i u njemu importiraj module likovi i 
 modul funkcije.
Stvori objekt k1 od klase Kruznica s radijusom 3. 
Stvori objekt k2 od klase Kvadrat sa stranicom 5.
'''

k1 = Kruznica(3)
k2 = Kvadrat(5)
print(k1,'opsega', opseg(k1),'povrsine', povrsina(k1))
print(k2,'opsega', opseg(k2),'povrsine', povrsina(k2))