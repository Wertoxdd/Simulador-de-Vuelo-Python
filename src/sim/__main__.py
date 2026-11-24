"""
    
Clase principal    
    
"""

from sim import parametros, simulador
def main():
    cohete_prueba = parametros.Cohete(masa=1.0, empuje=30, tiempo_combustion=2)
    for i in range(0, 3):
        print(f"{0.1*(10**-i):.3f}")
        registro = simulador.simular(cohete=cohete_prueba, dt=0.1*(10**-i), t_maximo=1000)
        registro.imprimir_resumen()
        
        if i==0:
            pasos_aceleracion_positiva = sum(1 for a in registro.aceleracion if a > 0)
            if pasos_aceleracion_positiva == 20: print(True)
            else: print(False)
            
        if i==1:
            pasos_aceleracion_positiva = sum(1 for a in registro.aceleracion if a > 0)
            if pasos_aceleracion_positiva == 200: print(True)
            else: print(False)
                    
        if i==2:
            pasos_aceleracion_positiva = sum(1 for a in registro.aceleracion if a > 0)
            if pasos_aceleracion_positiva == 2000: print(True)
            else: print(False)

    # TODO llamada a la grafica
    
if __name__ == "__main__":
    main()