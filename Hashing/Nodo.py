class Nodo:
    __sig: None
    __dato: object

    def __init__(self, dato):
        self.__dato = dato
        self.__sig = None

    def setSig(self, sig):
        self.__sig = sig

    def cargarsig(self, nodo):
        self.__sig = nodo

    def getSig(self):
        return self.__sig

    def getDato(self):
        return self.__dato
