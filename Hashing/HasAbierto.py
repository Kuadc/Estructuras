import numpy as np

class HashAbierto:
    __m:int
    __array: np.array

    def __init__(self, m):
        self.__m = int(self.isprime(m)//0.7)

        self.__array = np.zeros(self.__m, dtype=object)

    def insertar(self, num):
        pos = self.hashmodulo(num)
        if self.__array[pos] == 0:
            self.__array[pos] = num
            return

        pos = self.buscarPos(num, pos)
        if pos != -1:
            self.__array[pos] = num

    def hashmodulo(self, num):
        pos = num %self.__m
        print(f"posicion obtenida en el hash:{pos}")
        return pos

    def buscarPos(self, num, pos):
        print("Buscando posicion con sondeo lineal...")

        while self.__array[pos] != 0 :
            if self.__array[pos] == num:
                print("El numero ya existe")
                return -1
            else:
                pos = (pos + 1) % self.__m
                print(f"nueva posicion obtenida: {pos}")
        return pos

    def buscarCuadratica(self, num, pos):
        i=0
        while self.__array[pos] != 0:

            pos = self.proximo(pos,i)
            if self.__array[pos] == num:
                print("El numero ya existe")
                return -1
            i+=1

        return pos
    
    def buscarDobleHash(self, num, pos):
        mod = self.isprime_dobleHash(self.__m - 1)
        hash2 = mod - (num % mod)

        while self.__array[pos] != 0:
            if self.__array[pos] == num:
                print("El numero ya existe")
                return -1
            else:
                pos = (pos + hash2) % self.__m
                print(f"nueva posicion obtenida: {pos}")
    
        return pos
    

    def mostrar(self):
        for i in range(self.__m):
            print(f"Numero: {self.__array[i]}")


    def isprime_dobleHash(self, num):
        while not isprime(num):
            num -= 1
        return num
    
    def isprime(self, num):
        while not isprime(num):
            num += 1
        return num


    #metodos de prueba
    def dobleHashing(self, num):
        hash1 = self.myhashDivision(num)
        mod = self.isprime_dobleHash(self.__m - 1)
        hash2 = mod - (num % mod)
        
        return (hash1 + hash2) % self.__m
    
    def pruebaLineal(self, num):
        hash = self.myhashDivision(num)
        i = 1
        while self.__array[(hash + i) % self.__m] != None:
            i += 1
        return (hash + i) % self.__m

    def proximo(self, pos,i):
        pos = (pos + pow(pos,i)) % self.__m
        print(f"proxima posicion obtenida: {pos}")
        return pos


if __name__ == "__main__":
    h = HashAbierto(10)
    h.insertar(2033)
    h.insertar(5035)
    h.insertar(4089)
    h.insertar(5089)#posicion 7
    h.insertar(5103)#posicion 7 - luego de la prueba lineal se inserta en la 8

    h.mostrar()
