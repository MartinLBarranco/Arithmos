from math import gcd

class Rational:
  def __init__(self, num:int, den:int):
    """
    La forma de representar y de parsear fracciones es:
    a/b o simlpemente a donde a y b son enteros. o bien un entero seguido coma y de varios dígitos\n 
    El numerador puede tener un menos para indicar el signo.

    A la hora de instanciar un racional, se deben de cumplir las sigueintes condiciones:\n
    1) El denominador debe de ser distinto de 0 \n
    2) Si se puede simplificar a un entero, entonces se simplifica a un entero
    3) el deniominador debe de ser positivo, para ello, si no lo es, se le cambia el signo a ambos números
    4) se ha de poner siempre como la fracción irreducible. Esto se hace dividiendo num y den por su mcd
    """
    if not isinstance(num, int):
      raise Exception("El numerador debe de ser un entero cacho de tonto.")
    elif not isinstance(den, int):
      raise Exception("El denominador debe de ser un entero, pedazo de mierda.")
    elif den == 0:
      raise Exception("El denominador no puede ser cero pedazo de imbécil.")
    if den < 0:
      num, den = (-1)*num, (-1)*den
    if num % den == 0:
      num, den = num //den, 1
    # ponemos como fracción irreducible
    c = gcd(num,den)
    num, den = num//c, den//c  
    self.num = num
    self.den = den
  
  def __repr__(self):
    if self.den == 1:
      return str(self.num)
    else:
      return str(self.num)+"/"+str(self.den)

  def __str__(self):
    if self.den == 1:
      return str(self.num)
    else:
      return str(self.num)+"/"+str(self.den)

  def printLatex(self):
    """
      Pone el racional listo como para ser escrito en LaTeX
    """
    if self.den == 1:
      return str(self.num)
    else:
      return "frac{" + str(self.num) + "}{" + str(self.den) + "}"
  
  def __abs__(self):
    """
      Valor absoluto del racional
    """
    return Rational(abs(self.num),self.den)
  
  def parteEntera(self):
    """
      Devuleve la parte entera de un Racional.\n es decir si p <= x < p+1 se devuelve p
    """
    if self.den == 1:
      return Rational(self.num, 1)
    a = self.num // self.den
    return Rational(a,1)

  def parteSuperior(self):
    """
      Devueleve la parte entera superior, \n es decir si p < x <= p+1 se devuelve p+1
    """
    if self.den == 1:
      return Rational(self.num, 1)
    a = self.num // self.den
    return Rational(a+1,1)
  
  def __add__(self, n):
    """
      La suma de dos racionales
    """
    if not isinstance(n, Rational):
      raise Exception("Solo se pueden sumar racionales gilipollas")
    a = self.num * n.den + self.den * n.num
    b = self.den * n.den
    return Rational(a,b)
  
  def __sub__(self, n):
    """
      La resta de dos racionales
    """
    if not isinstance(n, Rational):
      raise Exception("Solo se pueden restar racionales gilipollas")
    a = self.num * n.den - self.den * n.num
    b = self.den * n.den
    return Rational(a,b)
  
  def __mul__(self, n):
    """
      La multiplicación de dos racionales
    """
    if not isinstance(n, Rational):
      raise Exception("Solo se pueden multiplicar racionales gilipollas")
    a = self.num * n.num
    b = self.den * n.den
    return Rational(a,b)
  
  def __truediv__(self, n):
    """
      La división de dos racionales
    """
    if not isinstance(n, Rational):
      raise Exception("Solo se pueden cocientar racionales gilipollas")
    # Comprobamos que por el que se divide no es cero
    if n.num == 0:
      raise Exception("Estás dividiendo por 0 soplapollas. ¿No has ido al cole o qué?")
    a = self.num * n.den
    b = self.den * n.num
    return Rational(a,b)
  
  def __mod__(self, n):
    if not isinstance(n, Rational):
      raise Exception("Tienes que meter un racioanl para hacer módulo gilipollas")
    # Comprobamos que n es un entero
    elif n.den != 1:
      raise Exception("Tienes que meter un entero para hacer módulo gilipollas")
    elif self.den != 1:
      raise Exception("Solo se pueden hacer módulos con enteros gilipollas")
    a = self.num % n.num
    return Rational(a,1)
  
  def __pow__(self, n):
    if not isinstance(n, Rational):
      raise Exception("Tienes que meter un racional gilipollas")
    elif n.den != 1:
      raise Exception("Tienes que meter un entero gilipollas")
    a = (self.num)^n.num
    b = (self.den)^n.num
    return Rational(a,b)
  
  def __lt__(self, n):
    if not isinstance(n, Rational):
      raise Exception("Solo se pueden comparar racionales gilipollas")
    return self.num * n.den < self.den * n.num
  
  def __le__(self, n):
    if not isinstance(n, Rational):
      raise Exception("Solo se pueden comparar racionales gilipollas")
    return self.num * n.den <= self.den * n.num
  
  def __eq__(self, n):
    if not isinstance(n, Rational):
      raise Exception("Solo se pueden comparar racionales gilipollas")
    return self.num * n.den == self.den * n.num
  
  def __ne__(self, n):
    if not isinstance(n, Rational):
      raise Exception("Solo se pueden comparar racionales gilipollas")
    return not (self == n)

  def __ge__(self, n):
    if not isinstance(n, Rational):
      raise Exception("Solo se pueden comparar racionales gilipollas")
    return self.num * n.den >= self.den * n.num
  
  def factorial(self):
    if self.den != 1:
      raise Exception("Deberías de saber que el factorial es solo para enteros hijo de puta")
    if self.num == 1 or self.num == 0:
      return Rational(1,1)
    cont = 1
    for i in range(1,self.num +1):
      cont *= i
    return Rational(cont,1)

  def phi(self):
    if self.den != 1:
      raise Exception("Tu abuela sabe que phi es para enteros y tú no, que lo haces con fracciones con la cara de saltamontes que tienes")
    pass
  
  def factores(self):
    """
      Lista de los enteros que dividen al entero dado
    """
    if self.den != 1:
      raise Exception("Te va a factorizar la fracción tu puta madre")
    if self == Rational(1,1):
      return [Rational(1,1)]
    divisores = [Rational(1,1)]
    for i in range(2,int(self.num/2)):
      if self.num % i == 0:
        c = Rational(i,1)
        divisores.append(c)
    divisores.append(Rational(self.num, 1))
    return divisores
  
  def factoresPrimos(self):
    if self.den != 1:
      raise Exception("Eres tan tonto que pensabas que Q era un DFU")
    lista = [elem for elem in self.factores() if elem.esPrimo()]
    return lista

  def esPrimo(self):
    if self.den != 1:
      raise Exception("Tú si que eres primo")
    return len(self.factores()) == 2

  def periodo(self):
    pass

  def lenPeriodo(self):
    pass

  def digitoEnPos(self, n:int):
    if not isinstance(n, int):
      raise Exception("Siempre el mismo fallo capullo.")
    # Caso trivial de que sea un entero
    if self.den == 1:
      return 0
    pass

  def ratio2float(self):
    return self.num / self.den

  def parteDecimal(self):
    return self - self.parteEntera()

  def esEntero(self):
    return self.den == 1

def min(a:Rational,b:Rational):
  if a >= b:
    return b
  else:
      return a 

def max(a:Rational,b:Rational):
  if a >= b:
    return a
  else:
    return b

def mcd(a:Rational,b:Rational):
  if a.num != 1 or b.num != 1:
    raise Exception("Eres más tonto que alguien que no sabe lo que es un DIP")
  c = gcd(a.num, b.num)
  return Rational(c,1)

def mcm(a:Rational,b:Rational):
  if a.num != 1 or b.num != 1:
    raise Exception("Eres más tonto que alguien que no sabe lo que es un DIP")
  c = gcd(a.num, b.num)
  m = (a.num * b.num)//c
  return Rational(m,1)

def bezout(a:Rational, b:Rational):
  pass

def quoRem(a:Rational, b:Rational):
  if a.den != 1 or b.den != 1:
    raise Exception("No se puede hacer division euclidea de dos fracciones parguelas")
  c, r = a.num // b.num, a.num % b.num
  return (Rational(c,1), Rational(r,1))


a = Rational(47,8)
b = Rational(7,2)
print(a+b, a*b, a/b, a-b, a^Rational(4,1), a==b, a<=b)