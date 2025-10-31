## anotaciones

def REACaminos(self, origen): 
    distancia = np.full(5, math.inf)
    visitado = np.zeros(self.__tamaño, dtype=bool)
    antesesor = np.zeros(self.__tamaño, int)
    unacola = ColaCircular(5)
    distancia[0]=0
    visitado[0]=True
    antesesor[0]=origen
    unacola.insertar(origen)
    while not unacola.vacia():
        v = unacola.suprimir()
        print(f"vertice suprimido:{v}")
        aux = self.__array[v].getcabeza()
        while aux != None:
            if visitado[aux.getDato()] == False:
                visitado[aux.getDato()]=True
                distancia[aux.getDato()]=distancia[v]+1
                antesesor[aux.getDato()]=v

                unacola.insertar(aux.getDato())
            aux = aux.getSig()
    
    print(f"{visitado}")
    print(f"{distancia}")
    print(f"{antesesor}")
    return antesesor
    
    
        def REA(self, v):
            d = np.full(5, math.inf)
            d[v]=0
            unacola = ColaCircular(5)
            unacola.insertar(v)
            while not unacola.vacia():
                v = unacola.suprimir()
                print(f"vertice suprimido:{v}")
                aux = self.__array[v].getcabeza()
                while aux != None:
                    if d[aux.getDato()]==np.inf:
                        d[aux.getDato()]=d[v]+1
                        unacola.insertar(aux.getDato())
                    aux = aux.getSig()
            
            print(f"REA-{d}-")