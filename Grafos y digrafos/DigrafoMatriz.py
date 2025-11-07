import numpy as np
#from ListaAdSec import Lista
from ListaAdEnc import Lista

from Pila import Pila

import math

from cola import ColaCircular

class Digrafo:
    __array:np.array
    __tamaño: int

    def __init__(self, tamaño):
        self.__tamaño = tamaño
        self.__array = np.zeros((tamaño,tamaño), dtype=object)

    def insertarSecuencial(self, v1, v2, arista=1):
        self.__array[v1][v2]=arista


    def mostrar(self):
        print(self.__array)

    def adyacentes(self, v):
        lista=[]
        for i in range(self.__tamaño):
            if self.__array[v][i] != 0:
                lista+=[i]
        print(lista)
        return lista

    def gradoSalida(self,v):
        grado = 0
        for i in (self.__array[v]):
            if i !=0:
                grado+=1
        return grado
    
    def gradoEntrada(self, v):
        grado = 0
        for i in range(self.__tamaño):
            for j in range(self.__tamaño):
                if self.__array[i][j] == v:
                    grado+=1

        return grado
    
    def pozo(self, v):

        if self.gradoEntrada(v) > 0 and self.gradoSalida(v) == 0:
            print("El vertice es pozo")
        else:
            print("no es nodo pozo")
    
    def caminos(self, origen, destino):
        d, a = self.REA(origen)

        print(f"distancias:{d}")
        print(f"antesesores:{a}")
        if a[destino] == -1:
            print("camino no encontrado")
        else:
            pi = Pila(self.__tamaño)
            pi.insertar(destino)
            while origen!= destino:
                destino = a[destino]
                pi.insertar(destino)
            pi.recorrer()
            




    def REA(self, v):
        d = np.full(self.__tamaño, np.inf)
        a = np.full(self.__tamaño, -1)
        d[v]=0
        a[v]=v

        cola =ColaCircular(self.__tamaño)
        cola.insertar(v)
        while not cola.vacia():
            v = cola.suprimir()
            for elem in(self.adyacentes(v)):
                print(elem)
                if d[elem] == np.inf:
                    d[elem] = d[v] + 1
                    a[elem] = v
                    cola.insertar(elem)

        return d, a
    

if __name__ == "__main__":
    grafo = Digrafo(5)
    grafo.insertarSecuencial(0,1)
    grafo.insertarSecuencial(0,4)

    grafo.insertarSecuencial(1,3)
    
    grafo.insertarSecuencial(2,4)

    grafo.insertarSecuencial(3,2)

    grafo.insertarSecuencial(4,1)

    grafo.mostrar()
    
    grafo.pozo(0)
    
    #grafo.adyacentes(0)

    grafo.caminos(0,3         )


    
 

    