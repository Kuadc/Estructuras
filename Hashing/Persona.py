class Persona:
    __numero:int
    __nombre:str

    def __init__(self, num, nom):
        self.__nombre = nom
        self.__numero = num

    def getNom(self):
        return self.__nombre

    def getNum(self):
        return self.__numero