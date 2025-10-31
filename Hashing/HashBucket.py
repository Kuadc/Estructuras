import numpy as np
from Bucket import Bucket

class HashBucket:
    __m:int
    __c:int
    __n:int
    __t:int
    __array: np.array

    def __init__(self, n=0, c=0):
        self.__n = n
        self.__m = n//c
        self.__c = c
        self.__t = int((n//c) * 1.2)
        self.__array = np.zeros(self.__t, dtype=object)

    def myhashDivision(self, num):
        hash = num % self.__m
        return hash

    def insertar(self, num):
        pos = self.myhashDivision
        if self.__array[pos] == 0:
            self.__array[pos] = Bucket(self.__c)
            self.__array[pos].insertar(num)
            return

        if self.__array[pos].buscar(num):
            print("El Elemento ya existe")
            return

        if self.__array[pos].insertar(num):
            print("Elemento insertado")
        else:
            self.overflow(num)

    def overflow(self, num):
        if self.__array[self.__m+1] ==0:
            self.__array[self.__m+1] = Bucket(self.__c)
            self.__array[self.__m+1].insertar(num)
            return

        if self.__array[self.__m+1].buscar(num):
            print("El Elemento ya existe")
            return










