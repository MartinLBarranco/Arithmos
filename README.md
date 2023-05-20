# DOCUMENTACIÓN  🚧 🏗️ 🛠️

# Números

Es posible trabajar con los números más frecuentes de las matemáticas, ciencias varias e ingenierías varias. Estos los usa el usuario y además lo usan los grupos y anillos.

### Racionales:

Los racionales está creados por la siguiente clase:

```python
class Rational(num:int, den:int)
```

Es posible hacer las operaciones habituales sobre ellos: suma, resta, multiplicación, potencia por un entero de clase Rational, y operaciones de comparación y módulo si los números involucrados son enteros.

```python
a = Rational(47,8)
b = Rational(7,2)
print(a+b, a*b, a/b, a-b, a^Rational(4,1), a==b, a<=b)
```

La clase contiene los siguientes atributos:

- self.num: Denominador de la fracción.
- self.den: Es el denominador de la fracción.

La clase contiene los siguientes métodos:

- self.factorial(): En caso de que coincida con un entero, da el factorial del mismo.
- self.phi(): En caso de que coincida con un entero, da la función $\phi$ de Euler.
- self.factores(): En caso de que coincida con un entero, da los factores del mismo.
- self.factoresPrimos():En caso de que coincida con un entero, da los factores primos del mismo.
- self.esPrimo(): En caso de que coincida con un entero, dice si es primo
- self.periodo(): Da el periodo de una fracción.
- self.lenPeriodo(): Da la longitud del periodo.
- self.digitoEnPos(n:int): Da el dígito de la fracción base 10 en la posición n-ésima.
- self.ratio2float(): Da una aproximación del número como float de Python.
- self.parteDecimal(): Da la parte decimal de una fracción
- self.esEntero(): Dice si el número es un entero.
- self.__abs__(): Da el valor absoluto.
- self.parteEntera(): Da la parte entera de un número.
- self.parteSuperior(): Da la función techo de un número.
- self.printLatex(): Escribe el número lista para Látex.

Se dispone además de las siguientes funciones que toman siempre entradas de la clase Rationals:

- min(a,b): El mínimo de dos racionales
- max(a,b): El máximo de dos racionales
- mcd(a,b): El mcd de dos racionales si son enteros
- mcm(a,b):  El mcm de dos racionales si son enteros
- bezout(a,b):  Si a y b son enteros, devuelve la terna (d, f,g) donde d es el mcd y f g los coeficientes de la identidad de Bezout.
- quoRem(a,b): Si son enteros a y b, se da el cociente y resto de la división euclidiana.

### Enteros.

Los racionales está creados por la siguiente clase:

```python
class Entero(n:int)
```

Es posible hacer las operaciones habituales sobre ellos: suma, resta, multiplicación, potencia y operaciones de comparación y módulo.

La clase contiene los siguientes atributos:

- self.n: Es el valor propiamente dicho.
- self.valorAbs: Es el valor absoluto.
- self.signo: Es False si en menor o igual a cero, True en caso contrario.

La clase contiene los siguientes métodos:

- self.factorial(): Da el factorial del mismo.
- self.phi(): Da la función $\phi$ de Euler.
- self.factores(): Da los factores del mismo.
- self.factoresPrimos(): Da los factores primos del mismo.
- self.esPrimo(): Dice si es primo
- self.__abs__(): Da el valor absoluto.
- self.printLatex(): Escribe el número lista para Látex.
- self.cambiaBase(n:int): Devuelve una lista de Entero con los dígitos del numero pero en base n
- self.valoracionpadica(p:int): Dado un primo p, se da la valoración p-ádica del número.
- self.numDigis(): Da la cantidad de dígitos del numero

Se dispone además de las siguientes funciones que toman siempre entradas de la clase Rationals:

- min(a,b): El mínimo de dos Entero
- max(a,b): El máximo de dos Entero
- mcd(a,b): El mcd de dos Entero
- mcm(a,b):  El mcm de dos Entero
- bezout(a,b):  Devuelve la terna (d, f,g) donde d es el mcd y f g los coeficientes de la identidad de Bezout.
- combinacion(a,b): Da el cociente y resto de la división euclidiana.

### Permutación

Clase para trabajar con las permutaciones.

```python
class Permutacion(lista, n)
```

Donde n indica qué grupo simétrico estamos trabajando y lisa puede ser una de estas dos cosas:

- Lista de enteros entre 1 y n: indica que el elemento i va al i-ésimo elemento de la lista
- Lista de lista: cada sublista es un ciclo. Se expresa la lista como producto de ciclos disjuntos.

Al igual que Enteros y Rationals, es posible componer (mediante la suma en Python), hacer igualdad, desigualdad, potencia por un entero:

 Dispone de los siguientes atributos

- self.n: la dimensión
- self.lista: el diccionario indicando a donde va cada uno
- self.orden: el orden de la permutacion
- self.signo: el signo de la permutacion
- self.numTransposiciones: el numero de transposiciones en las que se descompone la permutacion
- self.numCiclos: numero de ciclos disjuntos en los que se factoriza la permutacion

Se dispone de los siguientes métodos:

- self.printPermuCompleta(): hace un ascii art de la permu como matriz
- self.printMatrizLatex(): La matriz de la permu en forma de Latex
- self.ciclosDisjuntosLatex(): La matriz como producto de ciclos disjuntos en formato de látex
- self.inversa(): La inversa de la permutación.

### Enteros modulares

Corresponden a los elementos de $\mathbb{Z}/\mathbb{Z}n$

```python
class Zmodulo(valor:int, n:int)
```

