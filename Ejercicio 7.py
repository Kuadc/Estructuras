from Cola.ColaEncadenada import colaEnca

class impresora:
    __tms =0
    __reloj =0
    __estado =""
    __contador = 0
    __tiempomax=0
    __tiempoAcumulado =0

    def __init__(self, tms=60, reloj=0, estado ="libre"):
        self.__tms = tms
        self.__reloj = reloj
        self.__estado = estado
        self.__contador = 0
        self.__tiempomax = 3
        self.__tiempoAcumulado = 0

    def comenzarimpresion(self,cola):
        trabajo = cola.recuperarPrimero()
        trabajo = trabajo/10
        finalizado = 0
        # el while esta pensado en que trabaje 1 pagina por minuto
        while self.__tiempomax > finalizado:
            if trabajo == 1:
                finalizado =3
                self.__contador+=1
                cola.suprimir()
            trabajo -=1
            finalizado +=1
            self.__reloj +=1
        if trabajo >self.__tiempomax:
            cola.suprimir()
            cola.insertarNuevo(trabajo, )
        self.__estado = "libre"

    def comienzo(self, cola,trabajo):
        while self.__reloj < self.__tms:
            if (trabajo>1):
                cola.insertarNuevo(trabajo, )
                trabajo =0

            if self.__reloj % 5 ==0:
                nuevoTrabajo = int(input("Ingrese cantidad de paginas:"))
                cola.insertarNuevo(nuevoTrabajo, )

            if self.__estado == "libre":
                if cola.vacia() == False:
                    self.__estado = "ocupada"
                    self.comenzarimpresion(cola, trabajo)
            elif self.__estado == "ocupada":
                    #actualiza el tiempo
            else: self.__reloj+=1


if __name__ == "__main__":
    cola = colaEnca()
    impres = impresora()
    impres.comienzo(cola, 10)




