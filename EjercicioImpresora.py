from Colasecuencial2 import cola
from trabajo import paginas


class impresora:
    __tms =0
    __reloj =0
    __estado =""
    __tiempomax=0
    __tiempoAcumulado =0

    __contador = 0
    def __init__(self, tms=3600, reloj=0, estado ="libre"):
        self.__tms = tms
        self.__reloj = reloj
        self.__estado = estado
        self.__contador = 0
        self.__tiempomax = 3
        self.__tiempoAcumulado = 0

    def EjecutarTrabajo(self, cola):
        estado = 0
        tiempo=0
        while estado <120:
            if cola.vacia() == False:
                unTrabajo = cola.suprimir()
                print("trabajo suprimido:",unTrabajo)
                tiempo = unTrabajo.getPag()
                tiempo *= 6
                if tiempo <= 120:
                    self.__contador+=1
                    self.__reloj+=tiempo
                    self.__tiempoAcumulado+=self.__reloj - unTrabajo.getTemp()
                    estado+=tiempo
                elif tiempo >120:
                    unTrabajo.setPag()
                    cola.insertar(unTrabajo)
                    estado=120
                    self.__reloj +=120
            else:
                if cola.vacia() and estado <120:
                    estado = 120



    def start(self, cola, pag):
        trab = paginas(pag, self.__reloj)
        cola.insertar(trab)
        while self.__reloj < self.__tms:
            if self.__reloj !=0 and self.__reloj % 300 == 0:
                print("se ejecuta:", self.__reloj)
                trab = paginas(40, self.__reloj)
                cola.insertar(trab)
                cola.mostrar()

            if cola.vacia():
                print("esta vacia suma 60seg al reloj")
                self.__reloj+=60
            else:
                if cola.vacia() == False:
                    print("tiene trabajo o trbaajos.")
                    cola.mostrar()
                    self.EjecutarTrabajo(cola)
        print("\n ---- Tiempo acumumulado de trabajar terminados en 60 minutos: ", self.__tiempoAcumulado)
        print("\n----Trabajos terminados en 60 minutos", self.__contador)
        print(f"\n--- Promedio de espera de trabajos: {(self.__tiempoAcumulado // self.__contador)//60} minutos")



if __name__ == "__main__":
    col = cola(10)
    impres = impresora()
    impres.start(col, 10)




