# -*- coding: utf-8 -*-
"""Copia de Examen del primer parcial.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1u8AVR9ce4bcSSv4qjexmldRx7hEG2GDV
"""

import numpy as np

# Importante: verifica que tu nombre y número de matrícula esten correctos
nombre = "Loredo Martinez Miguel Angel"
numero_de_matricula = 178424
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
    datos = np.array([17, 21, 44, 50, 79, 86, 140, 178, 203])
    media = np.mean(datos)
    mediana = np.median(datos)
    desv_est = np.std(datos)
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
    calificaciones = np.array([7.9, 7.8, 7.8, 6.7, 7.6, 8.7, 8.5, 7.3, 6.6, 9.9, 8.4, 7.2, 6.6, 5.7, 9.4, 8.4, 7.2, 6.3, 5.1, 4.8, 5.0, 6.1, 7.1, 8.2, 9.3, 10.0, 8.9])
    histograma = np.histogram(calificaciones, bins=10)
    return histograma

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
    tamano = np.array([100, 120, 140, 160, 180, 200, 220, 240, 260, 280])
    precio = np.array([1305710, 1658277, 1894167, 2136552, 2298267, 2553624, 2780503, 3289726, 3472743, 3779477])

    # Calcular la media
    mean_x = np.mean(tamano)
    mean_y = np.mean(precio)

    # Calcular las desviaciones
    deviation_x = tamano - mean_x
    deviation_y = precio - mean_y

    # Calcular el producto de las desviaciones
    product_deviations = deviation_x * deviation_y

    # Sumar los productos de las desviaciones
    sum_product_deviations = np.sum(product_deviations)

    # Calcular la desviación estándar
    std_x = np.std(x, ddof=1)
    std_y = np.std(y, ddof=1)

    # Calcular el coeficiente de correlación de Pearson
    pearson = sum_product_deviations / ((len(tamano) - 1) * std_x * std_y)

    return pearson

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
    #P(A)
    p_hombre = (60 + 70) / (250)
    #P(A|B)
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
    return "Tomar informacion de forma bruta para convertirlo a informacion que puede apreciarse de forma comprensible"

def importancia():
    return "Para que se puedan tomar decisiones a partir de los resultados obtenidos"

def objetivos():
    return "Aprender a usar el metodo de regresion para poder analizar y predecir de forma adecuada la informacion a partir de los datos"

def tipo_de_datos():
    return "informacion sobre deportes o temas de interes"
