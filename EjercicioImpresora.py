from Colasecuencial2 import cola
from trabajo import paginas


class impresora:
    __tms =0
    __reloj =0
    __estado =""
    __tiempomax=0
    __tiempoAcumulado =0

    __contador = 0
    def __init__(self, tms=60, reloj=0, estado ="libre"):
        self.__tms = tms
        self.__reloj = reloj
        self.__estado = estado
        self.__contador = 0
        self.__tiempomax = 3
        self.__tiempoAcumulado = 0

    def EjecutarTrabajo(self, cola):
        estado = 0
        tiempo=0
        while estado <30:
            if cola.vacia():
                unTrabajo = cola.suprimir()
                print("trabajoooooooooooooo:",unTrabajo)
                tiempo = unTrabajo.getPag()
                if tiempo <= 30:
                    self.__contador+=1
                    self.__tiempoAcumulado+=self.__reloj - unTrabajo.getTemp()
                    estado+=tiempo
                elif tiempo >30:
                    unTrabajo.setPag(30)
                    cola.insertar(unTrabajo)
                    estado=30
            else:
                if cola.vacia() and estado <30:
                    estado = 30
        self.__reloj+=tiempo       

    def start(self, cola, pag):
        while self.__reloj < self.__tms:
            if self.__reloj %5 == 0:
                trab = paginas(10, self.__reloj)
                cola.insertar(trab)
                cola.mostrar()

            if self.__estado == "libre":
                if pag >=1:
                    trab = paginas(pag, self.__reloj)
                    cola.insertar(trab)
                    self.EjecutarTrabajo(cola)
                    #empieza a trabajar
                else:
                    if cola.vacia() == False:
                        self.__reloj+=1
                        #TRABAJA LA IMPRESORA CON EL TRABAJO EN COLA

        


if __name__ == "__main__":
    col = cola(10)
    impres = impresora()
    impres.start(col, 10)




