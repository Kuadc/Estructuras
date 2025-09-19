import numpy as np

class Pila:
    __cantidad: int
    __tope: int
    __arreglo: np.ndarray

    def __init__(self, cantidad=0):
        self.__cantidad = cantidad
        self.__tope = -1
        self.__arreglo = np.zeros(self.__cantidad, dtype=int)

    def vacia(self):
        return self.__tope == -1
            

    def insertar(self, x):
        if self.__tope < self.__cantidad - 1:
            self.__tope += 1
            self.__arreglo[self.__tope] = x
            return x
        else:
            return 0
        

    def suprimir(self):
        x = 0
        if self.vacia():
            print("Pila vacia")
            return 0
        else:
            x = self.__arreglo[self.__tope]
            self.__tope -=1
            return x

    def mostrar(self,cadena=""):
        i = self.__tope
        if self.vacia()==False:
            print(f"{cadena}")
            while(i>=0):
                print(f"{self.__arreglo[i]}")
                i-=1
        else: print(f"{cadena} Vacia")
                
    def conversor(self,num):
        while num >=2:
            resto = num % 2
            self.insertar(resto)
            num = num//2
        self.insertar(num)

if __name__ == "__main__":
    unapila = Pila(10)
    otrapila = unapila
    unapila.conversor(8)
    unapila.mostrar()

    # IMPLEMENTACION TERMINADA