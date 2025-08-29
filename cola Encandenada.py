class Nodo:
    
    __sig : None
    __item :int

    def __init__(self,dato):
         self.__dato = dato
         self.__sig = None
    
    def setSig(self, sig):
         self.__sig = sig
         
    def cargarsig(self, nodo):
         self.__sig = nodo
    
    def getSig(self):
         return self.__sig  
    
    def getDato(self):
        return self.__dato
 
class colaEnca:
    
    __cantidad: int
    __pr = None
    __ul = None
    
    def __init__(self, cantidad=0):
        self.__cantidad = cantidad
        self.__pr = None
        self.__ul = None

    def insertar(self, item):
        
         unNodo = Nodo(item)
         #self.__cabeza = unNodo
         if(self.__ul ==None):
             self.__pr = unNodo
         else:
             self.__ul.setSig(unNodo)
         self.__ul = unNodo     
         self.__cantidad +=1
         return self.__ul.getDato()
             
    def vacia(self):
        return self.__cantidad == 0
    def suprimir(self):
         x = 0
         if self.vacia():
             print("La cola esta vacia")
         else:
             x = self.__pr.getDato()
             self.__pr = self.__pr.getSig()
             self.__cantidad -=1
             if self.__pr == None:
                 self.__ul = None
             return x
         
    def recuperarPrimero(self):
        return self.__pr

    def mostrar(self):
        aux = self.__pr
        while aux != None:
               print(f"\n Item = {aux.getDato()}")
               aux = aux.getSig()    

if __name__ == "__main__":
    
    co = colaEnca()
    co.insertar(3)
    co.insertar(5)
    co.mostrar()
    print("Suprimienod numero")
    co.suprimir()
    co.mostrar()







"""INSERTAR: La primera vez que ingresa el insertar agrega un nodo, y como ul tiene NUll entra al primer if, luego
sale y agrega a ul el primer nodo y suma. luego en el segundo nodo, el que camina y enlaza es ul"""

     

 



