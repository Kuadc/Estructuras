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
        self.__pr = None

    def insertar(self, elemento,pos ):
        unNodo = Nodo(elemento)
        if self.__cab == None:
            unNodo.setSig(self.__cab)
            self.__cab = unNodo
            self.__pr = unNodo
            self.__ul = unNodo
            self.__cantidad+=1

        if pos == self.__cantidad:
            print("agrega al final")
            #agrega al final
            self.__ul.setSig(unNodo)
            self.__ul = unNodo
            self.__cantidad+=1
        else:
            if 1<= pos <self.__cantidad:
                print("agrega en posicion determinada")
                if pos == 1:
                    print("si la posicion es 1")
                    unNodo.setSig(self.__cab)
                    self.__cab = unNodo
                    self.__pr = unNodo
                    self.__cantidad+=1
                else:
                    print("si la possicoin es mayor a 2")
                    aux = self.__cab
                    anterior = self.__cab
                    i=0
                    while aux != None and i<pos-1:
                        anterior = aux
                        aux = aux.getSig()
                        i+=1
                    if i == pos-1:
                        anterior.setSig(unNodo)
                        unNodo.setSig(aux)
                        self.__cantidad+=1
            else:
                print("\n---CUIDADO - Fuera de rango-----\n")


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
    lista.insertar(60, 6)

    lista.mostrar()

    #suprimiendo
    print("\n suprimiendo.....")
    lista.suprimir(30,1)
    print("\n")
    lista.mostrar()





