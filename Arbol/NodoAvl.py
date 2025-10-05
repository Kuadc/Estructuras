class NodoAvl:
    __clave: int
    __iqz: None
    __der: None
    __h: int

    def __init__(self, dato=0):
        self.__clave = dato
        self.__izq = None
        self.__der = None
        self.__h = 0

    def getDato(self):
        return self.__clave
    def setDato(self, dato):
        self.__clave = dato
    def getIzq(self):
        return self.__izq
    def getDer(self):
        return self.__der
    def setIzq(self, izq):
        self.__izq = izq
    def setDer(self, der):
        self.__der = der

    def getH(self):
        return self.__h

    def setH(self, newH):
        self.__h = newH
