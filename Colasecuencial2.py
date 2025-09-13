from trabajo import paginas

import numpy as np

class cola:
    __cantidad: int
    __tope: int
    __pr:int
    __ul:int
    __arreglo: np.ndarray

    def __init__(self, max=0):
        self.__cantidad = 0
        self.__max = max
        self.__arreglo = np.empty(self.__max, dtype=paginas)
        self.__pr = 0
        self.__ul = 0
        
        
    #inserta por el ultimo lugar o cola.
    def insertar(self,x):
        if self.__cantidad < self.__max:
            self.__arreglo[self.__cantidad]=x
            print("--------Inserta trbaajo", self.__arreglo[self.__cantidad])
            self.__ul = (self.__ul+1) % self.__max
            self.__cantidad +=1
            return x
        else:
            return 0
            
        
    
    def vacia(self):
        return self.__cantidad == 0
    
    
    
    #suprime por el primer lugar
    def suprimir(self):
        if self.vacia:
            print("Pila esta vacia")
        else:
            x = self.__arreglo[self.__pr]
            self.__pr = (self.__pr+1)%self.__max
            print("primer elemento:",self.__arreglo[self.__pr].getPag())
            self.__cantidad -=1
            return x
    
    def mostrar(self):
        i=self.__pr
        j=0
        if self.vacia() == False:
            while j<self.__cantidad:
                print(f"Item:{self.__arreglo[i]}")
                i=(i+1)%self.__max
                j+=1
        
    
