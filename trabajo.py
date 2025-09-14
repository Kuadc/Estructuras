class paginas:
    __pag:int
    __temp:int

    def __init__(self, pag, reloj):
        self.__pag = pag
        self.__temp = reloj

    def getPag(self):
        return self.__pag

    def setPag(self):
        self.__pag-=30

    def getTemp(self):
        return self.__temp
