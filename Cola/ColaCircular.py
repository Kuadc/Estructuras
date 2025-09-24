import numpy as np


class ColaCircular:
    __pr:int
    __ul:int
    __max:int
    __arreglo: np.array

    def __init__(self, max=0):
        self.__max = max
        self.__cant = 0
        self.__ul = 0
        self.__pr = 0
        self.__arreglo = np.zeros(max, dtype=int)


    def insertar(self,x):
        if self.__cant < self.__max:
            self.__arreglo[self.__ul] = x
            self.__ul = (self.__ul+1)%self.__max
            self.__cant +=1
        else:
            print("cola llena")

    def suprimir(self):
        if self.vacia():
            print("cola vacia")
        else:
            x = self.__arreglo[self.__pr]
            self.__pr = (self.__pr+1)%self.__max
            self.__cant-=1
            return x

    def mostrar(self):
        i=0
        j=self.__pr
        while i<self.__cant:
            print(f"{self.__arreglo[j]}")
            j = (j+1)%self.__max
            i+=1

    def vacia(self):
        return self.__cant == 0

if __name__ == "__main__":
    pi = ColaCircular(5)
    pi.insertar(5)
    pi.insertar(4)
    pi.insertar(3)
    pi.insertar(2)
    pi.insertar(1)

    pi.mostrar()
    print("------------------------- 1")
    pi.suprimir()
    pi.mostrar()

    print("------------------------- 2")
    pi.suprimir()
    pi.mostrar()
    pi.insertar(5)
    pi.insertar(4)
    print("-------------------------3")
    pi.mostrar()