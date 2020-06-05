class Polje():

    '''
    Stvori datoteku slagalica.py Implementiraj klasu Polje i u njoj metodu __init__().
    Prilikom inicijalizacije polja postavlja se privatni atributi __broj na preneseni broj.
    Ako se nije prenio broj, onda je on 0 Implementiraj metodu vratiBroj() koja će vratiti broj polja.
    Implementiraj metode kao svojstva jeBroj() i jePrazno() koje će vratiti True ili False ako je polje broj ili prazno.
    '''

    def __init__(self, broj = 0):
        self.__broj = broj

    def vratiBroj(self):
        return self.__broj

    @property
    def jeBroj(self):
        if self.__broj > 0:
            return True
        return False

    @property
    def jePrazno(self):
        if self.__broj <= 0:
            return True
        return False

    '''
    Implementiraj stringovnu reprezentaciju __str__() koja će vratiti: 
        broj 'n' ako je broj polja n > 0 
        razmak ' ' ako je broj polja = 0 
    Implementiraj reprezentaciju __Repr__() koja će vratiti string kojim se stvara objekt od te klase
    '''

    def __str__(self):
        broj = self.vratiBroj()
        if broj > 0:
            return str(broj)
        elif broj == 0:
            return " "

    def __repr__(self):
        return "Polje({})".format(self.vratiBroj())


print('Zadatak 7.2\n')
brojevi = list(range(9))
for broj in brojevi:
    p = Polje(broj)
    print(p.vratiBroj(), p.jeBroj, p.jePrazno)

print("------------------------------------------------------------\n")



print('Zadatak 7.3\n')
polja = [Polje(broj) for broj in range(9)]
for p in polja:
    print(repr(str(p)), repr(p))



