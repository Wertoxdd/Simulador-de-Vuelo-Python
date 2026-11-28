"""

Modulo encargado de gestionar las gráficas de la simulación

"""

import matplotlib.pyplot as plt 
from sim import simulador


def imprimir_por_pantalla(registro, mensaje: str):
    plt.annotate(mensaje, 
                 xy=(registro.instante_apogeo, registro.apogeo), 
                 xytext=(registro.instante_apogeo +  10, registro.apogeo + 10), 
                 arrowprops=dict(arrowstyle="->")
                 )


def graficar_altura(registro) -> None:
    plt.plot(registro.tiempo, registro.altura)
    plt.scatter(registro.instante_apogeo, registro.apogeo, color="green", label="Apogeo", zorder=5) # destaca el apogeo
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Altura (m)")
    plt.title("Altura / Tiempo")
    plt.grid(True)
    plt.legend()
    plt.show()
    
    
def graficar_velocidad(registro) -> None:
    plt.plot(registro.tiempo, registro.velocidad)
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Velocidad (m/s)")
    plt.title("Velocidad / Tiempo")
    plt.grid(True)
    plt.show()        


def graficar_aceleración(registro) -> None:
    plt.plot(registro.tiempo, registro.aceleracion)
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Aceleración (m/s^2)")
    plt.title("Aceleración / Tiempo")
    plt.grid(True)
    plt.show()
    
    
def graficar_vuelo(registro) -> None:
    fig, ejes = plt.subplots(3, 1, sharex=True, figsize=(10, 8))
    ejes[0].plot(registro.tiempo, registro.altura)
    ejes[0].set_ylabel("Altura (m)")
    ejes[0].set_xlabel("Tiempo (s)")
    ejes[1].plot(registro.tiempo, registro.velocidad)
    ejes[1].set_ylabel("Velocidad (m/s)")
    ejes[1].set_xlabel("Tiempo (s)")
    ejes[2].plot(registro.tiempo, registro.aceleracion)
    ejes[2].set_ylabel("Aceleración (m/s^2)")
    ejes[2]set_xlabel("Tiempo (s)")
    for eje in ejes:
        eje.grid(True)
        
    plt.show()
