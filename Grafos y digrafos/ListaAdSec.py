import numpy as np

class Lista:
    __tamaño:int
    __cantidad:int
    __ul:int
    __array : np.array

    def __init__(self, tam):
        self.__tamaño = tam
        self.__cantidad = 0
        self.__ul = 0
        self.__array = np.zeros(tam, dtype=object)


    def insertar(self, v2, arista):
        if v2 <= self.__tamaño:
            self.__array[v2] = arista
            self.__cantidad+=1

    def Adyacentes(self):
        for i in range(self.__tamaño):
            if self.__array[i] != 0:
                print(f"Nodo: {i}")

    def ady(self):
        



