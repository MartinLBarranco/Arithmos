# This file is part of the materials accompanying the book
# "Mathematical Logic through Python" by Gonczarowski and Nisan,
# Cambridge University Press. Book site: www.LogicThruPython.org
# (c) Yannai A. Gonczarowski and Noam Nisan, 2017-2022
# File name: propositions/semantics.py

"""Semantic analysis of propositional-logic constructs."""

from typing import AbstractSet, Iterable, Iterator, Mapping, Sequence, Tuple

from propositions.syntax import *
from propositions.proofs import *

from itertools import product

#: A model for propositional-logic formulas, a mapping from variable names to
#: truth values.
Model = Mapping[str, bool]

def is_model(model: Model) -> bool:
    """Checks if the given dictionary is a model over some set of variable
    names.

    Parameters:
        model: dictionary to check.

    Returns:
        ``True`` if the given dictionary is a model over some set of variable
        names, ``False`` otherwise.
    """
    for key in model:
        if not is_variable(key):
            return False
    return True

def variables(model: Model) -> AbstractSet[str]:
    """Finds all variable names over which the given model is defined.

    Parameters:
        model: model to check.

    Returns:
        A set of all variable names over which the given model is defined.
    """
    assert is_model(model)
    return model.keys()

def evaluate(formula: Formula, model: Model) -> bool:
    """Calculates the truth value of the given formula in the given model.

    Parameters:
        formula: formula to calculate the truth value of.
        model: model over (possibly a superset of) the variable names of the
            given formula, to calculate the truth value in.

    Returns:
        The truth value of the given formula in the given model.

    Examples:
        >>> evaluate(Formula.parse('~(p&q76)'), {'p': True, 'q76': False})
        True

        >>> evaluate(Formula.parse('~(p&q76)'), {'p': True, 'q76': True})
        False
    """
    assert is_model(model)
    assert formula.variables().issubset(variables(model))
    if is_constant(formula.root):
        return formula.root == "T"
    if is_variable(formula.root):
        return model[formula.root]
    if is_unary(formula.root):
        assert formula.first is not None
        return not evaluate(formula.first, model)
    if is_binary(formula.root):
        assert formula.first is not None and formula.second is not None
        if formula.root == "&":
            return evaluate(formula.first, model) and evaluate(formula.second, model)
        if formula.root == "|":
            return evaluate(formula.first, model) or evaluate(formula.second, model)
        else:
            a, b = evaluate(formula.first, model), evaluate(formula.second, model)
            z = (a,b)
            if z == (True, False):
                return False
            else:
                return True
    # Task 2.1

def all_models(variables: Sequence[str]) -> Iterable[Model]:
    """Calculates all possible models over the given variable names.

    Parameters:
        variables: variable names over which to calculate the models.

    Returns:
        An iterable over all possible models over the given variable names. The
        order of the models is lexicographic according to the order of the given
        variable names, where False precedes True.

    Examples:
        >>> list(all_models(['p', 'q']))
        [{'p': False, 'q': False}, {'p': False, 'q': True}, {'p': True, 'q': False}, {'p': True, 'q': True}]

        >>> list(all_models(['q', 'p']))
        [{'q': False, 'p': False}, {'q': False, 'p': True}, {'q': True, 'p': False}, {'q': True, 'p': True}]
    """
    for v in variables:
        assert is_variable(v)
    allm = [dict(zip(variables, posibles)) for posibles in product([False,True], repeat=len(variables))]
    return allm
    # Task 2.2

def truth_values(formula: Formula, models: Iterable[Model]) -> Iterable[bool]:
    """Calculates the truth value of the given formula in each of the given
    models.

    Parameters:
        formula: formula to calculate the truth value of.
        models: iterable over models to calculate the truth value in.

    Returns:
        An iterable over the respective truth values of the given formula in
        each of the given models, in the order of the given models.

    Examples:
        >>> list(truth_values(Formula.parse('~(p&q76)'), all_models(['p', 'q76'])))
        [True, True, True, False]
    """
    res = [evaluate(formula, modelito) for modelito in models]
    return res
    # Task 2.3

def print_truth_table(formula: Formula) -> None:
    """Prints the truth table of the given formula, with variable-name columns
    sorted alphabetically.

    Parameters:
        formula: formula to print the truth table of.

    Examples:
        >>> print_truth_table(Formula.parse('~(p&q76)'))
        | p | q76 | ~(p&q76) |
        |---|-----|----------|
        | F | F   | T        |
        | F | T   | T        |
        | T | F   | T        |
        | T | T   | F        |
    """
    def printBool(val:bool)->str:
        """
        Correcta impresion de cada booleano.\n
        True -> "T"\n
        False -> "F"
        """
        if val:
            return 'T'
        else:
            return 'F'
    longitudes = [len(vari) for vari in formula.variables()] + [len(str(formula))]
    #Dibujo de la primera línea
    primeralinea = ""
    for elem in formula.variables():
        primeralinea += "| " + elem + " "
    primeralinea += "| " + str(formula) + " |"
    #Dibujo de la barra espaciadora
    barra = ""
    for elem in longitudes:
        barra += "|" + '-'*(elem+2)
    barra += "|"
    print(primeralinea)
    print(barra)
    # Hacemos cada modelo
    modelos = all_models(formula.variables())
    #cogemos un modelo
    for mode in  modelos:
        #evaluamos la formula en este modelo y lo convertimos en un string
        resfor = evaluate(formula, mode)
        # Cogemos los valores de los modelos, los metemos en una lista y al final el resultado de evaluar
        lista = [printBool(elem) for elem in mode.values()] + [printBool(resfor)]
        nueva_linea = ""
        for i in range(len(lista)):
            nueva_linea += "| " + lista[i] + " "*longitudes[i]
        nueva_linea += "|"
        print(nueva_linea)
    # Task 2.4

