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
        d[v]=0
        unacola = ColaCircular(5)
        unacola.insertar(v)
        while not unacola.vacia():
            v = unacola.suprimir()
            print(f"vertice suprimido:{v}")
            aux = self.__array[v].getcabeza()
            while aux != None:
                if d[aux.getDato()]==np.inf:
                    d[aux.getDato()]=d[v]+1
                    unacola.insertar(aux.getDato())
                aux = aux.getSig()
        
        print(f"-{d}-")
        
    def REA2(self, v):
        d = np.full(5, math.inf)
        antesesor = np.zeros(self.__tamaño, int)
        antesesor[v]=v
        d[v]=0
        unacola = ColaCircular(5)
        unacola.insertar(v)
        while not unacola.vacia():
            v = unacola.suprimir()
            print(f"vertice suprimido:{v}")
            aux = self.__array[v].getcabeza()
            while aux != None:
                if d[aux.getDato()]==np.inf:
                    d[aux.getDato()]=d[v]+1
                    antesesor[aux.getDato()]=v
                    unacola.insertar(aux.getDato())
                aux = aux.getSig()
        
        print(f"-{d}-")
        print(f"{antesesor}\n\n")
        return antesesor
        
    def REACaminos(self, origen): 
        distancia = np.full(5, math.inf)
        visitado = np.zeros(self.__tamaño, dtype=bool)
        antesesor = np.zeros(self.__tamaño, int)
        unacola = ColaCircular(5)
        distancia[0]=0
        visitado[0]=True
        antesesor[0]=origen
        unacola.insertar(origen)
        while not unacola.vacia():
            v = unacola.suprimir()
            print(f"vertice suprimido:{v}")
            aux = self.__array[v].getcabeza()
            while aux != None:
                if visitado[aux.getDato()] == False:
                    visitado[aux.getDato()]=True
                    distancia[aux.getDato()]=distancia[v]+1
                    antesesor[aux.getDato()]=v

                    unacola.insertar(aux.getDato())
                aux = aux.getSig()
        
        print(f"{visitado}")
        print(f"{distancia}")
        print(f"{antesesor}")
        return antesesor

                
    def camino(self, origen,destino):
        antesesores = self.REA2(origen)
        unapila = Pila(self.__tamaño)
        unapila.insertar(destino)
        while origen != destino:
            destino = antesesores[destino]
            unapila.insertar(destino)
        unapila.mostrar()
            
                   
                    
    def REP(self, v):
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
        #for i in range(5):
        #print(f"-{d}-")
        
        
        
        
        
        
        
        
        
        
                
            
        
        
        
        
        