"""
Clase encargada de hacer las simulaciones correspondientes.

"""

from sim import parametros, fisica
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
    
    def imprimir_resumen(self) -> None:
        print("------|   RESUMEN   |------")
        print("Apogeo: " + str(self.apogeo))
        print("Instante del apogeo: " + str(self.instante_apogeo))
        print("Tiempo total del vuelo: " + str(self.tiempo_total))
        print("Velocidad del impacto: " + str(self.velocidad_impacto))
        
        
def simular(cohete: parametros.Cohete, dt: float, t_maximo: float) -> Registro:
    if cohete.empuje <= cohete.masa*parametros.GRAVEDAD:
        raise ValueError("Error: Calculos erroneos (empuje menor que el peso).")
    
    t, h, v = 0.0, 0.0, 0.0
    registro = Registro()
    while (h > 0 or v >= 0) and t < t_maximo:
        a = fisica.calcular_aceleracion(t, cohete)
        registro.registrar(t, h, v, a)
        v += a*dt
        h += v*dt
        t += dt
        
    return registro