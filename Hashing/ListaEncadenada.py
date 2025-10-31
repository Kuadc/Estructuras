from Nodo import Nodo

class ListaEncadenada:
    __cab = None
    def __init__(self):
        self.__cab = None

    def insertar(self, x):
        nodo = Nodo(x)
        nodo.setSig(self.__cab)
        self.__cab = nodo

    def buscar(self, num):
        if self.__cab.getDato() == num:
            return True
        else:
            aux = self.__cab
            while aux != None and aux.getDato() != num:
                aux = aux.getSig
            if aux == None:
                return False
            else:
                return True




    def suprimir(self, pos):
        if self.__cab == None:
            return
        else:
            x = self.__cab
            self.__cab = self.__cab.getSig()
        return x

    def mostrar(self):
        aux = self.__cab
        while aux != None:
            print(f"Dato:{aux.getDato()}")
            aux = aux.getSig()





if __name__ == "__main__":
    lista = ListaEncadenada()
    lista.insertar(50,1)
    lista.insertar(70,2)
    lista.insertar(30,3)

    #se inserta en la posicion determinada
    lista.insertar(40,2)

    #insertando no valido
    lista.insertar(60, 1)
    lista.insertar(90, 3)

    lista.mostrar()

    #suprimiendo
    print("\n suprimiendo.....")
    lista.suprimir(1)
    print("\n")
    lista.mostrar()





