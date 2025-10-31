import numpy as np
from Nodo import Nodo
from ListaEncadenada import ListaEncadenada

class HashTable:
    __m:int
    __array: np.array

    def __init__(self,m):
        self.__array = np.zeros(m,dtype=object)
        self.__m = m


    #Metodos de Transformacion
    def myhashDivision(self, num):
        hash = num % self.__m
        return hash

    def myhashExtraccion(self, num):
        hash = (abs(num) % 100)%self.__m
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

