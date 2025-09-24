import numpy as np

class ColaSecuencial:
    __pr:int
    __ul:int
    __max:int
    __arreglo: np.array

    def __init__(self, cantidad=0):
        self.__max = cantidad
        self.__ul = -1
        self.__pr = 0
        self.__arreglo = np.zeros(cantidad, dtype=int)

    def insertar(self,x):
       if self.__ul <self.__max:
           self.__arreglo[self.__ul+1] = x
           self.__ul+=1
       else:
           print("cola llena")

    def suprimir(self):
        if self.vacia():
            print("cola vacia")
        else:
            x = self.__arreglo[self.__pr]
            i=0
            self.__ul-=1
            while i<self.__ul+1:
                self.__arreglo[i] = self.__arreglo[i+1]
                i+=1
            return x

    def mostrar(self):
        i=0
        while i<self.__ul+1:
            print(f"{self.__arreglo[i]}")
            i+=1

    def vacia(self):
        return self.__ul == -1

if __name__ == "__main__":
    pi = ColaSecuencial(5)
    pi.insertar(5)
    pi.insertar(4)
    pi.insertar(3)
    pi.insertar(2)
    pi.insertar(1)

    pi.mostrar()
    print("-------------------------")
    pi.suprimir()
    pi.mostrar()
