from collections import Counter
from Nodo import NodoArbol

cadena ="abracadabra"
cantidad = Counter(cadena)
lista=[]
for clave, valor in cantidad.items():
    lista.append((clave,valor))

orden = sorted(lista, key=lambda x: x[1])
print(f"{orden}")

nodo1= NodoArbol(lista[0])
nodo2= NodoArbol(lista[1])










