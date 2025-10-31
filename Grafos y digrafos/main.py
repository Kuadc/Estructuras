from Digrafo import Digrafo


if __name__ == "__main__":
    #grafo = Digrafo(5)
    #grafo.insertarSecuencial(0,1)
    #grafo.insertarSecuencial(0,4)
    #grafo.Adyacentes(0)


    print("Encadenada")
    grafo1 = Digrafo(5)
    grafo1.insertarEncadenada(0, 1)
    grafo1.insertarEncadenada(0, 4)
    
    grafo1.insertarEncadenada(1, 0)
    grafo1.insertarEncadenada(1, 3)
    grafo1.insertarEncadenada(1, 4)
    
    grafo1.insertarEncadenada(2, 3)
    grafo1.insertarEncadenada(2, 4)
    
    grafo1.insertarEncadenada(3, 1)
    grafo1.insertarEncadenada(3, 2)
    
    grafo1.insertarEncadenada(4, 0)
    grafo1.insertarEncadenada(4, 1)
    grafo1.insertarEncadenada(4, 2)
    
    grafo1.Adyacentes(0)
    grafo1.REA(3)

    grafo1.camino(3,4)

