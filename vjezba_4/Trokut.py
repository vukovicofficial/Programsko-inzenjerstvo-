from math import sqrt

# ZADATAK 4.1

'''
Zadatak 4.1 - TrokutStvori datoteku trokut.py
Napravi klasu Trokut i specijalnu metodu __init__() koja će primiti stranice trokuta a, b, c i spremiti ih uprivatni atribut __stranice.
Pri tome će se provjeravati jesu li sve stranice >= 0 i da li zadovoljavaju uvjettrokuta (zbroj dviju stranica je veći od treće stranice).
U jednom i u drugom slučaju podignut će se iznimka sporukom "Nije Trokut".
Napravi stringovnu reprezentaciju __str__() koja će za trokut sa stranicama 3,4,5 vratiti string "trokut 3 4 5".
Napravi reprezentaciju __repr__() koja će za trokut sa stranicama 3,4,5 vratiti string "Trokut(3,4,5)"
'''


class Trokut():

    def __init__(self, a, b, c):
        if (a < 0 or b < 0 or c < 0) or (a + b <= c) or (c + b <= a) or (a + c <= b):
            raise ValueError("Nije Trokut")
        else:
            self.__stranice = (a, b, c)

    def __str__(self):
        return "trokut %i, %i, %i" % (self.__stranice[0], self.__stranice[1], self.__stranice[2])

    def __repr__(self):
        return "Trokut (%i, %i, %i)" % (self.__stranice[0], self.__stranice[1], self.__stranice[2])

    #---------------------------------------------------------------------------------------------------------------------------------------

    # ZADATAK 4.2

    '''
    Napravi metodu opseg() koja će vratiti opseg trokuta.
    Napravi metodu povrsina() koja će vratiti površinu trokuta po Heronovoj formuli P=(s−a)(s−b)(s−c)√gdje je s polupseg.
    '''

    def opseg(self):
        return (self.__stranice[0] + self.__stranice[1] + self.__stranice[2])

    def povrsina(self):
        s = self.opseg() / 2
        return sqrt( (s - self.__stranice[0])*(s - self.__stranice[1])*(s - self.__stranice[2]) )

    # ---------------------------------------------------------------------------------------------------------------------------------------