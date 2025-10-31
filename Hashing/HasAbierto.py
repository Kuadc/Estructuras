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

        pos = self.buscar(num, pos)
        if pos >=0:
            self.__array[pos] = num

    def hashmodulo(self, num):
        pos = num %self.__m
        print(f"posicion obtenida en el hash:{pos}")
        return pos

    def proximo(self, pos,i):
        pos = (pos + pow(pos,i)) % self.__m
        print(f"proxima posicion obtenida: {pos}")
        return pos


    def buscar(self, num, pos):
        i=0
        while i<10:
            nuevo = self.proximo(pos,i)
            if self.__array[nuevo] == num:
                print("El numero ya existe")
                i=10
            else:
                if self.__array[nuevo] == 0:
                    pos = nuevo
                    i=10
            i+=1
        return pos

    def mostrar(self):
        for i in range(self.__m):
            print(f"Numero: {self.__array[i]}")


if __name__ == "__main__":
    h = HashAbierto(10)
    h.insertar(2033)
    h.insertar(5035)
    h.insertar(4089)
    h.insertar(5089)

    h.mostrar()
