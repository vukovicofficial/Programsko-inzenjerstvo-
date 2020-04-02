
from vjezba_2.Stvar import Stvar
from vjezba_2.Razlomak import Razlomak

'''Zadatak 2.1'''
print('\n*** Zadatak 2.1 ***')

s1 = Stvar()
s2 = Stvar()
s3 = s2

print(Stvar.brojStvari)
del(s2)
print(Stvar.brojStvari)
del(s3)
print(Stvar.brojStvari)
del(s1)
print(Stvar.brojStvari)

#-----------------------------------------------------

'''Zadatak 2.2'''

print('\n*** Zadatak 2.2 ***')
r1 =Razlomak(314,100)
r2 =Razlomak.inverz(r1)
print(r1,r2,r1)

#----------------------------------

'''Zadatak 2.3'''
print('\n*** Zadatak 2.3 ***')

r1 = Razlomak.stvori(3.14)
print(r1)
r2 = Razlomak.stvori(0.006021)
print(r2)
r3 = Razlomak.stvori(-75.204)
print(r3)
