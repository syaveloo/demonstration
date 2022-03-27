class Tarif:
    def __init__(self):
        """ docstring """
        self.__pocket = (100.00, 50.00, 10.00)
        self.__cost = 177.46
        self.__add = (2.7, 3.9, 14.4)

    def getpocket(self):
        return self.__pocket

    def getadd(self):
        return self._add

    def getcost(self):
        return self.__cost


class Main(Tarif):
    def __init__(self, spent):
        """ docstring """
        super(Main, self).__init__()
        pocket = super(Main, self).getpocket()
        plata = super(Main, self).getpocket()
        self.sum = super(Main, self).getcost()

        def addit():
            """ additional payment """
            for usr, trf in zip(spent, pocket):
                x = float(usr)-trf
                yield x if x >= 0 else 0

        def plussum():
            "additpayment"
            for a, b in zip(additional, plata):
                self.sum += a*b

        additional = addit()
        plussum()

        print(self.sum)


if __name__ == "__main__":
    Main(input("sep=<space> |").split())
