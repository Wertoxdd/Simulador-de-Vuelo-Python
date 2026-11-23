# Simulador de vuelo de un cohete

Simulador de vuelo vertical (1D) de un cohete escrito en Python. Calcula la altura, la velocidad y la aceleración a lo largo de todo el vuelo, y obtiene el apogeo, el tiempo total de vuelo y la velocidad de impacto.

El proyecto se desarrolla por fases: cada una añade un fenómeno físico al modelo anterior y se valida frente a una solución analítica antes de integrarse en `main`.

## Estado

En desarrollo. **Fase actual: 1 (modelo mínimo).** De momento está implementado el cálculo de la aceleración; el bucle de simulación y las gráficas están en curso.

## Modelo físico

Fase 1: el cohete vuela en vertical, con **masa constante** y sometido solo a dos fuerzas, el empuje del motor y su peso. No se considera el rozamiento del aire.

Se toma el sentido positivo hacia arriba y la altura $h = 0$ en el suelo. Por la segunda ley de Newton, la aceleración es la fuerza neta dividida entre la masa. Con $T$ el empuje, $m$ la masa, $g$ la gravedad y $t_b$ el tiempo de combustión:

$$
a(t) =
\begin{cases}
\dfrac{T}{m} - g & \text{si } t < t_b \quad \text{(motor encendido)} \\[8pt]
-g & \text{si } t \ge t_b \quad \text{(motor apagado)}
\end{cases}
$$

Para que el cohete despegue hace falta $T > m\,g$.

**Integración numérica.** El movimiento se calcula con el método de Euler: el tiempo avanza en pasos pequeños de duración $\Delta t$ (`dt` en el código) y, en cada paso, la velocidad y la altura se actualizan a partir de la aceleración y la velocidad. Cuanto menor es $\Delta t$, más se acerca el resultado a la solución exacta.

**Gravedad.** Se usa la gravedad estándar, $g = 9{,}80665\ \mathrm{m/s^2}$, tomada de `scipy.constants.g`.

## Instalación

Requisitos: Python y Git. Probado con Python 3.14.

```bash
git clone https://github.com/Wertoxdd/Simulador-de-Vuelo-Python.git
cd Simulador-de-Vuelo-Python

python -m venv .venv
# Windows (PowerShell):  .venv\Scripts\Activate.ps1
# Windows (CMD):         .venv\Scripts\activate
# Linux / macOS:         source .venv/bin/activate

pip install -r requirements.txt
pip install -e .
```

## Uso

Por ahora solo se puede ejecutar la prueba del cálculo de la aceleración, desde la raíz del repositorio:

```bash
python tests/pruebas_fisica.py
```

## Dependencias

| Librería | Para qué se usa |
|---|---|
| `scipy` | Solo `scipy.constants.g`, el valor estándar de la gravedad. |
| `numpy` | Análisis de los resultados de la simulación. |
| `matplotlib` | Gráficas del vuelo. |

Las versiones exactas están en [`requirements.txt`](requirements.txt).

## Estructura del proyecto

```
.
├── src/
│   └── simulador/
│       ├── __init__.py
│       ├── parametros.py      # parámetros del cohete
│       └── fisica.py          # cálculo de la aceleración
├── tests/
│   └── pruebas_fisica.py      # pruebas del cálculo de la aceleración
├── pyproject.toml             # metadatos e instalación del paquete
├── requirements.txt           # dependencias con sus versiones
└── README.md
```

## Hoja de ruta

- [x] **Fase 0:** repositorio, entorno y estructura básica
- [ ] **Fase 1:** modelo mínimo (empuje y gravedad, sin rozamiento)
- [ ] **Fase 2:** rozamiento aerodinámico
- [ ] **Fase 3:** masa variable
- [ ] **Fase 4:** fases de vuelo y paracaídas
- [ ] **Fase 5:** resultados, pruebas automáticas y documentación final