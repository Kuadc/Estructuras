from Nodo import NodoArbol

class Abb:
    __raiz:None
    __nod:None

    def __init__(self):
        self.__raiz = None

    def insertaHoja(self, nodo):
        self.__raiz = nodo

    def insertarNuevo(self, x, nod):
        if nod == None:
            nodo = NodoArbol(x)
            return nodo
        else:
            if x == nod.getDato():
                print("Ya existe el elemento")
                return
            elif x < nod.getDato():
               nod.setIzq(self.insertarNuevo(x, nod.getIzq()))
            else:
                nod.setDer(self.insertarNuevo(x, nod.getDer()))
        return nod

    def preOrden(self, nodo):
        if nodo != None:
            print(f"{nodo.getDato()}")
            self.preOrden(nodo.getIzq())
            self.preOrden(nodo.getDer())
        else:
            return

    def getCabeza(self):
        return self.__raiz


    def iniciar(self,x):
        nodo = NodoArbol(x)
        self.__raiz = nodo


if __name__ == "__main__":

    a = Abb()
    a.iniciar(15)
    a.insertarNuevo(10, a.getCabeza())
    a.insertarNuevo(20, a.getCabeza())
    a.insertarNuevo(56, a.getCabeza())
    a.insertarNuevo(5, a.getCabeza())



    print("por Izquierda")
    a.preOrden(a.getCabeza())
