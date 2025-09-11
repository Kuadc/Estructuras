class Nodo:
    
    __sig : None
    __item : None

    #cargardato 
    def __init__(self,dato):
        self.__dato = dato
        self.__sig = None

    def setSig(self, nodo):
        self.__sig = nodo

#obtener siguiente
    def getSig(self):
        return self.__sig  

    def getDato(self):
        return self.__dato
 
class PilaEnca:
  __cant : int
  __cabeza : None

  def __init__(self,cant=0):
     self.__cant = cant
     self.__cabeza = None  

  def insertar(self, item):

       unNodo = Nodo(item)
       unNodo.setSig(self.__cabeza)
       self.__cabeza = unNodo
       self.__cant+=1

  def mostrar(self):

    aux = self.__cabeza

    while aux != None:
       print(f"\n Items = {aux.getDato()}")
       aux = aux.getSig()    

if __name__ == "__main__":

     Pila = PilaEnca()

     Pila.insertar(4)
     Pila.insertar(5)
     Pila.insertar(6)
     Pila.mostrar()



#IMPLEMENTACION TERMINADA





     

 



