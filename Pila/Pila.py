import numpy as np

class Pila:
    __tope:int
    __cant:int
    __arreglo: np.array

    def __init__(self, cantidad=0):
        self.__tope = 0
        self.__cant = cantidad
        self.__arreglo = np.zeros(self.__cant, dtype = int)

    def insertar(self, x):
        if self.__tope < self.__cant:
            self.__arreglo[self.__tope] = x
            self.__tope+=1
            return x
        else:
            print("lista llena")
            return 0

    def suprimir(self):
        if self.vacia():
            print("pila vacia")
        else:
            x =self.__arreglo[self.__tope-1]
            self.__tope-=1
            return x

    def mostrar(self):
        i=self.__tope-1
        while i >=0 :
            print(f"{self.__arreglo[i]}")
            i-=1

    def vacia(self):
        return self.__cant == 0

if __name__ == "__main__":

    pi = Pila(5)
    pi.insertar(5)
    pi.insertar(4)
    pi.insertar(3)
    pi.insertar(2)
    pi.insertar(1)

    pi.mostrar()

    pi.suprimir()
    pi.mostrar()