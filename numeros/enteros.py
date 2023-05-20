from math import gcd, lcm, comb

def esPrimito(n:int):
  # comprobar si un numero positivo mayor estricto que 1 es primo
  if n == 2:
    return True
  if n % 2 == 0:
    return False
  for i in range(2, n//2):
    if n % i == 0:
      return False
  return True

class Entero:
    def __init__(self,n:int):
        if not isinstance(n, int):
            raise Exception("Lo que has escrito no es un entero pedazo de imbécil")
        self.signo = n <= 0
        self.valorAbs = abs(n)
        self.n = n
    
    def __repr__(self):
        return str(self.n)

    def __str__(self):
        return str(self.n)

    def printLatex(self):
        return str(self.n)
    
    def __abs__(self):
        return Entero(abs(self.n)) 
    
    def __add__(self, otro):
        if not isinstance(otro, int):
            raise Exception("Lo que has metido no es un Entero gilipollas.")
        return Entero(self.n+otro.n)
    
    def __sub__(self, otro):
        if not isinstance(otro, int):
            raise Exception("Lo que has metido no es un Entero gilipollas.")
        return Entero(self.n-otro.n)
    
    def __mul__(self, otro):
        if not isinstance(otro, int):
            raise Exception("Lo que has metido no es un Entero gilipollas.")
        return Entero(self.n-otro.n)
    
    def __truediv__(self, otro):
        if not isinstance(otro, int):
            raise Exception("Lo que has metido no es un Entero gilipollas.")
        return (Entero(self.n // otro.n), Entero(self.n % otro.n))
    
    def __mod__(self, otro):
        if not isinstance(otro, int):
            raise Exception("Lo que has metido no es un Entero gilipollas.")
        return Entero(self.n % otro.n)
    
    def __pow__(self, otro):
        if not isinstance(otro, int):
            raise Exception("Lo que has metido no es un Entero gilipollas.")
        if otro.n < 0:
            raise Exception("La potencia tiene que ser positiva capullo.")
        return Entero(self.n**otro.n)
    
    def __lt__(self, otro):
        if not isinstance(otro, int):
            raise Exception("Lo que has metido no es un Entero gilipollas.")
        if otro.n < 0:
            raise Exception("La potencia tiene que ser positiva capullo.")
        return self.n < otro.n
    
    def __le__(self, otro):
        if not isinstance(otro, int):
            raise Exception("Lo que has metido no es un Entero gilipollas.")
        if otro.n < 0:
            raise Exception("La potencia tiene que ser positiva capullo.")
        return self.n <= otro.n
    
    def __eq__(self, otro):
        if not isinstance(otro, int):
            raise Exception("Lo que has metido no es un Entero gilipollas.")
        if otro.n < 0:
            raise Exception("La potencia tiene que ser positiva capullo.")
        return self.n == otro.n
    
    def __ne__(self, otro):
        if not isinstance(otro, int):
            raise Exception("Lo que has metido no es un Entero gilipollas.")
        if otro.n < 0:
            raise Exception("La potencia tiene que ser positiva capullo.")
        return self.n != otro.n

    def __ge__(self, otro):
        if not isinstance(otro, int):
            raise Exception("Lo que has metido no es un Entero gilipollas.")
        if otro.n < 0:
            raise Exception("La potencia tiene que ser positiva capullo.")
        return self.n >= otro.n
    
    def esCero(self):
        return self.n == 0

    def factorial(self):
        res = 1
        for i in range(1, (self.n)+1):
            res *= i
        return Entero(res)

    def phi(self):
        pass
    
    def factores(self):
        factores = [Entero(1)]
        for i in range(1, (self.n)//2):
            if self.n % i == 0:
                factores.append(Entero(i))
        factores.append(self)
        return factores
    
    def factoresPrimos(self):
        res = []
        for elem in self.factores():
            if elem.esPrimo():
                res.append(elem)
        return res

    def esPrimo(self):
        if self.n == 2:
            return True
        if self.n % 2 == 0:
            return False
        for i in range(2, (self.n)//2):
            if self.n % i == 0:
                return False
        return True

    def valoracionpadica(self, p:int):
        if not esPrimito(p):
            raise Exception("El numero que metes tiene que ser primo")
        if self.esCero():
            raise Exception("La valoración p-ádica de 0 es infinito")
        k = 0
        while self.n % (p**k) == 0:
            k += 1
        return k

    def cambiaBase(self, n:int):
        """
            Devuelve la lista con los dígitos en clase Entero del número pero en otra base
        """
        if not isinstance(n, int):
            raise Exception("La base tiene que ser un entero so tonto.")
        if n <= 1:
            raise Exception("La base tiene que ser mayor o igual a 2.")
        res = []
        b = self.n
        while b != 0:
            b, digito = b // n, b % n
            res.append(Entero(digito))
        res = res[::-1]
        return res

    def numDigis(self):
        if self.n < 0:
            return len(str(self.n)) - 1
        else:
            return len(str(self.n))


def min(a,b):
    if (not isinstance(a,Entero)) or (not isinstance(b,Entero)):
        raise Exception("Tienes que meter enteros sopla pollas.")
    return Entero(min(a.n, b.n))

def max(a,b):
    if (not isinstance(a,Entero)) or (not isinstance(b,Entero)):
        raise Exception("Tienes que meter enteros sopla pollas.")
    return Entero(max(a.n, b.n))

def mcd(a,b):
    if (not isinstance(a,Entero)) or (not isinstance(b,Entero)):
        raise Exception("Tienes que meter enteros sopla pollas.")
    return Entero(gcd(a.n, b.n))

def mcm(a,b):
    if (not isinstance(a,Entero)) or (not isinstance(b,Entero)):
        raise Exception("Tienes que meter enteros sopla pollas.")
    return Entero(lcm(a.n, b.n))

def bezout(a,b):
    pass

def combinacion(a,b):
    if (not isinstance(a,Entero)) or (not isinstance(b,Entero)):
        raise Exception("Tienes que meter enteros sopla pollas.")
    return Entero(comb(a.n, b.n))