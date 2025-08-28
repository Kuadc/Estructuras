import numpy as np
from peldaño import peldaño

class Pila:
    __cantidad: int
    __tope: int
    __arreglo: np.ndarray

    def __init__(self, cantidad=0):
        self.__cantidad = cantidad
        self.__tope = -1
        self.__arreglo = np.empty(self.__cantidad, dtype=peldaño)

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

    def mostrar(self, cadena):
        i = self.__tope
        if self.vacia()==False:   
            while(i>=0):
                print(f"{cadena}:{self.__arreglo[i]}")
                i-=1
                
                
    def subirpeldaño(self):
        peldaños = self.__arreglo[0].getPeldaños()
        while peldaños >0:
            if peldaños >=2:
                self.__arreglo[0].sumarCadena("2")
                peldaños-=2
            else:
                self.__arreglo[0].sumarCadena("1")
                peldaños-=1
            

if __name__ == "__main__":
    unapila = Pila(1)
    unpeldaño = peldaño(10,"")
    unapila.insertar(unpeldaño)
    unapila.subirpeldaño()
    unapila.mostrar("solucion de escalones")
    
    
    