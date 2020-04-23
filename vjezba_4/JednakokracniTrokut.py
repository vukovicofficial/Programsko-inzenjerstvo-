from vjezba_4.Trokut import Trokut

# ZADATAK 4.3

'''
Napravi podklasu JednakokracniTrokut klase Trokut koja će u specijalnoj metodi __init__() koristiti__init__() od svoje nadklase. __init__() prima dva parametra koji predstavljaju duljinu baze i duljinukraka.
Na sličan način napravi podklasu JednakostranicniTrokut klase JednakokracniTrokut koji će uspecijalnoj metodi __init__() primati samo jednu stranicu.
'''

class JednakokracniTrokut(Trokut):

    def __init__(self, db, dk):
        Trokut.__init__(self, db, dk, dk)

#------------------------------------------------------------------------------------------------------------------------------------------