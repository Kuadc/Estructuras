import numpy as np
from celda import celda

class ListaCursor:
        __cantidad: int
        __tope: int
        __arreglo: np.ndarray
        __libre:int
        __cab:int

        def __init__(self, cantidad=0):
            self.__cantidad = cantidad
            self.__tope = -1
            self.__arreglo = np.empty(self.__cantidad, dtype=celda)
            self.__libre = 0
            self.__cab =0

        def vacia(self):
            return self.__libre == 0
                

        def insertar(self, x, pos):
            if self.vacia() and pos == 1:
                self.__tope += 1
                unacelda = celda(x)
                self.__arreglo[pos-1] = unacelda
                self.__libre +=1
                self.__cab = 0
            else:
                pos-=1
                if 1<= pos <=self.__libre+1:
                    unacelda = celda(x)
                    aux = self.__cab
                    i=0
                    while i<pos:
                        
                        aux = self.__arreglo[i].getSig()
                        i+=1
                    
                    unacelda.setSig(aux)
                    self.__arreglo[self.__libre] = unacelda    
                    self.__arreglo[pos-1].setSig(self.__libre)
                
                    self.__libre+=1
                else:
                    print("posicion fuera de rango o lista llena")
                    
    

        def suprimir(self):
            
            pass

        def mostrar(self):
            aux = self.__cab
            if self.vacia()==False:   
                while(aux != -1):
                    print("apunta fisicamente:", aux)
                    print(f"Dato:{self.__arreglo[aux].getDato()}\n")
                    aux = self.__arreglo[aux].getSig()
                    
                    
                    
                

if __name__ == "__main__":
        cursor = ListaCursor(5)
        cursor.insertar(20, 1)
        cursor.insertar(30, 2)
        cursor.insertar(90, 3)
        cursor.insertar(43, 2)
        
        cursor.mostrar()
        