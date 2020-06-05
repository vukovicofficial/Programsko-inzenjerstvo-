class Polje():
    '''
    Stvori datoteku 2048.py Implementiraj klasu Polje i u njoj metodu __init__().
    Prilikom inicijalizacije polja postavlja se privatni atributi __broj na preneseni broj.
    Ako se nije prenio broj, onda je on 0. Implementiraj "get" i "set" svojstvo broj koje će vratiti i postaviti broj polja.
    Implementiraj "get" svojstva jeBroj, jePrazno koje će vratiti True ili False ako je polje broj ili prazno.
    '''

    def __init__(self, broj = 0):
        self.__broj = int(broj)

    @property
    def broj(self):
        return self.__broj

    @broj.setter
    def broj(self, broj):
        self.__broj = broj

    @property
    def jeBroj(self):
        if self.__broj > 1:
            return True
        return False

    @property
    def jePrazno(self):
        if self.__broj > 1:
            return False
        return True


    '''
    Implementiraj stringovnu reprezentaciju __str__() koja će vratiti: broj 'n' ako je broj polja n > 0 točku '.' ako je broj polja = 0 
    Implementiraj reprezentaciju __repr__() koja će vratiti string kojim se stvara objekt od te klase. 
    Implementiraj specilajnu metodu __eq__() koja prima parametar other. 
    Ova metoda će vratiti True ako je: other instanca od Polje i ako je svojstvo broj od other jednako svojstvu broj 
     od self. other cijeli broj (instanca od int) i ako je vrijednost od other jednako svojstvu broj od self. 
    U suprotnom će vratiti False 
    '''

    def __str__(self):
        if self.__broj > 0:
            return "{}".format(self.broj)
        else:
            return "."

    # Vraća string koja predstavlja objekt klase Polje
    def __repr__(self):
        return "Polje({})".format(self.broj)

    def __eq__(self, other):
        if isinstance(other, Polje) and other.broj == self.broj:
            return True
        elif isinstance(other, int) and other == self.broj:
            return True

        return False


print('Zadatak 7.2\n')
polja = [Polje(0)] + [Polje(2**broj) for broj in range(1, 12)]
for p in polja:
    print(p.broj, p.jeBroj, p.jePrazno)

print('--------------------------------------------------------------\n')

print('Zadatak 7.3\n')
polja = [Polje(0)] + [Polje(2**broj) for broj in range(1, 12)]
for p in polja:
    print(repr(str(p)), repr(p))
print()

polja = [Polje(0)] + [Polje(2**broj) for broj in range(1, 3)]
elementi = [2, Polje(2), 3, Polje(3)]
for el in elementi:
    for p in polja:
        print('%r %r %s' % (el, p, el == p))


