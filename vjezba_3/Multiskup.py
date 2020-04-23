from itertools import groupby

class MultiSkup():
    # Zadatak 3.1 - MultiSkup

    '''
    Stvori datoteku multiskup.pyNapravi klasu MultiSkup koja će za razliku od klasičnog skupa imati više istih elemenata.
    Na primjer{1,1,2,2,2,3,3,4} je multiskup od 8 elemenata gdje se 1 pojavljuje 2 puta, 2 se pojavljuje 3 puta, 3 se pojavljuje2 puta, a 4 jedan put.
    Kako bi znali koliko puta se određeni element javlja u multiskupu, koristit ćemo rječnikčiji će ključevi biti elementi, a vrijednosti broj pojavljivanja elemenata.
    Napravi __init__() metodu multiskupa koja primita kolekciju elemenata (None ako se ne prenese).
    Napravi specijalnu medotu __str__() koja će ispisati stringovnu reprezentaciju skupa oblika{{element*broj_pojavljivanja, element*broj_pojavljivanja, ...}}.
    Na primjer, za multiskup {1,1,2,2,2,3,3,4}stringovna reprezentacija će vratiti {{1*2, 2*3, 3*2, 4*1}}
    '''

    def __init__(self, multiSkup = None):
        self.__multiSkup = {}

        if isinstance(multiSkup, MultiSkup):
            self.__multiSkup = multiSkup
        else:
            for key, group in groupby(multiSkup):
                self.__multiSkup[key] = len(list(group))

    def __str__(self):
        output = []
        for key, value in self.__multiSkup.items():
            output.append("%r*%r" % (key, value))
        return "{{" + ", ".join(output) + "}}"

    #-------------------------------------------------------------------------------------

    #Zadatak 3.2 - MultiSkup

    '''
    Napravi specijalnu metodu __iter__() koja će služiti za iteraciju multiskupa.
    Napravi specijalnu metodu __repr__() koja će vratiti reprezentaciju skupa. 
    Prilikom izrade reprezentacijemultiskupa parametre predstavi kao listu
    '''

    def __iter__(self):
        array = []

        for key, value in self.__multiSkup.items():
            for i in range(value):
                array.append(key)

        return iter(array)


    def __repr__(self):
        output = []
        for key, value in self.__multiSkup.items():
            output.append("%r: %r" % (key, value))
        return "Multiskup([" + ", ".join(output) + "])"


    #-------------------------------------------------------------------------------------


    #Zadatak 3.3 - MultiSkup

    '''
    Napravi metodu add() koja će dodavati element određeni broj puta. Ako broj ponavljanja nije prenesen ondaje on 1.
    Napravi metodu remove() koja će brisati element određeni broj puta. Ako broj ponavljanja nije prenesenonda je on 1.
    '''

    def add(self, key):
        if(key not in self.__multiSkup.keys()):
            self.__multiSkup[key] = 1
        else:
            self.__multiSkup[key] += 1

    def add(self, key, value = 1):
        if(key not in self.__multiSkup.keys()):
            raise ValueError('Ključ ne postoji.')
        else:
            self.__multiSkup[key] += value

    def remove(self, key, value = 1):
        if (key not in self.__multiSkup.keys()):
            raise ValueError('Ključ ne postoji.')
        else:
            self.__multiSkup[key] -= value

    # -------------------------------------------------------------------------------------


