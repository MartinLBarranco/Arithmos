from grupo import Grupo
from numeros.racionales import Rational
from calculosAuxiliares.infinito import infi 
"""
    Clase para el grupo de los racionales con la suma
"""


class QQ(Grupo):
    def __init__(self):
        Grupo.__init__(self, "Grupo de Números Racionales", "suma", "Numeros Racionales", infi)
        self.conmutativo = True

    def __repr__(self):
        return "(Q, +)"

    def __eq__(self, otro):
        return isinstance(otro, QQ)

    def __ne__(self,otro):
        return not isinstance(otro, QQ)

    def printLatex(self):
        return "\\mathbb\{Q\}"

    def elem(self, num:int, den:int):
        """
            Instancia un número
        """
        if not isinstance(num, int):
            raise Exception("Tienes que meter un entero en el numerador")
        if not isinstance(den, int):
            raise Exception("Tienes que meter un entero en el denominador")
        return Rational(num,den)

    def esElem(self, numero):
        """
            Comprueba que numero sea un Entero
        """
        return isinstance(numero, Rational)

    def orden(self):
        return infi

    def identidad(self):
        return Rational(0,1)
