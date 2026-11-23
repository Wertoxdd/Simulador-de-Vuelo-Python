"""

Clase responsable para hacer las pruebas de las fisicas del cohete.
    
"""

from src import simulador 
from simulador import parametros, fisica

def pruebas_calcular_aceleracion():
    cohetePrueba = parametros.Cohete(1.0, 30.0, 2.0)
    
    # prueba 1 -> t = 1
    resultado = fisica.calcular_aceleracion(1.0, cohetePrueba.empuje, cohetePrueba.masa, cohetePrueba.tiempo_combustion)
    print("Resultado acelereación: " + str(resultado))
    
pruebas_calcular_aceleracion()