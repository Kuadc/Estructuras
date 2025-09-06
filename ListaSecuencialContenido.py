import numpy as np

class listaSecuencial:
    __ul:int
    __pr:int
    __cantidad:int
    __tamaño:int
    __arreglo: np.ndarray


    def __init__(self, tamaño=0):
        self.__ul = -1
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
            self.__cantidad += 1
        elif item and self.__cantidad <self.__tamaño:
            print("inserta en posicion determinada")
            pos = self.buscar(item)

            ultimo = self.__ul
            while ultimo >= pos:
                self.__arreglo[ultimo + 1] = self.__arreglo[ultimo]
                ultimo -= 1
            self.__arreglo[pos] = item
            self.__cantidad += 1
            self.__ul += 1

        else:
                print("la posicion esta fuera de rango o la lista esta llena")

    def buscar(self, elemento):
        #retorna la posicion- implementar busqueda binaria
        pos =0
        max= self.__ul
        min = 0
        while min <= max:
            medio = (min +max) //2
            if elemento >self.__arreglo[medio]:
                pos = medio+1
                min = medio+1
            elif elemento == self.__arreglo[medio]:
                pos = medio
                min = max+1
            else:
                pos = medio
                max = medio - 1

        #retorna la posicion exacta
        return pos

    def suprimir(self, item):
        #suprime el elemento si existe
        if self.vacia() == False:
                pos = self.buscar(item)
                if  0<= pos <=self.__ul:
                    siguiente = self.__ul
                    while pos <=siguiente:
                        self.__arreglo[pos] = self.__arreglo[pos+1]
                        pos+=1
                    self.__ul-=1
                    self.__cantidad-=1
                else:
                    print("El elemento no se encuentra en la lista")
        else:
            print("Lista vacia")

    def recuperar(self, elemento):
        #retorna el elemento si lo encuentra
        if self.vacia() == False:
            pos = self.buscar(elemento)
            if 0 <= pos <= self.__ul:
                return self.__arreglo[pos]
            else:
                print("El elemento no se encuentra en la lista")
        else:
            print("Lista vacia")
    def anterior(self, pos):
        #CONSULTA: si tengo que retornar el elemento anterior o la posicion.
        if 1 < pos <= self.__cantidad:
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

if __name__ == "__main__":
    lista = listaSecuencial(10)


    lista.insertar(20)

    lista.insertar(10)

    lista.insertar(15)

    lista.insertar(50)

    lista.insertar(30)

    lista.insertar(18)


    print("--Lista luego de insertar--\n")
    lista.mostrar()

    lista.suprimir(15)
    print("\n--------------------------\n")
    print("--Lista luego de suprimir--\n")
    
    lista.mostrar()

    lista.suprimir(30)
    print("\n--------------------------\n")
    print("--Lista luego de suprimir--\n")
    lista.mostrar()



    lista.insertar(30)
    print("--Lista luego de insertar--\n")
    lista.mostrar()

