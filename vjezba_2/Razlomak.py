class Razlomak(object):
    '''Klasa razlomak'''
    def __init__(self, brojnik, nazivnik =1):
        if nazivnik == 0:
            raiseException('Nazivnik ne moze biti 0')

        self._brojnik = brojnik
        self._nazivnik = nazivnik

    def __str__(self):
        return'%d|%d'%(self._brojnik, self._nazivnik)

    def inverz(self):
        return Razlomak(self._nazivnik, self._brojnik)

    @staticmethod
    def numOfDecimalPlaces(num):
        stringOfNum = str(num)
        if not '.' in stringOfNum:
            return 0
        return len(stringOfNum) - stringOfNum.index('.') - 1

    @staticmethod
    def stvori(num:float):
        numberOfDecimalPlaces = Razlomak.numOfDecimalPlaces(num)

        number = "1"
        for i in range(numberOfDecimalPlaces):
            number += "0"

        return Razlomak(num * int(number), int(number))






