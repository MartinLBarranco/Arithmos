"""
    Clase para los numeros modulares. 
    valor en lo que vale, y n es lo que indica el Z/Zn
"""

class Zmodulo:
    def __init__(self,valor:int, n:int):
        if not isinstance(n, int):
            raise Exception("Lo que has escrito no es un entero pedazo de imbécil")
        if not isinstance(valor, int):
            raise Exception("Lo que has escrito no es un entero pedazo de imbécil")
        self.valor = valor
        self.n = n
    
    def __repr__(self):
        pass

    def __str__(self):
        pass

    def printLatex(self):
        pass
    
    def __add__(self, otro):
        pass
    
    def __sub__(self, otro):
        pass
    
    def __mul__(self, otro):
        pass
    
    def __truediv__(self, otro):
        pass

    def __pow__(self, otro):
        pass
    
    def __eq__(self, otro):
        pass
    
    def __ne__(self, otro):
        pass
    
    def esCero(self):
        pass

    def factorial(self):
        pass
    
    def factoresPrimos(self):
        pass

    def esPrimo(self):
        pass

    def numDigis(self):
        pass

