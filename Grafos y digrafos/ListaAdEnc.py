import numpy as np
from Nodo import Nodo

class Lista:
    __cabeza:None
    __pr:int
    __ul:int

    def __init__(self):
        self.__cabeza = None
        self.__ul=None

    def insertar(self, v2, arista):
        unNodo = Nodo(v2, arista)
        if self.__cabeza == None:
            self.__cabeza = unNodo
        else:
            self.__ul.setSig(unNodo)
        self.__ul = unNodo
            

    def Adyacentes(self):
        aux = self.__cabeza
        while aux != None:
            print(f"Nodo Adyacente:{aux.getDato()}")
            aux = aux.getSig()

    def listaAdyacente(self):
        lista=[]
        aux = self.__cabeza
        i=0
        while aux != None:
            lista = lista+[aux.getDato()]
            aux = aux.getSig()
        return lista
        
        
    def suprimir(self):
        x = 0
        if self.vacia():
            print("La cola esta vacia")
        else:
            x = self.__pr.getDato()
            self.__pr = self.__pr.getSig()
            self.__cantidad -= 1
            if self.__pr == None:
                self.__ul = None
            return x
        

    def getcabeza(self):
        return self.__cabeza
