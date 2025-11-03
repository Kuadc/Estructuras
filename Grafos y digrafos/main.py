from Digrafo import Digrafo


if __name__ == "__main__":
    #grafo = Digrafo(5)
    #grafo.insertarSecuencial(0,1)
    #grafo.insertarSecuencial(0,4)
    #grafo.Adyacentes(0)


    print("Encadenada")
    grafo1 = Digrafo(7)
    
    #grafo
    """grafo1.insertarEncadenada(0, 1)
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
    grafo1.insertarEncadenada(4, 2)"""
    
    
    #Digrafo no ponderado
    """grafo1.insertarEncadenada(0, 1)
    grafo1.insertarEncadenada(0, 4)
    
    grafo1.insertarEncadenada(1, 3)
    
    grafo1.insertarEncadenada(2, 4)
    
    grafo1.insertarEncadenada(3, 2)
    
    
    grafo1.insertarEncadenada(4, 1)"""
    
    
    #digrafo Ponderado
    
    
    grafo1.insertarEncadenada(0, 1, 2)
    grafo1.insertarEncadenada(0, 3, 1)
    
    grafo1.insertarEncadenada(1, 3, 3)
    grafo1.insertarEncadenada(1, 4, 10)
    
    grafo1.insertarEncadenada(2, 0, 4)
    grafo1.insertarEncadenada(2, 5, 5)
    
    
    grafo1.insertarEncadenada(3, 2, 2)
    grafo1.insertarEncadenada(3, 4, 2)
    grafo1.insertarEncadenada(3, 5, 8)
    grafo1.insertarEncadenada(3, 6, 4)
    
    grafo1.insertarEncadenada(4, 6, 6)
    
    grafo1.insertarEncadenada(6, 5, 1)
    
    
    
    """grafo1.Adyacentes(0)
    grafo1.REA(3)

    grafo1.camino(2,0)
    grafo1.REP()
    
    if grafo1.ciclico():
        print("Es aciclico -'No tiene ciclos'- ")
    else:
        print("No es aciclico 'Tiene al menos un ciclo' ")

    print("\n")
    grafo1.gradoEntrada(1)
    grafo1.gradoSalida(1)
    
    print("\n---------Nodo fuente")
    grafo1.NodoFuente(0)
    
    print("\n---------Nodo pozo")
    grafo1.NodoPozo(1)"""
    
    print("\n---------dijkstra")
    
    grafo1.distancias(0)
    #grafo1.Adyacentes(1)
    
    
    # tratar de hacer los ejercicios de los examenes. 
    
    
