class peldaño:
    __num:int
    __cadena:str
    
    def __init__(self,num=0, cadena=""):
        self.__num = num
        self.__cadena = cadena
        
    def sumarCadena(self, cadena):
        self.__cadena+=cadena +","
    
    def getPeldaños(self):
        return self.__num
        
    def __str__(self):
        return self.__cadena