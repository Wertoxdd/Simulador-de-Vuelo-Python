"""
Clase que declara los parámetros que sigue el cohete y el propio programa.    
    
"""
from scipy import constants
from dataclasses import dataclass

@dataclass(frozen=True)
class Cohete:
    masa: float
    empuje: float
    tiempo_combustion: float

GRAVEDAD = constants.g

cohete1 = Cohete(masa=1.0, empuje=30.0, tiempo_combustion=2.0)