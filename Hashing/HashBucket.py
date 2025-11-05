import numpy as np
from Bucket import Bucket

class HashBucket:
    __m:int
    __t:int
    __c:int
    __array: np.array
    

    def __init__(self, n=0, c=0):
        self.__c = c
        self.__m = n//c
        self.__t = int((n//c) * 1.2)
        self.__array = np.zeros(self.__t, dtype=object)
        self.__contador = np.zeros(self.__t,dtype=object)

    def myhashDivision(self, num):
        hash = num % self.__m
        return hash

    def insertar(self, num):
        pos = self.myhashDivision
        if self.__contador[pos] == 0:
            self.__array[pos] = Bucket(self.__c)
            self.__array[pos].insertar(num)
            self.__contador[pos]+=1
            return

        if self.__contador[pos] < self.__c:
            if self.__array[pos].buscar():
                print("Elemento ya ingresado")
                return
            else:
                self.__array[pos].insertar(num)
                self.__contador[pos]+=1
        else:
            self.overflow(num)

    def overflow(self, num):
        tamaño = self.__t - self.__m
        i=0
        while i<tamaño:
            if self.__array[self.__m + i] == 0:
                self.__array[self.__m + i] = Bucket(self.__c)
                self.__array[self.__m + i].insertar(num)
                self.__contador[self.__m + i] += 1
                return
            elif self.__contador[self.__m + i] < self.__c:
                    self.__array[self.__m + i].insertar(num)
                    self.__contador[self.__m + i] += 1
                    return
            i+=1

    def mostrar(self):
        print(self.__array)


if __name__ == "__main__":
    b = HashBucket(30, 3)
    b.mostrar()







