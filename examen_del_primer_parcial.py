# -*- coding: utf-8 -*-
"""ExamenPrimerParcial_177771

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18aWWZq3dTvJoU2prXUam5U6burfxHNI_
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Importante: verifica que tu nombre y número de matrícula esten correctos
nombre = "Uriel Montejano Briano"
numero_de_matricula = 177771
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
  data =[17, 21, 44, 50, 79, 86, 140, 178, 203]

  # Media
  mean = np.mean(data)

  # Mediana
  median = np.median(data)

  # Desviación estándar
  std_dev = np.std(data)

  # Tupla
  tupla_datos=(mean, median, std_dev)

  return tupla_datos

capitalizacion()

"""2.    La aistencia a los 10 últimos partidos en casa de las Águilas de Baltimore fue la siguiente:



20100, 24500, 31600, 28400, 49500, 19350, 25600, 30600, 11300, 28560


Calcule el rango, la varianza y la desviación stándard para estos datos

Regrese una tupla con el siguiente orden:

(rango, varianza, desv_est)
"""

def asistencia_dispersion():
  data_Aguilas =[20100, 24500, 31600, 28400, 49500, 19350, 25600, 30600, 11300, 28560]
  # Rango
  Rango=np.ptp(data_Aguilas)

  # Varianza
  Varianza=np.var(data_Aguilas)

  # Desviación estandar
  DevStd=np.std(data_Aguilas)

  tupla_datosAguilas=(Rango, Varianza, DevStd)

  return tupla_datosAguilas

asistencia_dispersion()

"""3.    Genere un histograma de las siguientes calificaciones en el examen parcial:

7.9, 7.8, 7.8, 6.7, 7.6, 8.7, 8.5, 7.3, 6.6, 9.9, 8.4, 7.2, 6.6, 5.7, 9.4, 8.4, 7.2, 6.3, 5.1, 4.8, 5.0, 6.1, 7.1, 8.2, 9.3, 10.0, 8.9

Nota: regrese el histograma generado con la función de numpy con 10 bins, no genere la gráfica
"""

def histograma_np():
  data=[7.9, 7.8, 7.8, 6.7, 7.6, 8.7, 8.5, 7.3, 6.6, 9.9, 8.4, 7.2, 6.6, 5.7, 9.4, 8.4, 7.2, 6.3, 5.1, 4.8, 5.0, 6.1, 7.1, 8.2, 9.3, 10.0, 8.9]
  # Dataframe
  df_data = pd.DataFrame([data])

  # Histograma
  histogramaCali = plt.hist(df_data.iloc[0], bins=10)
  return histogramaCali

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
  # Datos de ejemplo
  x = np.array([100,120,140,160,180,200,220,240,260,280])
  y = np.array([1305710, 1658277, 1894167, 2136552, 2298267, 2553624, 2780503, 3289726, 3472743, 3779477])

  # Calcular la media
  mean_x = np.mean(x)
  mean_y = np.mean(y)

  # Calcular las desviaciones
  deviation_x = x - mean_x
  deviation_y = y - mean_y

  # Calcular el producto de las desviaciones
  product_deviations = deviation_x * deviation_y

  # Sumar los productos de las desviaciones
  sum_product_deviations = np.sum(product_deviations)

  # Calcular la desviación estándar
  std_x = np.std(x, ddof=1)
  std_y = np.std(y, ddof=1)

  # Calcular el coeficiente de correlación de Pearson
  r = sum_product_deviations / ((len(x) - 1) * std_x * std_y)

  return r

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
  dfHombres = pd.DataFrame([60, 44])
  dfMujeres = pd.DataFrame([70, 76])

  evento_A = dfHombres
  evento_B = dfMujeres

  prob_a = np.mean(evento_A)
  prob_b = np.mean(evento_B)

  # Probabilidad condicional
  prob_intersecciones_AB = np.mean(evento_A & evento_B)

  prob_AB = prob_intersecciones_AB / np.mean(dfMujeres.values)
  return prob_AB

probabilidad_condicional()

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
  txt = "El análisis masivo de datos de pruebas de un proceso de producción, esto mediante la recopilación de datos, organización y clasificación y aplicando el análisis estadístico para facilitar el entendimiento de los datos y generar información"
  return txt

def importancia():
  txt = "Es importante debido a que con la aplicación de la minería de datos, podemos leer grandes cantidades de dato, interpretarlos y clasificarlos, esto generando información. "
  return txt

def objetivos():
  txt = "Objetivos: Analizar todos las pruebas realizadas en un proceso de producción para analizar las areas de mejora. Resultados: Una implementación de mejora en el proceso de producción, disminuyendo el error humano y aumentando la eficiencia"
  return txt

def tipo_de_datos():
  txt = "Datos como tiempo, fechas, turnos de operadores, cantidad de productos, etc"
