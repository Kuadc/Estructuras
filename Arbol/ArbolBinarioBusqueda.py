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

    #La cantidad de descendientes son todos los nodos que estran por debajo "cualquier numero"
    def Descendientes(self, num):
        self.cantDescendientes(self.__raiz, num)


    def cantDescendientes(self, nodo, num):
        if nodo == None:
            print("Nodo no encontrado")
            return
        else:
            if nodo.getDato() == num:
                print("nodo encontrado")
                cant = self.cantidad(nodo, 0)
                print(f"cantidad de descendientes:{cant}")
            elif num < nodo.getDato():
                self.cantDescendientes(nodo.getIzq(), num)
            else:
                self.cantDescendientes(nodo.getDer(), num)

    def cantidad(self, nodo, cant):
        if nodo == None:
            cant-=1
            return cant
        else:
            cant = self.cantidad(nodo.getIzq(), cant + 1)
            cant = self.cantidad(nodo.getDer(), cant + 1)
            return cant


    def imprimir_arbol(self, raiz, nivel=0):
        if raiz is not None:
            self.imprimir_arbol(raiz.getDer(), nivel + 1)
            print("    " * nivel + f"{raiz.getDato()}")
            self.imprimir_arbol(raiz.getIzq(), nivel + 1)

    def nodoshojas(self):
        self.nodoHojaRe(self.__raiz)


    def nodoHojaRe(self, nodo):
        if nodo == None:
            return
        elif nodo.getIzq() == None and nodo.getDer() == None:
            print(f"Nodo hoja{nodo.getDato()}")
        else:
            self.nodoHojaRe(nodo.getDer())
            self.nodoHojaRe(nodo.getIzq())


    def nodoHojaRaiz(self, nodo, izq, der):
        if nodo == None:
            return 0
        elif nodo.getIzq() == None and nodo.getDer() == None:
            return 1
        else:
            izq=self.nodoHojaRaiz(nodo.getDer(), izq, der)
            der=self.nodoHojaRaiz(nodo.getIzq(), izq, der)
            return (izq+der)


    #----------------------Grado de un nodo------------------------------------
    #---------------------------------------------------------------------------

    def gradoDeNodo(self, nodo, num):
        if nodo == None:
            return
        else:
            if nodo.getDato() == num:
                print("nodo encontrado, ver grado")
                grado = self.grado(nodo)
                print(f"grado del nodo:{grado}")
            elif num < nodo.getDato():
                self.gradoDeNodo(nodo.getIzq(), num)
            else:
                self.gradoDeNodo(nodo.getDer(), num)

    def gradoNodo(self, num):
        self.gradoDeNodo(self.__raiz, num)





    #----------------------altura de un nodo------------------------------------
    #---------------------------------------------------------------------------

    def verAlturaNodo(self, nodo):
        if not nodo:
            return -1
        alt_izq = self.verAlturaNodo(nodo.getIzq())
        alt_der = self.verAlturaNodo(nodo.getDer())
        return 1 + max(alt_izq, alt_der)


    def buscarAlturaNodo(self, nodo, num):
        if nodo == None:
            return
        else:
            if nodo.getDato() == num:
                print("Nodo encontrado, verticar alurta")
                altura = self.verAlturaNodo(nodo)
                print(f"Altura de nodo: {altura}")
            elif num < nodo.getDato():
                self.buscarAlturaNodo(nodo.getIzq(), num)
            else:
                self.buscarAlturaNodo(nodo.getDer(), num)
    def alturaNodo(self, num):
        if self.__raiz == None:
            print("No hay nodos")
        else:
            self.buscarAlturaNodo(self.__raiz, num)


    def NodoPadre(self, num, nodo):
        if nodo == None:
            return
        else:
            if nodo.getDato() == num:
                return True
            elif num < nodo.getDato():
                band=self.NodoPadre(num, nodo.getIzq())
                if band:
                    print("Hijo encontrado")
                    print(f"nodo padre:{nodo.getDato()}")
            else:
                band=self.NodoPadre(num, nodo.getDer())
                if band:
                    print("Hijo encontrado")
                    print(f"nodo padre:{nodo.getDato()}")

    def verNivel(self, nodo, nivel):
        if nodo is None:
            return nivel-1
        else:
            izq = self.verNivel(nodo.getIzq(), nivel+1)
            der = self.verNivel(nodo.getDer(), nivel+1)
            return max(izq,der)

    
    def nivelNodo(self, nodo, num):
        if nodo is None:
            return 
        else:
            if nodo.getDato() == num:
                nivel=self.verNivel(nodo,0)
                print(f"nivel de {num}: {nivel}")
            elif num < nodo.getDato():
                self.nivelNodo(nodo.getIzq(), num)
            else:
                self.nivelNodo(nodo.getDer(),num)

if __name__ == "__main__":

    a = Abb()
    a.iniciar(15)
    a.insertarNuevo(10, a.getCabeza())
    a.insertarNuevo(20, a.getCabeza())
    a.insertarNuevo(56, a.getCabeza())
    a.insertarNuevo(5, a.getCabeza())
    a.insertarNuevo(19, a.getCabeza())
    a.insertarNuevo(60, a.getCabeza())
    a.insertarNuevo(13, a.getCabeza())
    a.insertarNuevo(12, a.getCabeza())
    altura = a.altura(0, a.getCabeza())
    print("altura:", altura)

    print("\n------------------------------")

    print("------------Punto A-----------\n")
    nodo = 56
    #a.PuntoA(nodo, a.getCabeza())
    a.NodoPadre(nodo, a.getCabeza())

    print("muestra por Izquierda primero ('Inorden VID')")
    a.preOrden(a.getCabeza())

    print("\n------------------------------")

    print("------------Punto D-----------\n")
    nodo = 10
    a.PuntoD(nodo, a.getCabeza())

    print("\n------------------------------")
    print("------------Ejercicio N°3-------\n")
    cadena = "Carlos"

    a.imprimir_arbol(a.getCabeza())

    a.Descendientes(5)

    a.nodoshojas()

    cantidad= a.nodoHojaRaiz(a.getCabeza(),0,0)
    print(f"cantidad de hojas: {cantidad}")

    a.alturaNodo(10)

    a.nivelNodo(a.getCabeza(), 20)
    #a.buscar(5, a.getCabeza())
    #a.suprimir(15, a.getCabeza())
    #print("luego de suprimir")
    #a.preOrden(a.getCabeza())
    
    #altura = a.altura(0, a.getCabeza())
    #print("altura:", altura)