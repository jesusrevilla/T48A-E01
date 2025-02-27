# -*- coding: utf-8 -*-
"""Copia de Examen del primer parcial.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1OQBw9JR_AfTcZw5zNe-Q8R676cQL2W_S
"""

import numpy as np

# Importante: verifica que tu nombre y número de matrícula esten correctos
nombre = "Uriel Martinez Monreal"
numero_de_matricula = 178646
fecha = '2025-02-26'

"""1.   El 30 de junio de 1992, la capitalización de mercados de valores del Pacífico y Asia fue:

País |  Capitalización (en miles de millones de dólares)
-----|---------------------------------------------------
Filipinas | 17
Indonesia | 21
Tailandia | 44
Singapur | 50
Malasia | 79
Corea del Sur | 86
Taiwan | 140
Hong Kong | 178
Australia | 203

* a) Encuentre la media aritmética de los datos
* b) Encuentre la mediana de los datos
* c) Encuentre la desviación estándar de los datos

regrese una tupla en el siguiente orden:
(media, mediana, desv_est)
"""

def capitalizacion():
    cap = np.array([17, 21, 44, 50, 79, 86, 140, 178, 203])
    media = np.mean(cap)
    mediana = np.median(cap)
    desv_est = np.std(cap)
    return (media, mediana, desv_est)

"""2.    La aistencia a los 10 últimos partidos en casa de las Águilas de Baltimore fue la siguiente:



20100, 24500, 31600, 28400, 49500, 19350, 25600, 30600, 11300, 28560


Calcule el rango, la varianza y la desviación stándard para estos datos

Regrese una tupla con el siguiente orden:

(rango, varianza, desv_est)
"""

def asistencia_dispersion():
    asistencia = np.array([20100, 24500, 31600, 28400, 49500, 19350, 25600, 30600, 11300, 28560])
    rango = np.max(asistencia) - np.min(asistencia)
    varianza = np.var(asistencia)
    desv_est = np.std(asistencia)
    return (rango, varianza, desv_est)

"""3.    Genere un histograma de las siguientes calificaciones en el examen parcial:

7.9, 7.8, 7.8, 6.7, 7.6, 8.7, 8.5, 7.3, 6.6, 9.9, 8.4, 7.2, 6.6, 5.7, 9.4, 8.4, 7.2, 6.3, 5.1, 4.8, 5.0, 6.1, 7.1, 8.2, 9.3, 10.0, 8.9

Nota: regrese el histograma generado con la función de numpy con 10 bins, no genere la gráfica
"""

def histograma_np():
    calificaciones = np.array([7.9, 7.8, 7.8, 6.7, 7.6, 8.7, 8.5, 7.3, 6.6, 9.9, 8,4, 7.2, 6.6, 5.7, 9.4, 8.4, 7.2, 6.3, 5.1, 4.8, 5.0, 6.1, 7.1, 8.2, 9.3, 10.0, 8.9])
    histograma = np.histogram(calificaciones, bins=10)
    return histograma
histograma_np()

"""4.    Analiza la correlación entre los datos de Tamaño y Precio y

Regresa el coeficiente de Pearson


   Tamaño (m²) | Precio (MXN)
   ------------|------------
          100  |    1305710
          120  |    1658277
          140  |    1894167
          160  |    2136552
          180  |    2298267
          200  |    2553624
          220  |    2780503
          240  |    3289726
          260  |    3472743
          280  |    3779477
"""

def correlacion():
    tamaño = np.array([100, 120, 140, 160, 180, 200, 220, 240, 260, 280])
    precio = np.array([1305710, 1658277, 1894167, 2136552, 2298267, 2553624, 2780503, 3289726, 3472743, 3779477])
    correlacion = np.corrcoef(tamaño, precio)
    return correlacion
correlacion()

"""5.        La tienda de departamentso Friendly ha sido objeto de muchos robos durante el último mes; pero debido al aumento a las medidas de seguridad, se han detenido 250 ladrones. Se registró el sexo de cada ladrón; también se anotó si se trataba de un primer delito o era reincidente. Los datos se resumen en la siguiente tabla.

Sexo | Primera ofensa | Reincidente
-----|----------------|------------
Hombre | 60 | 70
Mujer | 44 | 76

Suponga que se selecciona al azar un ladrón detenido, calcule
* la probabilidad de que el ladrón sea hombre: p_hombre
* la probabilidad de que sea la primera ofensa, dado que es hombre: p_po_hombre

Regrese ambos datos en una tupla con el siguiente orden
(p_hombre, p_po_hombre)
"""

def probabilidad_condicional():
    p_hombre = (60 + 70) / (60 + 70 + 44 + 76)
    p_po_hombre = 60 / (60 + 70)
    return (p_hombre, p_po_hombre)

"""Contesta las siguientes preguntas

Definición del Problema:

6.     ¿Cuál es el problema específico que se desea resolver con la minería de datos?
7.     ¿Por qué es importante resolver este problema?

Objetivos del Proyecto:

8.     ¿Cuáles son los objetivos principales del anteproyecto?
9.     ¿Qué resultados esperas obtener al final del proyecto?

Recolección de Datos:

10.    ¿Qué tipo de datos se necesitarán para este proyecto?

Regresa cadenas de texto con tu respuesta.
"""

def problema_especifico():

    return """
      La identificacion, analisis y resolucion de problemas en los datos por medio de graficos y predicciones
      para anticipar fallos en sistemas de gran manejo de datos

    """

def importancia():

    return """
      Porque por ejemplo existen sistemas como los casos de los bancos o cualquier medio de inversiones en los cuales cualquier error minimo de datos
      puede llevar a perdidas monetarias ya sea para emprendedores o empresas por igual

    """

def objetivos():

    return """

    Actualmente trabajo en un restaurante el cual tiene datos almacenados de años anteriores pero existen casos o dias en los que
    la venta esperada no es la misma a la venta real y los superiores toman eso como una baja en la calidad del servicio
    que se brinda,

    asi que espero poder crear un sistema de datos que basado en los años anteriores y los dias que surge algun evento
    pueda haber una prediccion mas acertada

    """

def tipo_de_datos():

    return """
    Para esto se necesitarian los datos ya obtenidos anteriormente de la venta de años anteriores, asi como datos sobre eventos televisivos proximos
    y tambien saber los dias en los que la gente consume mas y cuales son sus mayores preferencias para hacer un calculo estimado mas cerrado

    """