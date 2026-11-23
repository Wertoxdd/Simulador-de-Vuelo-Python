"""
    
Clase principal    
    
"""

from sim import parametros, fisica, simulador
def main():
    # un unico caso de prueba
    cohete_prueba = parametros.Cohete(masa=2500, empuje=70000, tiempo_combustion=80)
    registro = simulador.simular(cohete=cohete_prueba, dt=0.0001, t_maximo=10000)
    registro.imprimir_resumen()
    # TODO llamada a la grafica
    
if __name__ == "__main__":
    main()