# Zadatak (5.1)

'''
Stvori modul likovi.pyNapravi klase Kruznica i Kvadrat.
Inicijalizator od Kruznica prima radijus kružnice, a inicijalizator odKvadrat prima duljinu stranice.
Napravi stringovnu reprezentaciju __str__() klasa Kruznica i Kvadrat koja će za kružnicu vratiti stringoblika "kruznica
 radijusa r", a za kvadrat "kvadrat stranice a", gdje će se iznos radijusa i stranice zaokružiti nadvije decimale.
Napravi if uvjet koji će izvršavati donji test ako se trenutni modul pokrene.
'''


class Kruznica():

    def __init__(self, radijus):
        self.__radijus = radijus

    @property
    def radijus(self):
        return self.__radijus

    @radijus.setter
    def radijus(self, radijus):
        self.radijus = radijus

    def __str__(self):
        return "kruznica radijusa %.3f" % (self.__radijus)

class Kvadrat():
    def __init__(self, duljinaStranice):
        self.__duljina_stranice = duljinaStranice

    @property
    def duljina_stranice(self):
        return self.__duljina_stranice

    @duljina_stranice.setter
    def kvadrat(self, duljina_stranice):
        self.__duljina_stranice = duljina_stranice

    def __str__(self):
        return "kvadrat stranice %.3f" % (self.__duljina_stranice)

if __name__ == "__main__":
    kruznica = Kruznica(3)
    kvadrat = Kvadrat(4.5)
    print(kruznica)
    print(kvadrat)

