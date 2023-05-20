"""
    Cosas auxiliares
"""


class Infinito:
    def __repr__(self):
        return "∞"

    def __eq__(self, other):
        return isinstance(other, Infinito)

infi = Infinito()