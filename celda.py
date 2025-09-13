class celda:
    __dato:int
    __sig:int
    
    def __init__(self, dato=0):
        self.__dato = dato
        self.__sig = -1
        
    def getDato(self):
        return self.__dato
    
    def getSig(self):
        return self.__sig
    
    def setSig(self, sig):
        self.__sig = sig
        