"""
Consideramos Sn
Para listar todos los posibles elementos o todos los posibles factoriales,
se dispondrán de un .txt en el que la línea n-ésima contendrá n! que se irán calculando externamente vía haskell
Ademas de otro .txt listando todas las posibles permutaciones de cada Sn.
Así solo que hay que hacer lecturas y no cálculos
Covendría tener los primeros 100 factoriales
y todas sus posibles permutaciones.
Un único elemento de Sn
    corresponde con:
    (   1    2    3    4   ...   n   )
    (  s(1) s(2) s(3) s(4) ...  s(n) )
  Se introdice como p = Permutacion(lista=[s(1),s(2),s(3),s(4),...s(n)], n)  Como permutación directamente. Tiene que especificarse donde va TODO ELMUNO
  o bien como p = Permutacion(lista=[[a1, a2, a3...],[b1,b2,b3...]], n)      Como producto de transposiciones DISJUNTAS que se representan como lista de listas
"""
class Permutacion:

  def __init__(self,lista:list, n:int):
    """
      Se ha de almacenar como un diccionario. Esto se debe a como se va a trabajar con cada permutación.
    """
    # Comprobamos los tipos
    if not isinstance(lista, list) or not isinstance(n, int):
      raise Exception("Paso ya de todo...")
    if n <= 0:
      raise Exception("El orden del grupo debe ser mayor o igual a 1 capullo.")
    self.n = n
    #Caso de que sea una lista completa
    if esListaCompleta(lista, self.n):
      self.dict = {i:lista[i-1] for i in range(1, len(lista)+1)}
      self.orden = None
      self.signo = (-1)**self.numTransposiciones
      self.numTransposiciones = None
      self.numCiclos = None
    #Caso de ciclos disjuntos
    elif esprodCiclos(lista, self.n):
      self.dict = {i:lista[i-1] for i in range(1, len(lista)+1)}
      self.orden = None
      self.signo = (-1)**self.numTransposiciones
      self.numTransposiciones = None
      self.numCiclos = None
    else:
      raise Exception("Lo que has metido no es una permutación.")

  def __repr__(self):
    return str([i for i in self.dict.values()])
  
  def __eq__(self, other):
    if not isinstance(other, Permutacion):
      raise Exception("Te equivocas más con los tipos que en la vida.")
    if self.n != other.n:
      return False
    for i in range(1, len(self.dict) + 1):
      if self.dict[i] != other.dict[i]:
        return False
    return True

  def __ne__(self, other):
    if not isinstance(other, Permutacion):
      raise Exception("Te equivocas más con los tipos que en la vida.")
    return not self == other

  def __add__(self, other):
    """
      Se corresponde con la composición de permutaciones
    """
    if not isinstance(other, Permutacion):
      raise Exception("Te equivocas más con los tipos que en la vida.")
    if self.n != other.n:
      raise Exception("Tu puta madre.")
    lista = [i for i in range(1, self.n + 1)]
    res = [self.dict[other.dict[i]] for i in lista]
    return Permutacion(res, self.n)
  
  def __pow__(self, other:int):
    if not isinstance(other, int):
      raise Exception("Te equivocas más con los tipos que en la vida.")
    if other < 0:
      raise Exception("Solo se pueden poner potencias positivas.")
    if other == 1:
      return self
    if other == 0:
      return Permutacion([i for i in range(1, self.n + 1)], self.n)
    res = self
    for i in range(1,other):
      res = res + self
    return res
    
  def printPermuCompleta(self):
    """
    Se escribe esto:
      (   1    2    3    4   ...   n   )
      (  s(1) s(2) s(3) s(4) ...  s(n) )
    """
    pass

  def printMatrizLatex(self):
    """
      Como self.printPermuCompleta pero en formato de latex
    """
    lista_elementos = list(self.dict.values())
    n = len(lista_elementos)
    
    codigo_latex = "\\begin{matrix}\n"
    
    # Agregar la primera fila
    codigo_latex += " & ".join(str(i) for i in range(1, n+1))
    codigo_latex += "\\\\\n"
    
    # Agregar la segunda fila
    codigo_latex += " & ".join(str(num) for num in lista_elementos)
    codigo_latex += "\n\\end{matrix}"
    
    return codigo_latex

  def printCiclosDisjuntosLatex(self):
    """
      Se escribe como producto de ciclos disjuntos:
        (a1, a2, a3...),(b1,b2,b3...)
    """
    pass
  
  def inversa(self):
    """
      Halla la inversa de una permutación
    """
    claves = self.dict.keys()
    values = self.dict.values()
    res = dict(zip(values,claves))
    res = dict(sorted(res.items()))
    res = list(res.values())
    return Permutacion(res, self.n)
  
  def img(self, n:int):
    """
      Dice a dónde va el numero n
    """
    if n <= 0 or n > self.n or not isinstance(n, int):
      raise Exception("Indice del numero fuera del rango o la cagaste con el tipo.")
    return self.dict[n]

def esListaCompleta(lista, n):
  return len(lista) == n and all(isinstance(elem,int) and 1<=elem and elem<=n and lista.count(elem)==1 for elem in lista)

def esprodCiclos(listalista, n):
  # Comprobamos que la suma de las longitudes son menores que n y que las longitudes de cada uno son mayores que 2
  if not all(isinstance(elem, list) for elem in listalista) or not sum([len(elem) for elem in listalista]) <= n or not all(len(elem) >= 2 for elem in listalista):
    return False
  # Comprobamos que cada numero solo aparece 0 o 1 vez
  union_listas = []
  for elem in listalista:
    union_listas = union_listas + elem
  for i in range(1,n+1):
    if union_listas.count(i) > 1:
      return False
  # Comprobamos que todos los elementos estan entre 1 y n
  if not all(i in range(1,n+1) for i in union_listas):
    return False
  # Comprobamos que son disjuntos dos a dos
  conjuntos = [set(elem) for elem in listalista]
  for i in range(len(conjuntos)):
    for j in range(i+1, len(conjuntos)):
      if set() != conjuntos[i].intersection(conjuntos[j]):
        return False
  return True
