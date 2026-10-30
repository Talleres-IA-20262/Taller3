"""Punto 1. Distribuciones discretas y decisiones de respuesta."""
import math


def normalize(weights: dict) -> dict:
    """Retorna un diccionario nuevo cuyas probabilidades suman uno.

    Entrada: weights = {resultado: peso}.
    Salida: {resultado: probabilidad}, con las mismas claves.

    Tips:
    - Conserve las claves y su orden; no modifique weights.
    - Rechace pesos negativos, no finitos, diccionarios vacíos y suma cero.
    """
    # TODO: Add your code here
    
    if not weights:
        raise ValueError("El diccionario no puede estar vacio")
    
    for weight in weights.values():
        if weight < 0 or not math.isfinite(weight):
            raise ValueError("Los pesos deben ser no negativos y finitos")
        
    max_weight = max(weights.values())
    if max_weight == 0:
        raise ValueError("La suma de los pesos no puede ser cero")
    
    total = sum(weights.values())
    
    resultados = {}
    for key, value in weights.items():
        resultados[key] = value / total

    return resultados
    # FIN DEL BLOQUE DEL ESTUDIANTE


def expected_utility(distribution: dict, utilities: dict) -> float:
    """Calcula sum_s P(s) U(s) para una acción.

    Entradas: distribution = {resultado: probabilidad} y
    utilities = {resultado: utilidad} para una sola acción.
    Salida: un número con la utilidad esperada.

    Tips:
    - distribution ya debe estar normalizada; no normalice utilidades.
    - Ambas tablas deben contener los mismos resultados posibles.
    """
    # Validación de las entradas; no modificar.
    if set(distribution) != set(utilities) or not distribution:
        raise ValueError("Probabilidades y utilidades deben tener las mismas claves")
    if any(not math.isfinite(p) or p < 0 for p in distribution.values()):
        raise ValueError("Distribución inválida")
    if not math.isclose(sum(distribution.values()), 1, abs_tol=1e-9):
        raise ValueError("La distribución debe sumar uno")
    if any(not math.isfinite(u) for u in utilities.values()):
        raise ValueError("Utilidades no finitas")
    # TODO: Add your code here
    total = 0.0
    
    for resultado,probabilidad in distribution.items():
        total += probabilidad * utilities[resultado]
    return total
    # FIN DEL BLOQUE DEL ESTUDIANTE


def best_action(distribution: dict, actions: dict) -> tuple[str, dict]:
    """Retorna (nombre de acción, utilidades esperadas por acción).

    Entradas: distribution = {resultado: probabilidad} y
    actions = {acción: {resultado: utilidad}}.
    Salida: (acción elegida, {acción: utilidad esperada}).

    Tips:
    - actions asocia cada acción con su tabla de utilidades.
    - Reutilice expected_utility y conserve la primera acción en los empates.
    """
    # Validación de las acciones; no modificar.
    if not actions:
        raise ValueError("Se requiere al menos una acción")
    # TODO: Add your code here
    utilidades_esperadas = {}
    for action, util_dict in actions.items():
        utilidades_esperadas[action] = expected_utility(distribution, util_dict)
    mejor_accion = max(utilidades_esperadas, key=utilidades_esperadas.get)
    return mejor_accion, utilidades_esperadas
    # FIN DEL BLOQUE DEL ESTUDIANTE
