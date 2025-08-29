import numpy as np

class Pila:
    __cantidad: int
    __tope: int
    __arreglo: np.ndarray

    def __init__(self, cantidad=0):
        self.__cantidad = cantidad
        self.__tope = -1
        self.__arreglo = np.zeros(self.__cantidad, dtype=int)

    def vacia(self):
        return self.__tope == -1
            

    def insertar(self, x):
        if self.__tope < self.__cantidad - 1:
            self.__tope += 1
            self.__arreglo[self.__tope] = x
            return x
        else:
            return 0
        

    def suprimir(self):
        x = 0
        if self.vacia():
            print("Pila vacia")
            return 0
        else:
            x = self.__arreglo[self.__tope]
            self.__tope -=1
            return x

    def mostrar(self,cadena=""):
        i = self.__tope
        if self.vacia()==False:
            print(f"{cadena}")
            while(i>=0):
                print(f"{self.__arreglo[i]}")
                i-=1
        else: print(f"{cadena} Vacia")
                
    def conversor(self,num):
        while num >=2:
            resto = num % 2
            self.insertar(resto)
            num = num//2
        self.insertar(num)
        
    def insertarDiscos(self):
        x = self.__cantidad
        while x >0:
            self.insertar(x)
            x-=1
    
    def confirmar(self,torreOrigen):
        x=0
        if self.vacia():
            print("primera vez que entra esta vacia")
            x= torreOrigen.suprimir()
            self.insertar(x)
            print("Cambio realizado, mostrando estado actual\n")
            
        else:
            print(f"disco actual en torre destino: {self.__arreglo[self.__tope]}")
            x= torreOrigen.suprimir()
            if self.__arreglo[self.__tope] <x:
                torreOrigen.insertar(x)
                print("No se puede realizar este cambio, el tamaño del disco es menor, intente nuevamente")
                
            else:
                self.insertar(x)
                print("Cambio realizado, mostrando estado actual\n")
                
            
        
        
    def moverPieza(self, torreDestino):
            if self.vacia()==False:
                torreDestino.confirmar(self)
                return
            else:
                print("No se puede realizar el movimiento 'Torre origen vacia'")
                return
            

def mostrarEstado(p1,p2,p3):
    p1.mostrar("Estado  torre 1:")
    p2.mostrar("Estado  torre 2:")
    p3.mostrar("Estado  torre 3:")
    
            
def comienzoJuego(p1,p2,p3, torreOrigen, torreDestino):
            torres ={
                1: "torre 1",
                2:"torre 2",
                3:"torre 3"}
            try:
                torres[torreOrigen]
                torres[torreDestino]
        
                if (torreOrigen == 1) and (torreDestino ==2):
                    p1.moverPieza(p2)
                    mostrarEstado(p1,p2,p3)
                    
                elif (torreOrigen == 1) and (torreDestino ==3):
                    p1.moverPieza(p3)
                    mostrarEstado(p1,p2,p3)
                    
                #torre 2 con destino 1 o 3
                elif (torreOrigen == 2) and (torreDestino ==1):
                    p2.moverPieza(p1)
                    mostrarEstado(p1,p2,p3)
                    
                elif (torreOrigen == 2) and (torreDestino ==3): 
                    p2.moverPieza(p3)
                    mostrarEstado(p1,p2,p3)
                    
                #Torre 3 con destino 1 o 2
                elif (torreOrigen == 3) and (torreDestino ==1):
                    p3.moverPieza(p1)
                    mostrarEstado(p1,p2,p3)
                    
                elif (torreOrigen == 3) and (torreDestino ==2):
                    p3.moverPieza(p2)
                    mostrarEstado(p1,p2,p3)
                    
            except KeyError:
                print("\n-------------------------------")
                print("Torre invalida intene nuevamente")
                print("-------------------------------\n")
        
        
        

if __name__ == "__main__":
    #unapila = Pila(10)
    #unapila.conversor(8)
    #unapila.mostrar()
    discos = int(input("Ingrese la cantidad de discos: "))
    
    p1 = Pila(discos)
    p1.insertarDiscos()
    
    p2 = Pila(discos)
    p3 = Pila(discos)
    
    p1.mostrar("Estado inicial torre 1")
    p2.mostrar("Estado inicial torre 2")
    p3.mostrar("Estado inicial torre 3")
    
    
    #comienzo del juego, tomar 2 numeros del usuario
    print("----------COMIENZA EL JUEGO-----------\n")
    
    bandera = True
    while bandera:
        to= int(input("Ingrese numero de la torre origen :"))
        td= int(input("\nIngrese numero de la torre destino:"))
        comienzoJuego(p1,p2, p3,to,td)
    
    
    
    