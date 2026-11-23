"""

Clase responsable de todas las funciones físicas y matemáticas del cohete.

"""

import parametros


def calcular_aceleracion(tiempo, empuje, masa, t_combustion) -> float:
    if tiempo < t_combustion:
        return empuje/masa-parametros.GRAVEDAD
    else:
        return -parametros.GRAVEDAD
    
