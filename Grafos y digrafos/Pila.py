import numpy as np

class Pila:
    __tope:object
    __cantidad:int
    __array: np.array
    def __init__(self, tope):
        self.__tope = tope
        self.__array = np.zeros(tope, dtype=object)
        self.__cantidad = 0
        
        
    def insertar(self, item):
        if self.__cantidad <self.__tope:
            self.__array[self.__cantidad]=item
            self.__cantidad+=1
        else:
            print("pila llena")
            
    def mostrar(self):
        i=self.__cantidad-1
        while i>=0:
            print(f"{self.__array[i]}",end=" ")
            i-=1
            
        
            