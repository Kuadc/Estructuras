from Nodo import Nodo

class ListaEncadenada:
    __ul = None
    __pr = None
    __cantidad: int
    __cab = None

    def __init__(self):
        self.__cab = None
        self.__cantidad =0
        self.__ul = None

    def insertar(self, elemento):
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

            else:
                print("\n---CUIDADO - Fuera de rango-----\n")

    def buscar(self, elemento):
        if self.vacia() == False:
            aux = self.__cab
            pos = 0
            bandera = False
            while aux != None and bandera == False:
                if elemento < aux.getDato():
                    bandera = True
                else:
                    aux = self.siguiente(aux)
                    pos+=1

            print("posicion encontrada:",pos)
            return pos
        else:
            print("Lista vacia")


    def suprimir(self, elemento , pos):

        if 1 <= pos < self.__cantidad:
            if pos == 1 :
                if elemento == self.__cab.getDato():
                    print("si la posicion es 1")
                    self.__cab = self.__cab.getSig()
                    self.__pr = self.__cab
                    self.__cantidad-=1
                else:
                    print("El elemento no se encuentra en dicha posicion")
            else:
                print("si la posicion es mayor a 2")
                aux = self.__cab
                anterior = self.__cab
                i = 0
                while aux != None and i < pos - 1:
                    anterior = aux
                    aux = aux.getSig()
                    i += 1
                if i == pos - 1 and elemento == aux.getDato():
                    print(f"dato encontrado:{aux.getDato()}")
                    anterior.setSig(aux.getSig())
                    self.__cantidad-=1
                else:
                    print("el dato no se encuentra en dicha posicion")

        else:
            print("\n---CUIDADO - Fuera de rango-----\n")
    def recuperar(self):
        pass
    def mostrar(self):
        aux = self.__cab
        while aux != None:
            print(f"Dato:{aux.getDato()}")
            aux = aux.getSig()

    def primerElemento(self):
        pass

    def ultimoElemento(self):
        pass

    def siguiente(self, nodo):
        return nodo.getSig()

    def anterior(self, nodo):
        return nodo

    def vacia(self):
        return self.__cab == None






if __name__ == "__main__":
    lista = ListaEncadenada()
    lista.insertar(50)
    lista.insertar(70)
    print("\ninserto 30 en la posicion 0")
    lista.insertar(30)


    lista.insertar(40)
    lista.insertar(20)
    lista.insertar(80)


    lista.mostrar()







