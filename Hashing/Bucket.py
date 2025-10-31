import numpy as np

class Bucket:
    __tamaño:int
    __cantidad:int
    __ul:int
    __array : np.array

    def __init__(self, c):
        self.__tamaño = c
        self.__ul = 0
        self.__cantidad = 0
        self.__array = np.zeros(c, dtype=object)


    def insertar(self, item):
        #la lista por contenido se inserta ordenado
        #agrego cuando la lista esta vacia
        if self.__cantidad == 0:
            print("inserta al principio si esta vacia")
            self.__array[self.__ul] = item
            self.__cantidad += 1
            return

        if self.__cantidad < self.__tamaño:
            print("inserta en posicion determinada")
            pos = self.buscar(item)
            ultimo = self.__ul
            while ultimo >= pos:
                self.__arreglo[ultimo + 1] = self.__arreglo[ultimo]
                ultimo -= 1
            self.__arreglo[pos] = item
            self.__cantidad += 1
            self.__ul += 1
            return True
        else:
            return False

    def buscar(self, elemento):
        #retorna la posicion- implementar busqueda binaria
        band = False
        max= self.__ul
        min = 0
        while min <= max and not band:
            medio = (min +max) //2
            if elemento > self.__arreglo[medio]:
                min = medio+1
            elif elemento < self.__arreglo[medio]:
                 max=medio -1
            else:
                band = True
        return band

