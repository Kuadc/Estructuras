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
        nodo = Nodo(elemento)
        pos = self.buscar(elemento)
        print(f"{pos}")
        if self.__cab == None:
            self.__cab = nodo
            self.__cantidad+=1
            return
        if elemento:
            nodo.setSig(self.__anterior.getSig())
            self.__anterior.setSig(nodo)
            self.__cantidad+=1
        else:
            print("Fuera de rango")

    def buscar(self, elemento):
        if self.vacia() == False:
            aux = self.__cab
            anterior = aux
            i = 0
            while aux!= None and elemento > aux.getDato():
                anterior = aux
                aux = aux.getSig()
                i+=1
            self.__anterior = anterior
        
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

    def siguiente(self, elemento):
        self.buscar(elemento)
        return self.__siguiente

    def anterior(self, elemento):
        self.buscar(elemento)
        return self.__anterior

    def vacia(self):
        return self.__cab == None






if __name__ == "__main__":
    lista = ListaEncadenada()


    lista.insertar(50)
    lista.insertar(70)
    print("\ninserto 30 en la posicion 0")
    lista.insertar(30)


    #lista.insertar(40)
    #lista.insertar(20)
    #lista.insertar(80)

    lista.mostrar()
    #lista.ultimoElemento()
    #lista.primerElemento()

    #lista.suprimir(20)

    print("Luego de suprimir el primer elemento '20'")
    #lista.mostrar()

    #lista.suprimir(50)

    print("Luego de suprimir el primer elemento '50'")
    #lista.mostrar()




