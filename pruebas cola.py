
from Nodo import Nodo
import numpy as np

class Cola:
	__pr:None
	__ul:None
	__cant:int


	def __init__(self):
		self.__pr = None
		self.__ul = None
		self.__cant = 0

	def insertar(self, x):
		unnodo = Nodo(x)
		if self.__pr == None:
			self.__pr = unnodo
		else:
			self.__ul.setSig(unnodo)
		self.__ul = unnodo
		self.__cant+=1

	def suprimir(self):
		if self.vacia():
			print("cola vacia")
		else:
			x = self.__pr.getDato()
			self.__pr = self.__pr.getSig()
			self.__cant-=1
			return x

	def vacia(self):
		return self.__cant == 0
			
	def mostrar(self):
		i=self.__pr
		while i<self.__ul+1:
			print(f"{self.__arre[i]}")
			i+=1

	def mostrar2(self):
		aux = self.__pr
		while aux != None:
			print(f"{aux.getDato()}")
			aux = aux.getSig()

if __name__ == "__main__":

    pi = Cola()
    pi.insertar(5)
    pi.insertar(4)
    pi.insertar(3)
    pi.insertar(2)
    pi.insertar(1)
    pi.mostrar2()
    print("listo")
    pi.suprimir()
    pi.mostrar2()
	
  