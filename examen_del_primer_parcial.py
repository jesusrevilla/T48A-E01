# -*- coding: utf-8 -*-
"""Copia de Examen del primer parcial.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1eHtAAkUNzVpsGGq4-u2fa3LPENzR3ih2
"""

import numpy as np

# Importante: verifica que tu nombre y número de matrícula esten correctos

nombre = "Diego Adolfo Guerrero González"
numero_de_matricula = 177156
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
    capitalizaciones = np.array([17, 21, 44, 50, 79, 86, 140, 178, 203])
    media = np.mean(capitalizaciones)
    mediana = np.median(capitalizaciones)
    desv_est = np.std(capitalizaciones, ddof=0)
    return (media, mediana, moda, desv_est)

"""2.    La aistencia a los 10 últimos partidos en casa de las Águilas de Baltimore fue la siguiente:



20100, 24500, 31600, 28400, 49500, 19350, 25600, 30600, 11300, 28560


Calcule el rango, la varianza y la desviación stándard para estos datos

Regrese una tupla con el siguiente orden:

(rango, varianza, desv_est)
"""

def asistencia_dispersion():
    asistencias = np.array([20100, 24500, 31600, 28400, 49500, 19350, 25600, 30600, 11300, 28560])
    rango = np.ptp(asistencias)  # Rango (max - min)
    varianza = np.var(asistencias, ddof=0)
    desv_est = np.std(asistencias, ddof=0)
    return (rango, varianza, desv_est)

"""3.    Genere un histograma de las siguientes calificaciones en el examen parcial:

7.9, 7.8, 7.8, 6.7, 7.6, 8.7, 8.5, 7.3, 6.6, 9.9, 8.4, 7.2, 6.6, 5.7, 9.4, 8.4, 7.2, 6.3, 5.1, 4.8, 5.0, 6.1, 7.1, 8.2, 9.3, 10.0, 8.9

Nota: regrese el histograma generado con la función de numpy con 10 bins, no genere la gráfica
"""

def histograma_np():
    calificaciones = np.array([7.9, 7.8, 7.8, 6.7, 7.6, 8.7, 8.5, 7.3, 6.6, 9.9, 8.4,
                               7.2, 6.6, 5.7, 9.4, 8.4, 7.2, 6.3, 5.1, 4.8, 5.0, 6.1,
                               7.1, 8.2, 9.3, 10.0, 8.9])
    hist, bins = np.histogram(calificaciones, bins=10)
    return (hist, bins)

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
    tamanio = np.array([100, 120, 140, 160, 180, 200, 220, 240, 260, 280])
    precio = np.array([1305710, 1658277, 1894167, 2136552, 2298267, 2553624, 2780503, 3289726, 3472743, 3779477])
    coef_pearson = np.corrcoef(tamanio, precio)[0, 1]
    return coef_pearson

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
    total_ladrones = 250
    hombres = 60 + 70
    p_hombre = hombres / total_ladrones
    p_po_hombre = 60 / hombres
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
    return "Identificar patrones en el comportamiento de ventas para optimizar la toma de decisiones"

def importancia():
    return "Resolver este problema permitirá mejorar las estrategias comerciales y aumentar la rentabilidad"

def objetivos():
    return "Analizar datos históricos de ventas para predecir tendencias y optimizar el inventario"

def tipo_de_datos():
    return "Se necesitarán datos históricos de ventas, inventario, y comportamiento de clientes"
