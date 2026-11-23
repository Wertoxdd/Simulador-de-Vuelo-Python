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