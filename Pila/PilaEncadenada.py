from Nodo import Nodo
class PilaEnca:
    __tope:None
    __cant:int

    def __init__(self, cant):
        self.__tope = None
        self.__cant = cant

    def insert(self,x):
        unNodo = Nodo(x)
        unNodo.setSig(self.__tope)
        self.__tope=unNodo
        self.__cant+=1

    def delete(self):
        if self.empty():
            print("Pila Vacia")
        else:
            aux = self.__tope
            self.__tope = aux.getSig()
            return aux.getDato()

    def show(self):
        aux = self.__tope
        while aux != None:
            print(f"{aux.getDato()}")
            aux = aux.getSig()

    def empty(self):
        return self.__cant == 0

if __name__ == "__main__":
    pi = PilaEnca(5)
    pi.insert(5)
    pi.insert(4)
    pi.insert(3)
    pi.insert(2)
    pi.insert(1)

    pi.show()

    pi.delete()
    print("mostrar despues de leer")
    pi.show()
