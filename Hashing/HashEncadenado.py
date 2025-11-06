import numpy as np
from Nodo import Nodo
from ListaEncadenada import ListaEncadenada

from sympy import isprime

class HashTable:
    __m:int
    __array: np.array
    __col:int

    def __init__(self,m, col):
        self.__col = col
        self.__m = isprime(m/col)
        self.__array = np.zeros(self.__m,dtype=object)
        
    #Metodos de Transformacion
    def myhashDivision(self, num):
        hash = num % self.__m
        return hash

    def myhashExtraccion(self, num):
        hash = (abs(num) % 100)%self.__m
        return hash
    
    def myhashPlegado(self, num):
        n = str(num)
        hash=0
        for i in range(0, len(n), 2):
             hash+= int(n[i] + n[i + 1])
        return hash % self.__m

    def myhashCuadrado(self, num):
        n = str(num)
        hash = []
        for i in range(0, len(n), 3):
            hash += [(n[i] + n[i + 1] + n[i + 2])]
        return hash[len(hash) // 2] % self.__m

    def myhashAlfanumerico(self, num):
        hash =0
        for i in range(len(num)):
            hash += int(ord(num[i]) * (pow(10, i + 1)))
        return hash
    
    #Metodos de insercion, busqueda y eliminacion
    def insertar(self, num):
        if self.__array[self.myhashDivision(num)] == None:
            self.__array[self.myhashDivision(num)] = ListaEncadenada()
            self.__array[self.myhashDivision(num)].insertar(num)
            return

        if self.__array[self.myhashDivision(num)].buscar(num):
                print("El numero ya existe")
                return
        else:
            self.__array[self.myhashDivision(num)].insertar(num)

    #isprime
    def isprime(self, num):
        while not isprime(num):
            num += 1
        return num
    
    def buscarClave(self, clave):
        pos = self.myhashDivision(clave)
        cantidad = self.__array[pos].buscarClave(clave)
        print(f"El numero de itentos del elemento {clave} es: {cantidad}")
            