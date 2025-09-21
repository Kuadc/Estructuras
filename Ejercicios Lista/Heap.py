from ListaSecuencial import listaSecuencial


class Heap:
    __bloques:int
    __libre:int
    __heap:listaSecuencial

    def __init__(self, bloques=5, libres=5):
        self.__bloques = bloques
        self.__libre = libres

    def iniciar(self):
        self.__heap = listaSecuencial(self.__bloques)
        self.__heap.insertarNuevo(20, 1)
        self.__heap.insertarNuevo(10, 2)
        self.__heap.insertarNuevo(70, 3)
        self.__heap.insertarNuevo(50, 4)
        self.__heap.insertarNuevo(30, 5)

    def getHeap(self):
        return self.__heap

    def asignarEspacio(self, espacio):
        if self.__libre >=1:
            pos = self.__heap.buscarEspacio(espacio)
            if pos:
                self.__libre-= 1
                return pos
            else:
                print("no se encontro espacio disponile")
                return
        else:
            print("no hay espacio disponible")



if __name__ == "__main__":

    heap = Heap()
    heap.iniciar()

    numero = heap.asignarEspacio(20)
    print("------------------------------------------------")
    print("numero 20 asignado a la posicion en memoria:",numero)
    print("------------------------------------------------")

    lista=heap.getHeap()
    print("\n ---Espacio disponible----")
    lista.mostrar()


    numero2 = heap.asignarEspacio(40)
    print("------------------------------------------------")
    print("\nNumero 40 asignado a la posicion en memoria:",numero2)
    print("------------------------------------------------")

    print("\n ---Espacio disponible----")
    lista.mostrar()

    print(f"\n\nNumero almacenado en la direccion 0x{numero2} : {lista.recuperar(numero2)}")



