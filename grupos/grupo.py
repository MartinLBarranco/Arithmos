"""
    Clase principal de grupos
"""

class Grupo:
    def __init__(self, nombre, operacion, conjunto, cardinal=None):
        self.nombre = nombre
        self.operacion = operacion
        self.conjunto = conjunto
        self.cardinal = cardinal