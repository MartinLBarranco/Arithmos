from grupo import Grupo
from numeros.enteros import Entero
from calculosAuxiliares.infinito import infi
"""
    Clase para el grupo de Z con la suma
"""


class ZZ(Grupo):
    def __init__(self):
        Grupo.__init__(self, "Grupo de Números Enteros", "suma", "Numeros Enteros", infi)
        self.conmutativo = True

    def __repr__(self):
        return "(Z, +)"

    def __eq__(self, otro):
        return isinstance(otro, ZZ)

    def __ne__(self,otro):
        return not isinstance(otro, ZZ)

    def printLatex(self):
        return "\\mathbb\{Z\}"

    def elem(self, numero:int):
        """
            Instancia un número
        """
        if not isinstance(numero, int):
            raise Exception("Tienes que meter un entero")
        return Entero(numero)

    def esElem(self, numero):
        """
            Comprueba que numero sea un Entero
        """
        return isinstance(numero, Entero)

    def orden(self):
        return infi

    def identidad(self):
        return Entero(0)