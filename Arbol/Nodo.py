class NodoArbol:
    __clave: int
    __iqz: None
    __der: None

    def __init__(self, dato=0):
        self.__clave = dato
        self.__izq = None
        self.__der = None

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
