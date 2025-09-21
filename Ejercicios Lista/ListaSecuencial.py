import numpy as np

#Lista Secuencial por Posicion
class listaSecuencial:
    __ul:int
    __pr:int
    __cantidad:int
    __arreglo: np.ndarray


    def __init__(self, tamaño=0):
        self.__ul = 0
        self.__cantidad = 0
        self.__arreglo = np.zeros(tamaño, dtype=int)

    def vacia(self):
        return self.__cantidad == 0

    def insertarNuevo(self, item, pos):
        pos-=1
        if self.vacia() and pos ==0:
            self.__arreglo[self.__ul] = item
            self.__ul = 0
            self.__pr = 0
            self.__cantidad += 1
            return

        if 0 <= pos <= self.__ul+1:
            ultimo = self.__ul+1
            while ultimo > pos:
                print("ingreso")
                self.__arreglo[ultimo] = self.__arreglo[ultimo-1]
                ultimo -= 1
            self.__arreglo[pos] = item
            self.__cantidad += 1
            self.__ul += 1
        else:
            print("fuera de rango")


    def suprimir(self, pos):
        if self.vacia() == False:
            if 1 <= pos <= self.__cantidad:
                print("suprime en posicion determinada")
                siguiente = self.__ul
                while pos <= siguiente:
                    self.__arreglo[pos] = self.__arreglo[pos + 1]
                    pos += 1
                self.__ul -= 1
                self.__cantidad -= 1
            else:
                print("la posicion esta fuera de rango")
        else:
            print("Lista vacia")

    def recuperar(self, pos):
        return self.__arreglo[pos]

    def buscarEspacio(self, espacio):
        i = 0
        resto = 0
        while i< self.__cantidad:
            if self.__arreglo[i] == espacio:
                pos = i
                i = self.__cantidad
            elif self.__arreglo[i] > espacio:
                pos = i
                resto = self.__arreglo[i] - espacio
                i = self.__cantidad
            i += 1
        #shifteo el espacio ocupado va al final como un suprimir, pero agrego al final
        if pos >=0:
            siguiente = self.__ul
            while pos < siguiente:
                self.__arreglo[pos] = self.__arreglo[pos + 1]
                pos += 1
            self.__arreglo[self.__ul] = espacio
            pos = self.__ul
            self.__ul -= 1
            self.__cantidad -= 1
            self.__arreglo[self.__pr]+=resto
            return pos
        else:
            return None


    def mostrar(self):
        i=0
        while i<self.__cantidad:
            print(f"item numero {i+1}: {self.__arreglo[i]}")
            i+=1



if __name__ == "__main__":
    lista = listaSecuencial(5)
    lista.insertarNuevo(20,1)
    lista.insertarNuevo(10,2)
    lista.insertarNuevo(70, 3)
    lista.insertarNuevo(50, 1)


    print("--Lista luego de insertar--\n")
    lista.mostrar()
    #print("--------------------------\n")
    #lista.suprimir(2)
    #print("--Lista luego de suprimir--\n")
    #lista.mostrar()

    #print("Buscar elemento\n")
    #pos = lista.buscar(70)
    #print(f"Posicion:{pos}")




    """sig= lista.siguiente(2)
    print("siguiente:",sig)
    ant = lista.anterior(3)
    print("anteior:", ant)"""
