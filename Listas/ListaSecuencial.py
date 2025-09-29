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
            ultimo = self.__cantidad
            while ultimo >= pos:
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
                x = self.__arreglo[pos-1]
                siguiente = self.__ul
                while pos <= siguiente:
                    self.__arreglo[pos] = self.__arreglo[pos + 1]
                    pos += 1
                self.__ul -= 1
                self.__cantidad -= 1
                return x
            else:
                print("la posicion esta fuera de rango")
        else:
            print("Lista vacia")

    
    def suprimir2(self, pos):
        if self.vacia() == False:
            if 1 <= pos <= self.__cantidad:
                print("suprime en posicion determinada")
                x = self.__arreglo[pos]
                siguiente = self.__ul
                while pos < siguiente:
                    self.__arreglo[pos] = self.__arreglo[pos + 1]
                    pos += 1
                self.__ul -= 1
                self.__cantidad -= 1
                return x
            else:
                print("la posicion esta fuera de rango")
        else:
            print("Lista vacia")

    def recuperar(self, elemento):
        # retorna el elemento si lo encuentra
        if self.vacia() == False:
            pos = self.buscar(elemento)
            if 0 <= pos <= self.__ul:
                return self.__arreglo[pos]
            else:
                print("El elemento no se encuentra en la lista")
        else:
            print("Lista vacia")

    def buscar(self, elemento):
        #retorna la posicion
        i=0
        pos =0
        while i<self.__cantidad:
            if self.__arreglo[i] == elemento:
                pos =i
                i =self.__cantidad
            i+=1

        if pos == self.__cantidad:
            print("no se encontro el elemento")
        else:
            return pos

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

    def primerElemento(self):
        if self.vacia() == False:
            return self.__arreglo[0]
        else:
            print("Lista Vacia")

    def ultimoElemento(self):
        if self.vacia() == False:
            return self.__arreglo[self.__ul]
        else:
            print("Lista Vacia")

    
    def eliminarDuplicados(self):
        i=0
        j=0
  
        while i< self.__cantidad:
            dato = self.__arreglo[i]
            if j<self.__cantidad:
                if dato == self.__arreglo[j] and i!=j:
                    self.suprimir2(j)
                    i+=1
                    j=0
                j+=1 
            elif j==self.__cantidad:
                j=0
                i+=1
            else:
                j+=1
        


if __name__ == "__main__":
    lista = listaSecuencial(7)
    lista.insertarNuevo(20,1)
    lista.insertarNuevo(10,2)
    lista.insertarNuevo(70, 3)
    lista.insertarNuevo(50, 1)
    lista.insertarNuevo(70, 1)
    lista.insertarNuevo(50, 5)


    print("--Lista luego de insertar--\n")
    lista.mostrar()

    print("--Lista luego eliminar duplicados--\n")
    #lista.eliminarDuplicados()
    lista.suprimir(5)
    lista.mostrar()

