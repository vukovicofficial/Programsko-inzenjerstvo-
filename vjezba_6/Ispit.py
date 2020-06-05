import json
import sqlite3

# ZADATAK 6.1

'''
Stvori datoteku ispit.py
Postavi sljedeći kod na početak
'''

class Ispit(dict):

    def dodaj(self, student, kolegij, ocjena):
        if student not in self:
            self[student] = {}
        self[student][kolegij] = ocjena

    def izbrisi(self, student, kolegij):
        if kolegij in self[student]:
            self[student].pop(kolegij)

    def promijeni(self, student, kolegij, ocjena):
        self[student][kolegij] = ocjena

    '''
    Napravi metodu .spremi_datoteka() koja prima naziv datoteke datoteka i u njoj zapisuje podatke o ispitima na sljedeći način:
    '''
    def spremi_datoteka(self, naziv_datoteke):
        with open(naziv_datoteke, "w", encoding="utf8") as dat:
            for student, kolegiji_dict in self.items():
                for kolegiji, ocjena in kolegiji_dict.items():
                    dat.write("%s \t %s \t %s \n" % (student, kolegiji, str(ocjena)))


    '''
    Napravi statičnu medotu .ucitaj_datoteka() koja prima naziv datoteke datoteka iz koje pročita podatke, stvori objekt 
     od klase Ispiti i u njega pomoću metode.dodaj() ubaci podatke iz pročitane datoteke. Na kraju vrati taj objekt.
    '''

    @staticmethod
    def ucitaj_datoteku(naziv_datoteke):
        isp = Ispit()
        with open(naziv_datoteke, "r", encoding="utf8") as dat:
            for line in dat.readlines():
                info_string = line.split("\t")
                isp.dodaj(info_string[0].strip(), info_string[1].strip(), int(info_string[2].strip()))

        return isp

    '''
    U klasi Ispiti napravi metodu .spremi_json() koja prima naziv datoteke datoteka i u njoj zapisuje podatke o 
     ispitima pomoću metode .dump() modula json:
    Napravi statičnu metodu .ucitaj_json() koja prima naziv datoteke 
    datoteka iz koje pročita podatke, stvori objekt od klase Ispiti tako da prilikom inicijalizacije prenese se rezultat
    metode .load modula json i vrati taj objekt
    '''
    def spremi_json(self, naziv_datoteke):
        with open(naziv_datoteke, "w", encoding="utf8") as dat:
            json.dump(self, dat)


    @staticmethod
    def ucitaj_json(naziv_datoteke):


        with open(naziv_datoteke, "r", encoding="utf8") as dat:
           isp = Ispit(json.load(dat))
           return isp





