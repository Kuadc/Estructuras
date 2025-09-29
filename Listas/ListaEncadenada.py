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

    def insertar(self, x,pos):
        pos-=1
        if self.__cab == None or pos ==0:
            nodo = Nodo(x)
            nodo.setSig(self.__cab)
            self.__cab = nodo
            self.__cantidad +=1
        else: 
            print("posicion determinada",pos)
            if 1<= pos <=self.__cantidad:
                i=0
                aux = self.__cab
                anterior = self.__cab
                while i<pos:
                    anterior = aux
                    aux = aux.getSig()
                    i+=1
                nodo = Nodo(x)
                nodo.setSig(aux)
                anterior.setSig(nodo)
                self.__cantidad+=1
            else:
                print("fuera de rango")
                    


    def vacia(self):
        return self.__cantidad == 0

    def suprimir(self, pos):
        if self.vacia():
            print("lista vacia")
        else:
            pos-=1
            if 0<= pos <=self.__cantidad-1:
                if pos==0:
                    x = self.__cab.getDato()
                    self.__cab = self.__cab.getSig()
                    self.__cantidad-=1
                else:
                    i=0
                    aux = self.__cab
                    ant = self.__cab
                    while i<pos:
                        ant = aux
                        aux = aux.getSig()
                        i+=1
                    print(f"dato en aux:{aux.getDato()}")
                    x = aux.getDato()
                    ant.setSig(aux.getSig())
                    return x
            else:
                print("fuera de rango")
                        


    def suprimir2(self, elemento , pos):

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
    lista.insertar(60, 1)
    lista.insertar(90, 3)

    lista.mostrar()

    #suprimiendo
    print("\n suprimiendo.....")
    lista.suprimir(1)
    print("\n")
    lista.mostrar()





