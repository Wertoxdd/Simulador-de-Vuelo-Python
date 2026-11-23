"""

Clase responsable de todas las funciones físicas y matemáticas del cohete.

"""

from sim import parametros


def calcular_aceleracion(tiempo, empuje, masa, t_combustion) -> float:
    if tiempo < t_combustion:
        return empuje/masa-parametros.GRAVEDAD
    else:
        return -parametros.GRAVEDAD
