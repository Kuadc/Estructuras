from Nodo import NodoArbol

class Abb:
    __raiz:None
    __nod:None

    def __init__(self):
        self.__raiz = None

    def insertaHoja(self, raiz):
        self.__raiz = raiz

    def buscar(self, x, raiz):
        if raiz.getDato() == None:
            print("arbol vacio")
        else:
            if raiz.getDato() == x:
                print("Elemento encontrado")
                print("jsjasjsd")
            else:
                if x < raiz.getDato():
                    self.buscar(x, raiz.getIzq())
                else:
                    if x > raiz.getDato():
                        self.buscar(x , raiz.getDer())
    
    def insertarNuevo(self, x, nod):
        if nod == None:
            raiz = NodoArbol(x)
            return raiz
        else:
            if x == nod.getDato():
                print("Ya existe el elemento")
                return
            elif x < nod.getDato():
               nod.setIzq(self.insertarNuevo(x, nod.getIzq()))
            else:
                nod.setDer(self.insertarNuevo(x, nod.getDer()))
        return nod

    def preOrden(self, raiz):
        if raiz != None:
            print(f"{raiz.getDato()}")
            self.preOrden(raiz.getIzq())
            self.preOrden(raiz.getDer())
        else:
            return
    
    def InOrden(self, raiz):
        if raiz != None:
            self.preOrden(raiz.getIzq())
            print(f"{raiz.getDato()}")
            self.preOrden(raiz.getDer())
        else:
            return

    def PostOrden(self, raiz):
        if raiz != None:
            self.preOrden(raiz.getIzq())
            self.preOrden(raiz.getDer())
            print(f"{raiz.getDato()}")
        else:
            return

    def getCabeza(self):
        return self.__raiz

    def altura(self, altura, raiz): # aqui recibo el elemento del raiz para comparar que altlura tiene o la altura es solo sobre la raiz?
        if raiz.getIzq() != None:
            return self.altura(altura, raiz.getIzq())+1
        elif raiz.getDer() != None:
            return self.altura(altura, raiz.getDer())+1
        else: 
            return altura

    def hoja(self, raiz):
        if raiz.getIzq() == None and raiz.getDer() == None:
            return True
        else: return False

    def grado(self, raiz):
        grado = 0
        if raiz.getIzq() == None and raiz.getDer() == None:
            grado = 0
        elif raiz.getIzq() == None or raiz.getDer() == None:
            grado = 1
        else:
            grado = 2
        return grado
    
    def hijo(self, raiz):
        if raiz.getDer() != None:
            return raiz.getDer()
        else:
            return raiz.getIzq()

    def maximo(self, raiz):
        if raiz.getDer() != None:
            return self.maximo(raiz.getDer())
        else:
            return raiz

    def suprimir(self, x, raiz):
        if self.__raiz == None:
            print("Arbol vacio")
        else:
            print(raiz.getDato())
            if raiz.getDato() == x:
                if self.grado(raiz) == 0:
                    return None
                elif self.grado(raiz) == 1:
                    hijo = self.hijo(raiz)
                    return hijo
                else:
                    #buscar el maximo para agregalo como nueva raiz
                        maximo = self.maximo(raiz.getIzq())
                        print(f"maximo que encontro:{maximo.getDato()}")
                        raiz.setDato(maximo.getDato())
                        raiz.setIzq(self.suprimir(maximo.getDato(), raiz.getIzq()))
                        return raiz
            elif raiz.getDato() > x:
                raiz.setIzq(self.suprimir(x, raiz.getIzq()))
            else:
                raiz.setDer(self.suprimir(x, raiz.getDer()))
        return raiz


    def iniciar(self,x):
        raiz = NodoArbol(x)
        self.__raiz = raiz

    def PuntoA(self, nodo, raiz):
        if raiz.getDato() != None:
            if raiz.getDato() == nodo:
                print(f"Nodo Encontrado:{nodo}")
                return True
            else:
                if nodo < raiz.getDato():
                    band = self.PuntoA(nodo, raiz.getIzq())
                    if (band):
                        print(f"Padre:{raiz.getDato()}")
                        if raiz.getDer() != None:
                            print(f"Hermano:{raiz.getDer().getDato()}")
                else:
                    if nodo > raiz.getDato():
                        band = self.PuntoA(nodo, raiz.getDer())
                        if (band):
                            print(f"Padre:{raiz.getDato()}")
                            if raiz.getIzq() != None:
                                print(f"Hermano:{raiz.getIzq().getDato()}")
                            else:
                                print("No tiene hermanos")
        else:
            print("Nodo no encontrado")

    def PuntoD(self, nodo, raiz):
        if raiz.getDato() != None:
            if raiz.getDato() == nodo:
                print(f"Nodo Encontrado:{nodo}")
                print(f"Sucesores")
                self.preOrden(raiz)
            else:
                if nodo < raiz.getDato():
                    self.PuntoD(nodo, raiz.getIzq())

                else:
                    if nodo > raiz.getDato():
                        self.PuntoD(nodo, raiz.getDer())
        else:
            print("Nodo no encontrado")



if __name__ == "__main__":

    a = Abb()
    a.iniciar(15)
    a.insertarNuevo(10, a.getCabeza())
    a.insertarNuevo(20, a.getCabeza())
    a.insertarNuevo(56, a.getCabeza())
    a.insertarNuevo(5, a.getCabeza())
    altura = a.altura(0, a.getCabeza())
    print("altura:", altura)

    print("\n------------------------------")

    print("------------Punto A-----------\n")
    nodo = 56
    a.PuntoA(nodo, a.getCabeza())

    print("muestra por Izquierda primero ('Inorden VID')")
    a.preOrden(a.getCabeza())

    print("\n------------------------------")

    print("------------Punto D-----------\n")
    nodo = 10
    a.PuntoD(nodo, a.getCabeza())

    print("\n------------------------------")
    print("------------Ejercicio N°3-------\n")
    cadena = "Carlos"


    #a.buscar(5, a.getCabeza())
    #a.suprimir(15, a.getCabeza())
    #print("luego de suprimir")
    #a.preOrden(a.getCabeza())
    
    #altura = a.altura(0, a.getCabeza())
    #print("altura:", altura)