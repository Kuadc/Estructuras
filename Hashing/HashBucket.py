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

    def inicializar(self):
        for i in range(self.__t):
            self.__array[i] = Bucket(self.__c)

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


    def insert(self, num):
        pos = self.myhashDivision(num)
        print("posicion del hash:", pos)
        self.inRe(num, pos, self.__m)

    def inRe2(self, num, pos,overflow):
        if self.__contador[pos]==0:
            self.__array[pos].insertar(num)
            self.__contador[pos]+=1
            return
        else:
            if self.__contador[pos] < self.__c:
                self.__array[pos].insertar(num)
                self.__contador[pos]+=1
                return
            else:
                if self.__contador[overflow] < self.__c:
                    self.__array[overflow].insertar(num)
                    self.__contador[overflow]+=1
                    return
                pos = overflow+1
                self.inRe(num, pos, overflow+1)

    def inRe(self, num, pos,overflow):
        if self.__contador[pos]==0:
            self.__array[pos].insertar(num)
            self.__contador[pos]+=1
            return
        else:
            if self.__contador[pos] < self.__c:
                self.__array[pos].insertar(num)
                self.__contador[pos]+=1
                return
            else:
                if self.__contador[overflow] == self.__c:
                    pos=overflow+1
                    self.inRe(num, pos, overflow+1)
                self.__array[overflow].insertar(num)
                self.__contador[overflow]+=1

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
        for i in range(self.__t):
            print(self.__array[i].mostrar())

    def tamañoOvwerflow(self):
        print(f"m: {self.__m} t:{self.__t}")
        return self.__t - self.__m



if __name__ == "__main__":
    b = HashBucket(30, 3)
    b.inicializar()
    
    tam = b.tamañoOvwerflow()
    print(f"Tamaño del area de overflow: {tam}")

    b.insert(3)
    b.insert(13)
    b.insert(23)
    b.insert(33)
    b.insert(43)
    b.insert(53)
    b.insert(63)
    b.mostrar()







