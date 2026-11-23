"""
    
Clase principal    
    
"""

from sim import parametros, simulador
def main():
    cohete_prueba = parametros.Cohete(masa=1.0, empuje=30, tiempo_combustion=2)
    registro = simulador.simular(cohete=cohete_prueba, dt=0.01, t_maximo=1000)
    registro.imprimir_resumen()
    # TODO llamada a la grafica
    
if __name__ == "__main__":
    main()