'''
Može se lakše uraditi preko ugrađene biblioteke 'fractions'
'''


'''
Stvori datoteku razlomak.py
Napravi klasu Razlomak koja će imati dva atributa brojnik i nazivnik.
Brojnik i nazivnik se šalju kao argumenti tijekom inicijalizacije klase
Napravi svojstva za čitanje i pisanje brojnika i nazivnika.
Napravi metodu skrati() koja će skratiti razlomak, na primjer. razlomak 3/12 se može skratiti na 1/4.
'''


class Razlomak(object):

    def __init__(self, brojnik, nazivnik):
        self._brojnik = int(brojnik)
        self._nazivnik = int(nazivnik)

    # Getters
    @property
    def brojnik(self):
        return self._brojnik

    @property
    def nazivnik(self):
        return self._nazivnik
    #---------------------------

    # Setters
    @brojnik.setter
    def brojnik(self, brojnikVrijednost):
        self._brojnik = brojnikVrijednost

    @nazivnik.setter
    def nazivnik(self, nazivnikVrijednost):
        self._nazivnik = nazivnikVrijednost
    # ---------------------------

    #Metoda za skraćivanje razomaka ako je to moguće
    @property
    def skrati(self):
        najmanjiDjeljitelj = None

        if(self.brojnik <= self.nazivnik):
            manjiBroj = self.brojnik
        else:
            manjiBroj = self.nazivnik

        for djeljitelj in range(2, int(manjiBroj + 1)):
            if(self.brojnik % djeljitelj == 0 and self.nazivnik % djeljitelj == 0):
                najmanjiDjeljitelj = djeljitelj

        if(najmanjiDjeljitelj == None):
            print("Razlomak se ne može skratiti.")
        else:
            self.nazivnik //= najmanjiDjeljitelj
            self.brojnik //= najmanjiDjeljitelj
            print("Razlomak se može skratiti sa brojem", najmanjiDjeljitelj, "te razlomak sada izgleda:", repr(self))

    def __repr__(self):
        return "Razlomak(" + repr(self.brojnik) + ", " + repr(self.nazivnik) + ")"

    #-------------------------------------------------------------------------------------------------------------------

    #Vježba 1.1
    '''
    U klasi razlomak napravi specijalnu metodu __str__() koja će služiti za ispis razlomka u oblikubrojnik|nazivnik i specijalnu metodu __repr__() za reprezentaciju razlomka.
    Napravi specijalne metode za operacije usporedbe razlomaka.
    '''

    def __str__(self):
        return str(self.brojnik) + "|" + str(self.nazivnik)

    #__repr__ metoda je definirana ranije

    def __eq__(self, other):
        return (self.brojnik / self.nazivnik) == (other.brojnik / other.nazivnik)

    def __ge__(self, other):
        return (self.brojnik / self.nazivnik) >= (other.brojnik / other.nazivnik)

    def __lt__(self, other):
        return (self.brojnik / self.nazivnik) < (other.brojnik / other.nazivnik)

    # -------------------------------------------------------------------------------------------------------------------

    # Vježba 1.2
    '''
     klasi razlomak napravi specijalnu metode za zbrajanje, oduzimanje, množenje i dijeljenje razlomaka.
    '''

    def __add__(self, other):
        brojnik = (self.brojnik * other.nazivnik) + (other.brojnik * self.nazivnik)
        nazivnik = self.nazivnik * other.nazivnik

        return repr(Razlomak(brojnik, nazivnik))

    def __sub__(self, other):
        brojnik = (self.brojnik * other.nazivnik) - (other.brojnik * self.nazivnik)
        nazivnik = self.nazivnik * other.nazivnik

        return repr(Razlomak(brojnik, nazivnik))

    def __mul__(self, other):
        brojnik = self.brojnik * other.brojnik
        nazivnik = self.nazivnik * other.nazivnik

        return repr(Razlomak(brojnik, nazivnik))

    def __truediv__(self, other):
        brojnik = self.brojnik / other.brojnik
        nazivnik = self.nazivnik / other.nazivnik

        return repr(Razlomak(brojnik, nazivnik))

    # -------------------------------------------------------------------------------------------------------------------