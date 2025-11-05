from Nodo import NodoArbol

class Abb:
    __raiz:None

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
    def mostrar(self):
        self.PostOrden(self.__raiz)

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

    def insertar(self, num):
        self.__raiz = self.insertarRe(self.__raiz, num)

    def insertarRe(self, nodo, num):
        if nodo is None:
            nuevo = NodoArbol(num)
            return nuevo
        else:
            if num == nodo.getDato():
                print("Ya existe el numero")
                return
            elif num < nodo.getDato():
                nodo.setIzq(self.insertarRe(nodo.getIzq(), num))
            else:
                nodo.setDer(self.insertarRe(nodo.getDer(), num))

        return nodo

    def imprimir_arbol(self, raiz, nivel=0):
        if raiz is not None:
            self.imprimir_arbol(raiz.getDer(), nivel + 1)
            print("    " * nivel + f"{raiz.getDato()}")
            self.imprimir_arbol(raiz.getIzq(), nivel + 1)
    
    def nodoHoja(self):
        cantidad = self.nodoHojaRe(self.__raiz)
        print(f"cantida nodos hojas:{cantidad}")

    def nodoHojaRe(self, nodo):
        if nodo is None:
            return 0
        else:
            if nodo.getDer() is None and nodo.getIzq() is None:
                return 1
            else:
                izq = self.nodoHojaRe(nodo.getIzq())
                der = self.nodoHojaRe(nodo.getDer())
                return (izq+der)
    def descendientesDirectos(self):
        cant = self.desRe(self.__raiz)
        print("cantidad de descendientes:", cant)
        

    def desRe(self, nodo):
        if nodo is None:
            return 0
        else:
            if nodo.getIzq() is None or nodo.getDer() is None:
                return 1
            else:
                izq = self.desRe(nodo.getIzq())
                der = self.desRe(nodo.getDer())
                return (der+izq)

    def nivel(self, nivel):
        self.nivelRe(self.__raiz, nivel,1)

    def nivelRe(self, nodo, nivel,x):
        if nodo is None:
            return
        else:
            if nivel == x:
                print(f"nodo en el nivel {x}: {nodo.getDato()}")
            else:
                self.nivelRe(nodo.getIzq(),nivel, x+1)
                self.nivelRe(nodo.getDer(), nivel, x+1)


if __name__ == "__main__":

    a = Abb()
    a.insertar(15)#raiz
    a.insertar(20)#derecha
    a.insertar(50)#derecha
    a.insertar(5)#izq
    a.insertar(19)#derecha-izq
    a.insertar(60)#derecha-derecha
    a.insertar(13)#izq-derecha
    a.insertar(12)#iz-derecha-izq
    
    a.imprimir_arbol(a.getCabeza())
    print("------------PreOrden-----------\n")
    a.nodoHoja()
    a.descendientesDirectos()
    a.nivel(4)