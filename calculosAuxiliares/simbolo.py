"""
    Clase para el manejo de símbolo arbitrario. NO SE SI SE VA A USAR PERO POR SI ACASO.
"""

class Simbolo:
  def __init__(self,nombre:str, valor:float = None):
    if valor is not None:
      valor = float(valor)
    self.nombre = nombre
    self.valor = valor

  def __eq__(self, otro):
    if not isinstance(otro, Simbolo):
      raise Exception("Tienes que comparar símbolos")
    otro_es_none = otro.valor == None
    self_es_none = self.valor == None
    if otro_es_none and self_es_none:
      return self.nombre == otro.nombre
    else:
      return self.nombre == otro.nombre

  def __ne__(self, otro):
    if not isinstance(otro, Simbolo):
      raise Exception("Tienes que comparar símbolos")
    return not (self == otro)

  def __repr__(self):
    if self.valor is None:
      return self.nombre
    else:
      return str(self.valor)
  
  def sustituye(self, valor:float):
    if not isinstance(valor, float):
      valor = float(valor)
    return Simbolo(self.nombre, valor)