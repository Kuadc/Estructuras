class Nodo:
    __sig: None
    __vertice: object
    __arista:object


    def __init__(self, vertice, arista):
        self.__vertice = vertice
        self.__arista = arista
        self.__sig = None

    def setSig(self, sig):
        self.__sig = sig

    def getSig(self):
        return self.__sig

    def getDato(self):
        return self.__vertice
