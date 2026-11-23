"""
Clase encargada de hacer las simulaciones correspondientes.

"""

from sim import parametros
from dataclasses import dataclass, field

@dataclass #no es frozen porque los datos se rellenan durante la simulacion
class Registro:
    tiempo: list[float] = field(default_factory=list)
    altura: list[float] = field(default_factory=list)
    velocidad: list[float] = field(default_factory=list)
    aceleracion: list[float] = field(default_factory=list)

    def registrar(self, t: float, h: float, v: float, a: float) -> None:
        self.tiempo.append(t)
        self.altura.append(h)
        self.velocidad.append(v)
        self.aceleracion.append(a)

    def __len__(self) -> int:
        # se puede calcular con cualquiera de las 4 listas disponibles, porque tienen la misma longitud
        return len(self.tiempo)     
        
    @property
    def apogeo(self) -> float:
        return max(self.altura)

    @property
    def instante_apogeo(self) -> float:
        pos = self.altura.index(self.apogeo)
        return self.tiempo[pos]

    @property
    def tiempo_total(self) -> float:
        return self.tiempo[-1]

    @property
    def velocidad_impacto(self) -> float:
        return self.velocidad[-1]      

    
registro1 = Registro()
registro1.registrar(1, 4, 0.5, 50)
registro1.registrar(2,20,4,200)
registro1.registrar(3,24,6,300)
print(len(registro1))
print(registro1.tiempo_total)
print(registro1.velocidad_impacto)
print(registro1.apogeo)
print(registro1.instante_apogeo)

def bucle_ppal(cohete: parametros.Cohete, dt=0.001, t_maximo=1000) -> Registro:
    if cohete.empuje <= cohete.masa*parametros.GRAVEDAD:
        raise ValueError("Error: Calculos erroneos (empuje menor que el peso).")
    
    t, h, v = 0.0, 0.0, 0.0
    registro = Registro()
    