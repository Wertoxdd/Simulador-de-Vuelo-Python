"""

Clase responsable de todas las funciones físicas y matemáticas del cohete.

"""

from sim import parametros


def calcular_aceleracion(tiempo: float, cohete: parametros.Cohete) -> float:
    if tiempo < cohete.tiempo_combustion:
        return cohete.empuje/cohete.masa-parametros.GRAVEDAD
    else:
        return -parametros.GRAVEDAD
