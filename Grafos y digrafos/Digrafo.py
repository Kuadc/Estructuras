import numpy as np
#from ListaAdSec import Lista
from ListaAdEnc import Lista

from Pila import Pila

import math

from cola import ColaCircular

class Digrafo:
    __array:np.array
    __tiempo:int
    __tamaño: int

    def __init__(self, tamaño):
        self.__tiempo  = 0
        self.__tamaño = tamaño
        self.__array = np.empty(tamaño, dtype=object)
        for i in range(tamaño):
            self.__array[i] = Lista()

    def insertarSecuencial(self, v1, v2, arista=1):
        self.__array[v1].insertar(v2, arista)

    def insertarEncadenada(self, v1, v2, arista=0):
        self.__array[v1].insertar(v2, arista)

    def Adyacentes( self, v1):
        self.__array[v1].Adyacentes()
        
    def REA(self, v):
        d = np.full(5, math.inf)
        antesesor = np.full(self.__tamaño, -1)
        antesesor[v]=v
        d[v]=0
        unacola = ColaCircular(5)
        unacola.insertar(v)
        while not unacola.vacia():
            v = unacola.suprimir()
            aux = self.__array[v].getcabeza()
            while aux != None:
                if d[aux.getDato()]==np.inf:
                    d[aux.getDato()]=d[v]+1
                    antesesor[aux.getDato()]=v
                    unacola.insertar(aux.getDato())
                aux = aux.getSig()
        
        print(f"distancia de aristas-{d}-")
        print(f"{antesesor}\n\n")
        return antesesor
                
    def camino(self, origen,destino):
        antesesores= self.REA(origen)
        print(f"Camino de origen:{origen} a destino:{destino}")
        unapila = Pila(self.__tamaño)
        unapila.insertar(destino)
        
        if antesesores[destino] == -1:
            print("no hay camino")
        else:
            while origen != destino:
                    destino = antesesores[destino]
                    unapila.insertar(destino)
            unapila.mostrar()
                  
    def REP(self):
        d = np.zeros(self.__tamaño, int)
        f = np.zeros(self.__tamaño, int)
        self.__tiempo = 0
        for s in range(self.__tamaño):
            if d[s] == 0:
                self.Visita(s,d,f)
        print(f"{d}")

    def Visita(self, s,d,f):
        self.__tiempo+=1
        d[s] = self.__tiempo
        
        for u in self.__array[s].listaAdyacente():
            if d[u]==0:
                self.Visita(u, d, f)

        self.__tiempo+=1
        f[s]= self.__tiempo

    
    def conexo(self):
        antesesor = self.REA(self.__array[0].getcabeza().getDato())
        if np.any(antesesor):
            print("No es conexo")
        else:
            print("es conexo")
        
        
        
        
        
        
        
        
        
                
            
        
        
        
        
        