from ColaSecCajero import cola
import random

class Cajero:
    __tms: int
    __reloj: int
    __contador: int
    __atencion: int
    __tiempoAcumulado: int

    def __init__(self):
        self.__tms = 60
        self.__reloj = 0
        self.__contador = 0
        self.__atencion = 0
        self.__tiempoAcumulado = 0
    def start(self,cola):
        while self.__reloj < self.__tms:
            if 0<= random.random() <= 1 / 2:
                print("Inserto en la cola con tiempo:", self.__reloj)
                cola.insertarNuevo(self.__reloj, )

            if self.__atencion ==0 and cola.vacia() == False:
                x = cola.suprimir()
                self.__contador += 1
                print(f"reloj cuando se suprime:{self.__reloj}")
                print("tiempo de la cola suprimida:", x)
                self.__tiempoAcumulado += self.__reloj - x
                self.__atencion = 10
            else:
                self.__atencion-=1

            self.__reloj+=1

        print("----------TIEMPO PROMEDIO DE ATENCION-----------")
        print(f"---------{self.__tiempoAcumulado}---------")
        print(f"---------{self.__contador}---------")
        print("------------------------------------------------")









if __name__ == "__main__":
    #3 CAJEROS DISPONIBLES

    c1= cola(10,5)

    cajeros = Cajero()

    cajeros.start(c1)
