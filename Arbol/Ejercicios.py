from ArbolBinarioBusqueda import Abb


if __name__ == "__main__":

    a = Abb()
    a.iniciar(15)
    a.insertarNuevo(10, a.getCabeza())
    a.insertarNuevo(20, a.getCabeza())
    a.insertarNuevo(56, a.getCabeza())
    a.insertarNuevo(5, a.getCabeza())10

    print("muestra por Izquierda primer")
    a.preOrden(a.getCabeza())

    print("\n------------------------------")
    print("------------Punto A-----------\n")

    nodo = int(input("Ingrese un numero:"))
    a.PuntoA(nodo, a.getCabeza())
