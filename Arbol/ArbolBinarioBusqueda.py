from Nodo import NodoArbol

class Abb:
    __raiz:None
    __nod:None

    def __init__(self):
        self.__raiz = None

    def insertaHoja(self, nodo):
        self.__raiz = nodo

    def buscar(self, x, nodo):
        if nodo.getDato() == None:
            print("arbol vacio")
        else:
            if nodo.getDato() == x:
                print("Elemento encontrado")
            else:
                if x < nodo.getDato():
                    self.buscar(x, nodo.getIzq())
                else:
                    if x > nodo.getDato():
                        self.buscar(x , nodo.getDer())
    
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
    a.buscar(5, a.getCabeza())
    a.suprimir(15, a.getCabeza())
    print("luego de suprimir")
    a.preOrden(a.getCabeza())
