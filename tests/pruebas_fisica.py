"""

Clase responsable para hacer las pruebas de las fisicas del cohete.
    
"""

from sim import parametros, fisica

def pruebas_calcular_aceleracion():
    cohetePrueba = parametros.Cohete(1.0, 30.0, 2.0)
    
    # prueba 1 -> t = 0
    resultado = fisica.calcular_aceleracion(0.0, cohetePrueba)
    print("Resultado acelereación: " + str(resultado))

    # prueba 2 -> t = 1
    resultado = fisica.calcular_aceleracion(1.0, cohetePrueba)
    print("Resultado acelereación: " + str(resultado))

    # prueba 3 -> t = 1.999
    resultado = fisica.calcular_aceleracion(1.999, cohetePrueba)
    print("Resultado acelereación: " + str(resultado))

    # prueba 4 -> t = 2 
    resultado = fisica.calcular_aceleracion(2.0, cohetePrueba)
    print("Resultado acelereación: " + str(resultado))

    # prueba 5 -> t = 10
    resultado = fisica.calcular_aceleracion(10.0, cohetePrueba)
    print("Resultado acelereación: " + str(resultado))

    cohetePrueba2 = parametros.Cohete(2.0, 200.0, 3.0)

    # prueba 6 -> t = 1 cohete 2
    resultado = fisica.calcular_aceleracion(1.0, cohetePrueba2)
    print("Resultado acelereación: " + str(resultado))

    cohetePrueba3 = parametros.Cohete(2.0, 50.0, 3.0)

    # prueba 7 -> t = 1 cohete 3
    resultado = fisica.calcular_aceleracion(1.0, cohetePrueba3)
    print("Resultado acelereación: " + str(resultado))

    cohetePrueba4 = parametros.Cohete(2.0, 15.0, 3.0) 
    resultado = fisica.calcular_aceleracion(1.0, cohetePrueba4)
    print("Resultado acelereación: " + str(resultado))

pruebas_calcular_aceleracion()