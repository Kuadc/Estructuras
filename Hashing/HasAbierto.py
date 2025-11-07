import numpy as np

class HashAbierto:
    __m:int
    __array: np.array

    def __init__(self, m):
        self.__m = int(m//0.7)
        self.__array = np.zeros(self.__m, dtype=object)

    def insertar(self, num):
        pos = self.hashmodulo(num)
        if self.__array[pos] == 0:
            self.__array[pos] = num
            return

        pos = self.buscarPos(num, pos)
        if pos != -1:
            self.__array[pos] = num

    def insert(self, num):
        pos = self.hashmodulo(num)
        self.inReC(num, pos,1)
    

    # insertar recursivo con busqueda de residuo cuadratico
    def inReC(self, num, pos, i):
        if self.__array[pos] ==0:
            self.__array[pos] = num
            return
        else:
            if self.__array[pos] == num:
                print("repetido")
                return
            pos = (pos + (pow(pos,i))) %self.__m
            self.inReC(num, pos,i+1)

    # insertar recursivo con busqueda de prueba lineal

    def inRe(self, num, pos):
        if self.__array[pos] == 0:
            self.__array[pos] = num
            return
        else:
            if self.__array[pos] == num:
                print("ya existe")
                return
            pos = (pos + 1) % self.__m
            self.inRe(num, pos)

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
    
    def proximo(self, pos,i):
        pos = (pos + pow(pos,i)) % self.__m
        print(f"proxima posicion obtenida: {pos}")
        return pos


if __name__ == "__main__":
    h = HashAbierto(10)
    h.insert(2033)
    h.insert(5035)
    h.insert(4089)
    h.insert(5089)#posicion 7
    h.insert(5103)#posicion 7 - luego de la prueba lineal se inserta en la 8
    h.insert(5103)#posicion 7 - luego de la prueba lineal se inserta en la 8

    h.mostrar()