def is_tautology(formula: Formula) -> bool:
    """Checks if the given formula is a tautology.

    Parameters:
        formula: formula to check.

    Returns:
        ``True`` if the given formula is a tautology, ``False`` otherwise.
    """
    for modelo in  all_models(formula.variables()):
        if evaluate(formula, modelo) == False:
            return False
    return True
    # Task 2.5a

def is_contradiction(formula: Formula) -> bool:
    """Checks if the given formula is a contradiction.

    Parameters:
        formula: formula to check.

    Returns:
        ``True`` if the given formula is a contradiction, ``False`` otherwise.
    """
    for modelo in  all_models(formula.variables()):
        if evaluate(formula, modelo):
            return False
    return True
    # Task 2.5b

def is_satisfiable(formula: Formula) -> bool:
    """Checks if the given formula is satisfiable.

    Parameters:
        formula: formula to check.

    Returns:
        ``True`` if the given formula is satisfiable, ``False`` otherwise.
    """
    for modelo in  all_models(formula.variables()):
        if evaluate(formula, modelo):
            return True
    return False
    # Task 2.5c

def _synthesize_for_model(model: Model) -> Formula:
    """Synthesizes a propositional formula in the form of a single conjunctive
    clause that evaluates to ``True`` in the given model, and to ``False`` in
    any other model over the same variable names.

    Parameters:
        model: model over a nonempty set of variable names, in which the
            synthesized formula is to hold.

    Returns:
        The synthesized formula.
    """
    assert is_model(model)
    assert len(model.keys()) > 0
    lista = list(zip(model.keys(), model.values()))
    lista_formulas = []
    for elem in lista:
        if elem[1]:
            f = Formula(elem[0])
        else:
            f = Formula('~', Formula(elem[0]))
        lista_formulas.append(f)
    f = lista_formulas[0]
    for formu in lista_formulas[1:]:
        f = Formula("&", f, formu)
    return f
    # Task 2.6

def synthesize(variables: Sequence[str], values: Iterable[bool]) -> Formula:
    """Synthesizes a propositional formula in DNF over the given variable names,
    that has the specified truth table.

    Parameters:
        variables: nonempty set of variable names for the synthesized formula.
        values: iterable over truth values for the synthesized formula in every
            possible model over the given variable names, in the order returned
            by `all_models`\ ``(``\ `~synthesize.variables`\ ``)``.

    Returns:
        The synthesized formula.

    Examples:
        >>> formula = synthesize(['p', 'q'], [True, True, True, False])
        >>> for model in all_models(['p', 'q']):
        ...     evaluate(formula, model)
        True
        True
        True
        False
    """
    assert len(variables) > 0
    modelos = all_models(variables)
    print(modelos)
    # Task 2.7

def _synthesize_for_all_except_model(model: Model) -> Formula:
    """Synthesizes a propositional formula in the form of a single disjunctive
    clause that evaluates to ``False`` in the given model, and to ``True`` in
    any other model over the same variable names.

    Parameters:
        model: model over a nonempty set of variable names, in which the
            synthesized formula is to not hold.

    Returns:
        The synthesized formula.
    """
    assert is_model(model)
    assert len(model.keys()) > 0
    # Optional Task 2.8

def synthesize_cnf(variables: Sequence[str], values: Iterable[bool]) -> Formula:
    """Synthesizes a propositional formula in CNF over the given variable names,
    that has the specified truth table.

    Parameters:
        variables: nonempty set of variable names for the synthesized formula.
        values: iterable over truth values for the synthesized formula in every
            possible model over the given variable names, in the order returned
            by `all_models`\ ``(``\ `~synthesize.variables`\ ``)``.

    Returns:
        The synthesized formula.

    Examples:
        >>> formula = synthesize_cnf(['p', 'q'], [True, True, True, False])
        >>> for model in all_models(['p', 'q']):
        ...     evaluate(formula, model)
        True
        True
        True
        False
    """
    assert len(variables) > 0
    # Optional Task 2.9

def evaluate_inference(rule: InferenceRule, model: Model) -> bool:
    """Checks if the given inference rule holds in the given model.

    Parameters:
        rule: inference rule to check.
        model: model to check in.

    Returns:
        ``True`` if the given inference rule holds in the given model, ``False``
        otherwise.

    Examples:
        >>> evaluate_inference(InferenceRule([Formula('p')], Formula('q')),
        ...                    {'p': True, 'q': False})
        False

        >>> evaluate_inference(InferenceRule([Formula('p')], Formula('q')),
        ...                    {'p': False, 'q': False})
        True
    """
    assert is_model(model)
    # Comprobar las variables de la regla están dentro de las del modelo

    eval_premisas_model = True
    for premisa in rule.assumptions:
        jj = evaluate(premisa, model)
        eval_premisas_model = eval_premisas_model and jj

    # Comprobamos que las premisas evaluadas en el modelos son ciertas.
    res = evaluate(rule.conclusion, model)

    # Comprobamos que la conclusión evaluada en el modelo no es cierta.
    return  not (eval_premisas_model and not res)
    # Task 4.2

def is_sound_inference(rule: InferenceRule) -> bool:
    """Checks if the given inference rule is sound, i.e., whether its
    conclusion is a semantically correct implication of its assumptions.

    Parameters:
        rule: inference rule to check.

    Returns:
        ``True`` if the given inference rule is sound, ``False`` otherwise.
    """
    # Extraemos todas las variables de la regla y calculamos todos los modelos posibles
    modelos = all_models(rule.variables())

    # comprobamos que la regla es cierta para cada uno de los modelos creados
    for modelito in modelos:
        if not evaluate_inference(rule, modelito):
            return False
    return True
    # Task 4.3

