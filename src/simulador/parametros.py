"""
Clase que declara los parámetros que sigue el cohete y el propio programa.    
    
"""

from dataclasses import dataclass

@dataclass(frozen=true)
class Cohete:
    masa: float
    empuje: float
    tiempo_combustion: float

GRAVEDAD = 9.80665

cohete1 = Cohete(masa=1.0, empuje=30.0, tiempo_combustion=2.0)