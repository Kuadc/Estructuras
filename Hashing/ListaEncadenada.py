from Nodo import Nodo

class ListaEncadenada:
    __cab = None

    def __init__(self):
        self.__cab = None

    def insertar(self, x):
        nodo = Nodo(x)
        nodo.setSig(self.__cab)
        self.__cab = nodo

    def buscar(self, num):
        if self.__cab.getDato() == num:
            return True
        else:
            aux = self.__cab
            while aux != None and aux.getDato() != num:
                aux = aux.getSig
            if aux == None:
                return False
            else:
                return True
    
    def buscarClave(self, num):
        cant = self.buscarRe(1,num, self.__cab)
        return cant

    def buscarRe(self,pos,num, aux):
        if aux == None:
            return -1
        if aux.getDato() == num:
            return pos
        else:
            return self.buscarRe(pos + 1, num, aux.getSig())


    def suprimir(self, pos):
        if self.__cab == None:
            return
        else:
            x = self.__cab
            self.__cab = self.__cab.getSig()
        return x

    def mostrar(self):
        aux = self.__cab
        while aux != None:
            print(f"Dato:{aux.getDato()}")
            aux = aux.getSig()





#if __name__ == "__main__":
    





