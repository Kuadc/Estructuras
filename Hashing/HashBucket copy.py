import numpy as np
from Bucket import Bucket

class HashBucket:
    __m:int
    __t:int
    __array: np.array

    def __init__(self, n=0, c=0):
        self.__m = n//c
        self.__t = int((n//c) * 1.2)
        self.__array = np.zeros((self.__t,c), dtype=object)
        self.__contador = np.zeros(self.__m,dtype=object)

    def myhashDivision(self, num):
        hash = num % self.__m
        return hash

    def insertar(self, num):
        pos = self.myhashDivision
        if self.__array[pos] == 0:
            self.__array[pos]
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

    def mostrar(self):
        print(self.__array)


if __name__ == "__main__":
    b = HashBucket(30, 3)
    b.mostrar()







