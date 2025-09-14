from Nodo import Nodo

class ListaEncadenada:
    __ul = None
    __cantidad: int
    __cab = None
    __anterior = None
    __siguiente = None


    def __init__(self):
        self.__cab = None
        self.__cantidad =0
        self.__ul = None
        self.__anterior = None
        self.__siguiente = None

    def insertar(self, elemento):
        #este insertar contempla el self.__ul, pero es mas largo
        unNodo = Nodo(elemento)
        if self.__cab == None:
            unNodo.setSig(self.__cab)
            self.__cab = unNodo
            self.__ul = unNodo
            self.__cantidad+=1
        else:
            if elemento:
                print("agrega en posicion determinada")
                pos = self.buscar(elemento)
                if pos ==0:
                    unNodo.setSig(self.__cab)
                    self.__cab = unNodo
                    self.__cantidad += 1
                else:
                    aux = self.__cab
                    anterior = None
                    i =0
                    while i<pos:
                        anterior = self.anterior(aux)
                        aux = self.siguiente(aux)
                        i+=1
                    unNodo.setSig(aux)
                    anterior.setSig(unNodo)

                    if pos == self.__cantidad:
                        self.__ul = unNodo
                    self.__cantidad+=1

            else:
                print("\n---CUIDADO - Fuera de rango-----\n")
    def insertarconul(self, elemento):
        #En este insertar no contemplo el self.__ul, por lo tanto tendria que iterar en metodo "ultimoElemento"
        unNodo = Nodo(elemento)
        pos = self.buscar(elemento)
        if self.__cab == None or pos == 0:
            unNodo.setSig(self.__cab)
            self.__cab= unNodo
            self.__cantidad += 1
        else:
            aux = self.__cab
            anterior = self.__cab
            i = 0
            while i < pos:
                anterior = self.anterior(aux)
                aux = self.siguiente(aux)
                i += 1
            unNodo.setSig(aux)
            anterior.setSig(unNodo)

    def insertarSimple(self, elemento):
        if self.vacia():
            print("lista vacia")
            return
        if elemento:
            pass
    def buscar(self, elemento):
        if self.vacia() == False:
            aux = self.__cab
            pos=0
            bandera = False
            while aux != None and bandera == False:
                if elemento < aux.getDato():
                    bandera = True
                else:
                    aux = self.siguiente(aux)
                    pos+=1
            print("posicion encontrada:",pos)
            self.__anterior =
            return pos
        else:
            print("Lista vacia")
            return -1


    def suprimir(self, elemento):
        #como el insertart este metodo suprimir tampoco contempla cambiar el self.__ul
        if self.vacia() == False and elemento == self.__cab.getDato():
            self.__cab = self.__cab.getSig()
        else:
            aux = self.__cab
            anterior = None
            i = 0
            while aux != None and elemento != aux.getDato():
                anterior = self.anterior(aux)
                aux = aux.getSig()
            if aux != None:
                anterior.setSig(aux.getSig())
                self.__cantidad -= 1
            else:
                print("el dato no se encuentra en dicha posicion")
    def recuperar(self):
        pass
    def mostrar(self):
        aux = self.__cab
        while aux != None:
            print(f"Dato:{aux.getDato()}")
            aux = aux.getSig()

    def primerElemento(self):
        print(f"primero:{self.__cab.getDato()}")
        return self.__cab.getDato()

    def ultimoElemento(self):
        print(f"ultimo:{self.__ul.getDato()}")
        return self.__ul.getDato()

    def siguiente(self, nodo):
        return nodo.getSig()

    def anterior(self, nodo):
        #otra forma seria iterar hasta encontrar el anterior. ( elemento anterior no el nodo)
        return nodo

    def vacia(self):
        return self.__cab == None






if __name__ == "__main__":
    lista = ListaEncadenada()


    lista.insertarconul(50)
    lista.insertarconul(70)
    print("\ninserto 30 en la posicion 0")
    lista.insertarconul(30)


    lista.insertarconul(40)
    lista.insertarconul(20)
    lista.insertarconul(80)

    lista.mostrar()
    #lista.ultimoElemento()
    #lista.primerElemento()

    #lista.suprimir(20)

    print("Luego de suprimir el primer elemento '20'")
    #lista.mostrar()

    #lista.suprimir(50)

    print("Luego de suprimir el primer elemento '50'")
    #lista.mostrar()




