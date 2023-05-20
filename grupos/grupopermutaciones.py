from subprocess import run
from numeros.permutacion import Permutacion
from grupo import Grupo


class Sn(Grupo):
  def __init__(self,numero:int):
    if not isinstance(numero, int):
      raise Exception("Tienes que meter un entero igual que te metes un pepino en el culo")
    Grupo.__init__(self, "Grupo Simétrico", "Composición de permutaciones", "Conjunto de permutaciones", str(numero)+"!")
    self.n = numero
    self.conmutativo = 5 >= numero
    print(self.cardinal, self.conjunto, self.conmutativo, self.nombre, self.n, self.conmutativo, self.operacion)

  def __repr__(self):
    return "S_{}".format(str(self.n))

  def __eq__(self, other):
    if not isinstance(other, Sn):
      raise Exception("Esto no es un grupo simétrico tonto.")
    return self.n == other.n

  def __ne__(self,other):
    if not isinstance(other, Sn):
      raise Exception("Esto no es un grupo simétrico tonto.")
    return self.n != other.n
  
  def printLatex(self):
    return "S_{}".format(str(self.n))
  
  def elem(self,lista):
    """
      Instancia una permutación. 
    """
    return Permutacion(lista = lista, n = self.n)

  def esElem(self, permu):
    """
      Dada una permutación, dice si están en self.
    """
    if not isinstance(permu, Permutacion):
      return False
    return permu.n == self.n
  
  def orden(self):
    """
      Acceder al archivo con los órdenes de los grupos, que son los factoriales.
    """
    datos = open("../calculosAuxiliares/datos.txt", "w")
    datos.write(str(self.n))
    datos.close()
    run(["./factorial"], cwd="../calculosAuxiliares")
    res = open("../calculosAuxiliares/resultado.txt", "r")
    orden = res.read()
    return int(orden)
    
  def identidad(self):
    return Permutacion([i for i in range(1, self.n + 1)], self.n)
