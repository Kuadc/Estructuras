from NodoAvl import NodoAvl

class AVLTree:
    __raiz: None

    def __init__(self):
        self.__raiz = None

    def rotarConHijoIzquierdo(self, nodo):

        k1 = nodo.getIzq()
        nodo.setIzq(k1.getDer())
        k1.setDer(nodo)

        #se Actualiza la altura del nodo Actual "nodo"
        nodo.setH(max(self.altura(nodo.getIzq()), self.altura(nodo.getDer()))+1)
        k1.setH(max(self.altura(k1.getIzq()), nodo.getH())+1)

        return k1

    def rotarConHijoDerecho(self, nodo):
        k1 = nodo.getDer()
        nodo.setDer(k1.getIzq())
        k1.setIzq(nodo)

        #Actualizacion de alturas
        nodo.setH(max(self.altura(nodo.getIzq()), self.altura(nodo.getDer()))+1)
        k1.setH(max(self.altura(k1.getDer()), nodo.getH())+1)

        return k1


    def altura(self, nodo):
        if nodo == None:
            return -1
        else:
            return nodo.getH()
    def balance(self, nodo):
        if (nodo == None):
            return
        if (self.altura(nodo.getIzq()) - self.altura(nodo.getDer())) > 1:

            #print(f"----------------------------------> nodo que entro en crisis:{nodo.getDato()}")
            if self.altura(nodo.getIzq().getIzq()) >= self.altura(nodo.getIzq().getDer()):
                print("Realizo rotacion simple Izquierda - Izquierda")
                nodo = self.rotarConHijoIzquierdo(nodo)   # Caso Izquierda - Izquierda
            else:
                print("Realizo doble rotacion izquierda derecha")
                nodo.setIzq(self.rotarConHijoDerecho(nodo.getIzq()))
                nodo = self.rotarConHijoIzquierdo(nodo)

        elif self.altura(nodo.getDer()) - self.altura(nodo.getIzq()) >1:

            #print(f"---------------------------------->nodo que entro en crisis:{nodo.getDato()}")
            if self.altura(nodo.getDer().getDer()) >= self.altura(nodo.getDer().getIzq()):

                print("Realizo rotacion simple - Derecha-Derecha")
                nodo = self.rotarConHijoDerecho(nodo) #caso Derecha-Derecha
            else:
                print("Realizo doble rotacion derecha izquierda")

                nodo.setDer(self.rotarConHijoIzquierdo(nodo.getDer()))
                nodo = self.rotarConHijoDerecho(nodo)

        nodo.setH(max(self.altura(nodo.getIzq()), self.altura(nodo.getDer())) +1)

        return nodo
    def insertarNuevo(self, x, nodo):
        if nodo == None:
            nodo = NodoAvl(x)
            return nodo
        else:
            if x == nodo.getDato():
                print("Ya existe el elemento")
                return
            elif x < nodo.getDato():
                nodo.setIzq(self.insertarNuevo(x, nodo.getIzq()))
            else:
                nodo.setDer(self.insertarNuevo(x, nodo.getDer()))
        nodo = self.balance(nodo)
        return nodo

    def sup(self,x):
        self.__raiz = self.suprimir(x,self.__raiz)

    def minimo(self,nodo):
        if nodo.getIzq() != None:
            return self.minimo(nodo.getIzq())
        else:
            return nodo
    def suprimir(self,x, nodo):
        if nodo == None:
            print("No se encontro el elemento")

        if x < nodo.getDato():
            nodo.setIzq(self.suprimir(x,nodo.getIzq()))
        elif x>nodo.getDato():
            nodo.setDer(self.suprimir(x, nodo.getDer()))
        elif nodo.getIzq() != None and nodo.getDer() != None:
            minimo = self.minimo(nodo.getDer())
            nodo.setDato(minimo.getDato())

            print(f"nodo minimo:{nodo.getDato()}")
            nodo.setDer(self.suprimir(nodo.getDato(),nodo.getDer()))
        else:
            if nodo.getIzq():
                nodo = nodo.getIzq()
            else:
                nodo = nodo.getDer()
        nodo = self.balance(nodo)

        return nodo
    def preOrden(self, raiz):
        if raiz != None:
            print(f"{raiz.getDato()}")
            self.preOrden(raiz.getIzq())
            self.preOrden(raiz.getDer())
        else:
            return
    def getCabeza(self):
        return self.__raiz

    def insertar(self,x):
        self.__raiz = self.insertarNuevo(x, self.__raiz)

    def imprimir_arbol(self, raiz, nivel=0):
        if raiz is not None:
            self.imprimir_arbol(raiz.getDer(), nivel + 1)
            print("    " * nivel + f"{raiz.getDato()}")
            self.imprimir_arbol(raiz.getIzq(), nivel + 1)


if __name__ == "__main__":

    #insertar   7,5,2,4,3,8,1,6,11,10,9
    a = AVLTree()
    a.insertar(7)
    a.insertar(5)
    a.insertar(2)
    a.insertar(4)
    a.insertar(3)
    a.insertar(8)
    a.insertar(1)
    a.insertar(6)
    a.insertar(11)
    a.insertar(10)
    a.insertar(9)



    #a.preOrden(a.getCabeza())
    a.imprimir_arbol(a.getCabeza())

    a.sup(4)

    print("\nsuprimir 8")
    a.sup(8)
    a.sup(6)
    a.sup(5)
    a.sup(2)
    a.sup(1)
    a.sup(7)


    a.imprimir_arbol(a.getCabeza())