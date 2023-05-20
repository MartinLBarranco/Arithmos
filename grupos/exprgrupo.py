"""
    Parámetros:
        -nombre: string. es el nombre que representa al simbolo
        -expo: int. Indica si está elevado a algún exponente
    El elemento neutro se denota como "e".
"""
class SimbGrupo:
    """
    Parámetros:
        -nombre: string. es el nombre que representa al simbolo
        -expo: int. Indica si está elevado a algún exponente
    El elemento neutro se denota como "e".
"""
    def __init__(self,nombre:str, expo = 1):
        if not isinstance(nombre, str):
            print(nombre, type(nombre))
            raise Exception("Cagaste wey")
        elif not isinstance(expo, int):
            raise Exception("Cagaste wey int")
        if expo == 0:
            self.nombre = "e"
            self.expo = 1
        elif nombre == "e":
            self.nombre = "e"
            self.expo = 1
        else:
            self.nombre = nombre
            self.expo = expo

    def __eq__(self, otro):
        if not isinstance(otro, SimbGrupo):
            raise Exception("Tienes que meter un simbolo de grupo")
        return self.nombre == otro.nombre and self.exp == otro.exp

    def __ne__(self, otro):
        if not isinstance(otro, SimbGrupo):
            raise Exception("Tienes que meter un símbolo de grupo")
        return self.nombre != otro.nombre or self.exp != otro.exp

    def __repr__(self):
        if self.expo == 1: 
            return self.nombre
        elif self.expo == 0:
            return "e"
        elif self.expo > 1:
            return self.nombre+"^{}".format(str(self.expo))
        else:
            return self.nombre+"^({})".format(str(self.expo))
    
    def printLatex(self):
        if self.exp == 1: 
            return self.nombre
        elif self.exp == 0:
            return "e"
        elif self.exp > 1:
            return self.nombre+"^"+str(self.exp)
        else:
            return self.nombre+"^{-"+str(abs(self.exp))+"}"
    
    def esNeutro(self):
        return self.nombre == "e"

class ExprGrupo:
    """
        Representa la expresión de una palabra de un grupos arbitrario.
        No se asume que pertenezca a ningún grupo, así que solo aplica las reglas básicas de los grupos.
        Una expresion es asímismo un símbolo
    
        Parámetros:
            -lista: list[SimboloGrupo]: Es el producto de los símbolos que aparecen en la palabra
        Atributos:
            - lista: es la lista de las expresiones
            - simbolos: La lista de los nombres de los simbolos. Es decir una lista de strings
        Métodos:
            -eliminaNeutros :               Elimina todos los elementos neutros
            -juntaMismoSimbolo :            Junta e un mismo simbolo la secuencia de los mismos simbolos que esté en la posición posicion-ésima con su exponente correspondiente.
                                            Si es posicion == 0, los hace con todos los exponentes sean positivos o negativos. Si resultan en el elemento neutro NO LO ELIMINA.
                                            Si no hay secuencia posicion-ésima, la deja igual.
                                            Ejemplo:
                                                abbbabb -> juntaMismoSimbolo("b") = ab^3abb
                                                abbbabb -> juntaMismoSimbolo("b", 1) = ab^3abb
                                                abbbabb -> juntaMismoSimbolo("b", 1) = abbbab^2
                                                abbbabb -> juntaMismoSimbolo("a") = abbbabb 
            -desarrollaExponenteGrande :    Si toda la expresion está elevada a un numero, se desarrolla hasta que éste sea 1
    """
    def __init__(self, lista, nombre:str = None, exponente:int = 1):
        if not isinstance(nombre, str):
            raise Exception("Tienes que meter un nombre imbécil.")
        if nombre == "e":
            raise Exception("No hagas esto por favor te lo pido")
        if not all(isinstance(elem, SimbGrupo) for elem in lista):
            raise Exception("Tienes que meter cosas que sean de grupos imbecil.")
        self.simbolos = list(set([elem.nombre for elem in lista]))
        self.lista = lista
        self.expo = exponente
        self.nombre = nombre
        if self.expo == 0:
            self.simbolos = ["e"]
            self.lista = [SimbGrupo("e")]
            self.expo = 1
            self.nombre = nombre

    def __repr__(self) -> str:
        res = ""
        for elem in self.lista:
            res += str(elem)
        # Hay que mdoificar esto para que meta los expoenetnes de toda la expresion
        if self.expo > 1:
            res = "(" + res + ")^"+str(self.expo)
        return self.nombre + " := " + res

    def __add__(self, otro):
        """
            Compone la expresión con otro con la operacion del grupo
        """
        if not isinstance(otro, ExprGrupo):
            raise Exception("Mira que eres tonto del culo.")
        pass

    def __sub__(self, otro):
        """
            Compone la expresión con el inverso de otro con la operacion del grupo
        """
        if not isinstance(otro, ExprGrupo):
            raise Exception("Mira que eres tonto del culo.")
        pass

    def __pow__(self, n:int):
        """
            Hace la potencia de si misma n veces
        """
        if not isinstance(n, int):
            raise Exception("Mira que eres tonto del culo.")
        pass

    def printLatex(self):
        # Hay que mdoificar esto para que meta los expoenetnes de toda la expresion
        res = ""
        for elem in self.lista:
            res += elem.printLatex()
        return self.nombre + " \coloneq " + res

    def eliminaNeutros(self):
        """
            elimina todos los elementos neutros de la expresión
        """
        res = list(filter(lambda x: not x.esNeutro(), self.lista))
        return ExprGrupo(res)

    def juntaMismoSimbolo(simbolo:str, posicion:int = 0):
        """
            Junta e un mismo simbolo la secuencia de los mismos simbolos que esté en la posición posicion-ésima con su exponente correspondiente.
            Si es posicion == 0, los hace con todos los exponentes sean positivos o negativos. Si resultan en el elemento neutro NO LO ELIMINA.
            Si no hay secuencia posicion-ésima, la deja igual.
            Ejemplo:
                abbbabb -> juntaMismoSimbolo("b") = ab^3abb
                abbbabb -> juntaMismoSimbolo("b", 1) = ab^3abb
                abbbabb -> juntaMismoSimbolo("b", 1) = abbbab^2
                abbbabb -> juntaMismoSimbolo("a") = abbbabb 
        """
        pass

    def desarrollaExponenteGrande(self):
        """
            Si toda la expresion está elevada a un numero, se desarrolla hasta que éste sea 1
        """
        pass


"""
FALTA HACER EXPRESIONES COMPUESTAS
"""

a = SimbGrupo("a", 0)
b = SimbGrupo("a", 1)
c = SimbGrupo("a", 2)
d = SimbGrupo("a", -3)
l = [a,b,c,d,d,d,d,d,a,a,a,a,b,b,b,b,b,b]
for e in l:
    print(e.esNeutro())
print("\n")
expresion = ExprGrupo(l,"esperma",4)
print(expresion)