from ColaSecCajero import cola
import random

class Cajero:
    __tms: int
    __reloj: int
    __contador: int
    __sinA: int
    __tiempoAcumulado: int

    def __init__(self):
        self.__tms = 120
        self.__reloj = 0
        self.__contador = 0
        self.__sinA = 0
        self.__tiempoAcumulado = 0


    def eleccion(self, lista):
        li=list()
        menor = min(lista)
        print(lista)
        for i in range(len(lista)):
            if lista[i] == menor:
                li.append(i)
        if len(li)>0:
            eleccion = random.choice(li)

        else:
            eleccion = li[0]
        return eleccion

    def start(self, c1, c2, c3):
        lista = list()
        li = [c1,c2,c3]
        while self.__reloj < self.__tms:
            if self.__reloj >2:
                print("reloj actual:",self.__reloj)
                lista.append(c1.cantidad())
                lista.append(c2.cantidad())
                lista.append(c3.cantidad())
                eleccion = self.eleccion(lista)
                li[eleccion].insertar(self.__reloj)
                lista = []

            if c1.vacia() and c2.vacia() and c3.vacia():
                print("agrega 1 al reloj")
                self.__reloj+=1
            else:
                if c1.vacia() == False:
                    print("cajero 1")
                    cliente = c1.suprimir()
                    print("reloj cajero 1:", self.__reloj)
                    self.__reloj += c1.getMinutos()
                    print("minutos agregados al reloj", c1.getMinutos())
                    self.__contador += 1
                    self.__tiempoAcumulado+= self.__reloj - cliente

                elif c2.vacia() == False:
                    print("cajero 2")
                    print("reloj cajero 2:", self.__reloj)
                    cliente = c2.suprimir()
                    self.__reloj += c2.getMinutos()
                    print("minutos agregados al reloj", c2.getMinutos())
                    self.__contador += 1
                    self.__tiempoAcumulado += self.__reloj - cliente
                    print("reloj cajero 2 al finalizar:", self.__reloj)

                elif c3.vacia() == False:
                    print("cajero 3")
                    print("reloj cajero 3:", self.__reloj)
                    cliente = c3.suprimir()
                    self.__reloj += c3.getMinutos()
                    print("minutos agregados al reloj", c3.getMinutos())
                    self.__contador += 1
                    self.__tiempoAcumulado += self.__reloj - cliente

        tiempoTotalPromedio =  self.__tiempoAcumulado // self.__contador
        print("total de tiempo acumulado", self.__tiempoAcumulado)
        print("total de clientes atendidos", self.__contador)
        print(" Promedio de espera cliente atendidos: ", tiempoTotalPromedio)



if __name__ == "__main__":
    #3 CAJEROS DISPONIBLES
    # 1 CAJERO DEMORA EN ATENDER: 5
    # 2 CAJERO DEMORA EN ATENDER: 3
    # 3 CAJERO DEMORA EN ATENDER: 4

    #LLLEGA DE LOS CLIENTES EN 2 MINUTOS

    #CADA CAJERO TIENE SU COLA.
    c1= cola(10,5)
    c2 = cola(10,3)
    c3 = cola(10,4)

    cajeros = Cajero()

    cajeros.start(c1, c2, c3)

    #SE ELEJI ALEATORIAMENTE SI UN CLIENTE LLEGA Y MAS DE UN CAJERO ESTAN LIBRE Y COLA VACIA.

    #SI CAJEROS OCUPADOS : CLIENTE ELIJE LA COLA MAS CORTA.

    #SI HAY VARIAS COLAS CON LA MISMA CANTIDAD : ELECCION ALEATORIA

    """Realizar en un algoritmo que permita determinar:  
    a) El tiempo máximo de espera de los clientes en la cola.  
    b) Cantidad de clientes atendidos.  ok
    c) Cantidad de clientes que quedaron sin atender.  ok
    d) Promedio de espera de los clientes atendidos.   ok
    e) Promedio de espera de los clientes sin atender ok """
