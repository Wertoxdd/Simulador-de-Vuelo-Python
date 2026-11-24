"""

Modulo encargado de gestionar las gráficas de la simulación

"""

import matplotlib.pyplot as plt 
from sim import simulador


def graficar_altura(registro: simulador.Registro) -> None:
    plt.plot(registro.tiempo, registro.altura)
    plt.scatter(registro.instante_apogeo, registro.apogeo, color="green", label="Apogeo", zorder=5)
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Altura (m)")
    plt.title("Altura / Tiempo")
    plt.grid(True)
    plt.legend()
    plt.show()