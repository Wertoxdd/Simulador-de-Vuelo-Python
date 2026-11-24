"""
    
Clase principal    
    
"""

from sim import parametros, simulador, graficas
import time

def main():
    cohete_prueba = parametros.Cohete(masa=1.0, empuje=30, tiempo_combustion=2)
    for i in range(0, 3):
        print(f"{0.1*(10**-i):.3f}")
        registro = simulador.simular(cohete=cohete_prueba, dt=0.1*(10**-i), t_maximo=1000)
        registro.imprimir_resumen()
        graficas.graficar_altura(registro)        


if __name__ == "__main__":
    main()