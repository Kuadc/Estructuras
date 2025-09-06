import numpy as np

class listaSecuencial:
    __ul:int
    __pr:int
    __cantidad:int
    __tamaño:int
    __arreglo: np.ndarray


    def __init__(self, tamaño=0):
        self.__ul = 0
        self.__pr = 0
        self.__cantidad = 0
        self.__tamaño = tamaño
        self.__arreglo = np.zeros(tamaño, dtype=int)

    def vacia(self):
        return self.__cantidad == 0
    
    def insertar(self, item):
        #la lista por contenido se inserta ordenado
        #agrego cuando la lista esta vacia
        if self.vacia():
            print("inserta al principio si esta vacia")
            self.__arreglo[self.__ul] = item
            self.__ul=0
            self.__pr = 0
            self.__cantidad += 1
        elif item:
            print("inserta en posicion determinada")
            pos = self.buscar(item)
            print(f"posicion encontrada:{pos}")
            shift = self.__cantidad - (pos-1)
            ultimo = self.__ul
            while shift >0:
                self.__arreglo[ultimo+1] = self.__arreglo[ultimo]
                ultimo -=1
                shift-=1
            self.__arreglo[pos-1] = item
            self.__cantidad+=1
            self.__ul+=1
        else:
            print("la posicion esta fuera de rango")

    def suprimir(self, item):
        if self.__cantidad != 0:
            if item:
                print("suprime en posicion determinada")
                pos = self.buscar(item)
                shift = self.__cantidad - pos
                siguiente = pos
                while shift >0:
                    self.__arreglo[siguiente-1] = self.__arreglo[siguiente]
                    siguiente +=1
                    shift-=1
                self.__ul-=1
                self.__cantidad-=1
            else:
                print("la posicion esta fuera de rango")
        else:
            print("Lista vacia")

    def recuperar(self, pos):
        if self.__cantidad != 0:
            if 1 <= pos <= self.__ul+1:
                return self.__arreglo[pos-1]
            else:
                print("la posicion esta fuera de rango")
        else:
            print("No se puede recuperar elemento - Lista vacia")

    def buscar(self, elemento):
        #retorna la posicion- imprementar busqueda binaria
        i=0
        pos =0
        max= self.__cantidad-1
        min = 1

        while min <= max:
            medio = (min +max) //2
            print("medio:",medio)
            if self.__arreglo[medio]==elemento:
                pos = medio
            elif self.__arreglo[medio]>elemento:
                min = medio+1
            else:
                max = medio-1            

        if pos == self.__cantidad:
            print("no se encontro el elemento")
        else:
            return pos+1

    def anterior(self, pos):
        if 1 < pos <= self.__cantidad:
            print("anteriohhhr:",pos - 1)
            return pos-1
        else:
            print("Error, el anterior esta fuera de rango")

    def siguiente(self, pos):
        pos -=1
        if 1 <= pos <self.__ul:
            return pos+1
        else:
            print("Error, el siguiente esta fuera de rango")

    def mostrar(self):
        print("para mostrar")
        i=0
        while i<self.__cantidad:
            print(f"item numero {i+1}: {self.__arreglo[i]}")
            i+=1


if __name__ == "__main__":
    lista = listaSecuencial(5)
    lista.insertar(20)
    lista.insertar(10)
    lista.insertar(15)
    lista.insertar(50)
    
    


    print("--Lista luego de insertar--\n")
    lista.mostrar()
    print("--------------------------\n")
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
