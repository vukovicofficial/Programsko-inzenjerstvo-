from vjezba_5.likovi import *
from math import pi

# Zadatak 5.2

'''
U istom direktoriju gdje je i likovi.py stvori modul funkcije.py i u njemu importiraj modul likovi imodul math (iz 
 modula mathće se koristiti varijabla pi za izračun opsega i površine kružnice).
Napravi funkcije opseg() i povrsina() koje primaju za parametar lik i ovisno o tome koja je vrsta likaizračunava opseg 
 odnosno površinu. (za provjeru je li vrijednost ili varijabla instanca neke klase koristiisinstance()).
Napravi if uvjet koji će izvršavati donji test ako se trenutni modul pokrene.
'''

def opseg(lik):
    if isinstance(lik, Kruznica) == True:
        return 2 * lik.radijus * pi
    elif isinstance(lik, Kvadrat) == True:
        return 4 * lik.duljina_stranice

def povrsina(lik):
    if isinstance(lik, Kruznica) == True:
        return (lik.radijus * lik.radijus) * pi
    elif isinstance(lik, Kvadrat) == True:
        return lik.duljina_stranice * lik.duljina_stranice

if __name__ == "__main__":
    print(opseg.__name__)
    print(povrsina.__name__)