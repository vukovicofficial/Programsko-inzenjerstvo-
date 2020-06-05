from pprint import pprint

class Kvadrat():

    '''
    Stvori datoteku mine.py Implementiraj klasu Kvadrat i u njoj metodu __init__().
    Prilikom inicijalizacije kvadrata postavljaju se privatni atributi __broj na preneseni broj, __otkriven na False i __oznaka na False.
    Implementiraj metodu otkrij() koja će otkriti kvadrat ako nije označen.
    Implementiraj metodu oznaci() koja će označiti kvadrat ako nije otkriven, ili skinuti oznaku ako je kvadrat već označen.
    Implementiraj metode kao svojstva jeMina(), jeBroj() i jePrazan() koje će vratiti True ili False ako je kvadrat mina, broj ili prazan.
    '''

    def __init__(self, broj = 0):
        self.__broj = broj
        self.__otkriven = False
        self.__oznaka = False

    def otkrij(self):
        if self.__otkriven == False:
            self.__otkriven = True

    def oznaci(self):
        if self.__oznaka == False:
            self.__oznaka = True
        else:
            self.__oznaka = False

    @property
    def jeMina(self):
        if self.__broj == -1:
            return True
        return False

    @property
    def jeBroj(self):
        if self.__broj > 0:
            return True
        return False

    @property
    def jePrazan(self):
        if self.__broj == 0:
            return True
        return False

    '''
    Implementiraj stringovnu reprezentaciju __str__() koja će vratiti: 
        točku '.' ako kvadrat nije otkriven 
        upitnik '?' ako je kvadrat označen 
        križić 'x' ako je kvadrat otkriven i sadrži minu 
        broj 'n' gdje je n broj ako je kvadrat otkriven i sadrži broj 
        razmak ' ' ako je kvadrat otkriven i ako je prazan
    '''

    def __str__(self):
        if self.__otkriven == False:
            return "."
        elif self.__oznaka == True:
            return "?"
        elif self.__otkriven == True and self.__broj == -1:
            return "x"
        elif self.__otkriven == True and self.__broj > 0:
            return str(self.__broj)
        elif self.__otkriven == True and self.__broj == 0:
            return " "


print('Zadatak 7.2\n')

brojevi = [-1,0,1,2]
for broj in brojevi:
    k = Kvadrat(broj)
    print(k.jeMina, k.jeBroj, k.jePrazan)

print("---------------------------------------------------------------------------------\n")

print('Zadatak 7.3\n')
kvadrati = [Kvadrat(broj) for broj in [-1, 0, 1, 2]]
print('   oz ot oz ot')
for k in kvadrati:
    rez = []
    rez.append(str(k))
    for counter in range(2):
        k.oznaci()
        rez.append(str(k))
        k.otkrij()
        rez.append(str(k))

    print('%s  %s  %s  %s  %s  ' % tuple(rez))