Valor es el valor intrínseco, n es un entero positivo. distinto de 0 y 1.

🚧 🏗️ 🛠️

# TEORÍA DE GRUPOS

Todos los grupos heredan de la clase Grupo:

```python
class Grupo(nombre, operacion, conjunto, cardinal)
```

Donde nombre es su nombre, operacion es la operación, conjunto es el conjunto de definicion, y cardinal es el cardinal de conjunto. Esta clase a priori no la toca el usuario; es estrictamente estructural.

### Grupo Trivial

🚧 🏗️ 🛠️

Aparece cuando se le crea un grupo que depende de un parámetro que lo trivializa, como cocientar $\mathbb{Z}$  sobre 1

Solo tiene un elemento.

### Grupo simétrico

```python
class Sn(numero)
```

numero indica qué numero es el grupo simétrico.

Se puede comprar. Dispone de los siguientes atributos:

- self.nombre: “Grupo Simétrico”
- self.operacion: “Composición”
- self.conjunto: “Permutaciones de permutaciones”
- self.cardinal: numero!
- self.n: numero
- self.conmutativo: False si numero ≥ 5

Dispone de los siguientes métodos:

- self.printLatex(): “S_n”
- self.elem(lista): Devuelve la clase permutacion: Permutacion(lista,n)
- self.esElem(cosa): dice si la cosa es una permutacion
- self.orden(): Da n!
- self.identidad(): Da el elemento identidad del grupo.

### Enteros con la suma

```python
class ZZ()
```

numero indica qué numero es el grupo simétrico.

Se puede comprar. Dispone de los siguientes atributos:

- self.nombre: “Grupo de Números Enteros”
- self.operacion: “suma”
- self.conjunto: “Números Enteros”
- self.cardinal: infinito
- self.conmutativo: True

Dispone de los siguientes métodos:

- self.printLatex(): “\mathbb{Z}”
- self.elem(numero): Devuelve la clase Entero: Entero(numero)
- self.esElem(cosa): dice si la cosa es un Entero
- self.orden(): Da infinito
- self.identidad(): Da Entero(0)

### Racionales con la suma

```python
class QQ()
```

numero indica qué numero es el grupo simétrico.

Se puede comprar. Dispone de los siguientes atributos:

- self.nombre: “Grupo de Números Racionales”
- self.operacion: “suma”
- self.conjunto: “Números Racionales”
- self.cardinal: infinito
- self.conmutativo: True

Dispone de los siguientes métodos:

- self.printLatex(): “\mathbb{Q}”
- self.elem(numerador, denominador): Devuelve la clase Rational: Rational(numerador, denominador)
- self.esElem(cosa): dice si la cosa es un Rational
- self.orden(): Da infinito
- self.identidad(): Da Entero(0)

### Enteros modulares

🚧 🏗️ 🛠️

Si se mete 0 devuelve el grupo Z con la suma

# Lógica Preposicional ( 📁logic/propositions)

Nota: He seguido el libro “Mathematical Logic through Python.”

### class Formula(root:string, first:Optional[Formula], second:Optional[Formula])

Tiene los siguientes atributos:

- root: es el operador (~, &, | ) o bien es un valor de verdad (T, F) o una variable ([p, q, r, … z, seguido de los números que se quiera)
- first: En caso de que root sea la negación, first es la formula que niega o el primer argumento en caso de ser binario
- second: es el segundo argumento de la operación en caso de ser binario

La clase tiene los siguientes métodos útiles (tiene más pero espero no usarlos):

- variables: Da el conjunto de las variables de la formula
- operators: Da el conjunto de los operadores que se están usando
- substitute_variables(substitution_map: Mapping[str, Formula]): sustituye en cada ocurrencia de las variables que aparecen en el diccionario por las formulas correspondientes del diccionario en la fórmula dada.
- substitute_operators(substitution_map: Mapping[str, Formula]): Ídem pero con operadores
- parse(str:string): Parsea una formula suponiendo que esté bien escrita.

De cara al aspecto semántico, podemos halar el nuevo tipo: Model = Mapping[str, bool]. Encontramos las siguientes funciones:

- is_model(model:Model): comprueba si el diccionario es un modelo
- variables(model:Model): Devuelve la lista de las variables dentro del modelo
- evaluate(formula:Formula, model:Model): Evalúa la formula sobre el modelo dado.
- all_models(variables:Sequence[str]) : da todos los posibles modelos que puede haber con la lista de variables dadas.
- truth_values(formula:Formula, models:Iterable[Model]): Evalúa la fórmula sobre todos los modelos dados como input.
- print_truth_table(formu:Formula): escribe en pantalla la tabla de verdad de una formula
- is_tautology(formu:Formula): Comprueba si la formula es una tautología.
- is_contradiction(formu:Formula): Comprueba si la formula es una contradicción.
- is_satisfacible(formu:Formula): Comprueba si la formula es satisfacible.

### class InferenceRule(assumptions:Sequence[Formula], conclusion:Formula)

La clase InferenceRule está compuesta de los atributos:

- assumptions: Sequence[Formula]: es la lista de las premisas
- conclusion:Formula: es la conclusión a la que se llega.

La clase contiene los siguientes métodos:

- variables(self): Es el conjunto de las variables tanto de las premisas como de la conclusión.

Adicionalmente, tenemos las siguientes funciones:

- evaluate_inference(rule:InferenceRule, model:Model): Comprueba que dado un modelo en el que se cumplen todas las premisas, se cumpla la conclusion. Esta función está en semantics.py.
- is_sound_inference(rule:InferenceRule): comprueba que la regla de inferencia tiene sentido. Esta función está en semantics.py.
