# -*- coding: utf-8 -*-
"""Copia de Examen del primer parcial.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1rJyXugi7e_jOcOar1BZrUMHpjLyQVtuj
"""

import numpy as np

# Importante: verifica que tu nombre y número de matrícula esten correctos
nombre = "José Emanuel Guerrero Torres"
numero_de_matricula = 176308
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
  arr=np.array([17,21,44,50,79,86,140,178,203])
  mean = np.mean(arr)
  #print(f"Media: {mean}")
  median = np.median(arr)
  #print(f"Mediana: {median}")
  std = np.std(arr)
  #print(f"Desviación estándar: {std}")
  return (mean, median, std)

capitalizacion()

"""2.    La aistencia a los 10 últimos partidos en casa de las Águilas de Baltimore fue la siguiente:



20100, 24500, 31600, 28400, 49500, 19350, 25600, 30600, 11300, 28560


Calcule el rango, la varianza y la desviación stándard para estos datos

Regrese una tupla con el siguiente orden:

(rango, varianza, desv_est)
"""

def asistencia_dispersion():
  arr=([20100, 24500, 31600, 28400, 49500, 19350, 25600, 30600, 11300, 28560])
  range = np.ptp(arr)
  #print(f"Rango: {range}")
  variance = np.var(arr)
  #print(f"Varianza: {variance}")
  std = np.std(arr)
  #print(f"Desviación estándar: {std}")
  return (range, variance, std)

  variance = np.var(data)

asistencia_dispersion()

"""3.    Genere un histograma de las siguientes calificaciones en el examen parcial:

7.9, 7.8, 7.8, 6.7, 7.6, 8.7, 8.5, 7.3, 6.6, 9.9, 8.4, 7.2, 6.6, 5.7, 9.4, 8.4, 7.2, 6.3, 5.1, 4.8, 5.0, 6.1, 7.1, 8.2, 9.3, 10.0, 8.9

Nota: regrese el histograma generado con la función de numpy con 10 bins, no genere la gráfica
"""

def histograma_np():
  import matplotlib.pyplot as plt
  arr=([7.9, 7.8, 7.8, 6.7, 7.6, 8.7, 8.5, 7.3, 6.6, 9.9, 8.4, 7.2, 6.6, 5.7, 9.4, 8.4, 7.2, 6.3, 5.1, 4.8, 5.0, 6.1, 7.1, 8.2, 9.3, 10.0, 8.9])
  plt.hist(arr, bins=10)  # bins define el número de barras en el histograma
  plt.xlabel("calificaciones")
  plt.ylabel("frecuencia")
  plt.title("Histograma de los datos")
  plt.show()
  return

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
  x = np.array([100, 120, 140, 160, 180, 200, 220, 240, 260, 280])
  y = np.array([1305710,1658277,1894167,2136552,2298267,2553624,2780503,3289726,3472743,3779477])
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

  print("Coeficiente de correlación de Pearson:", r)

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
  # Datos de la tabla
  hombre_po = 60
  hombre_re = 70
  mujer_po = 44
  mujer_re = 76

  # Total de detenidos
  total_detenidos = hombre_po + hombre_re + mujer_po + mujer_re

  # Probabilidad de que el ladrón sea hombre
  p_hombre = (hombre_po + hombre_re) / total_detenidos

  # Probabilidad de que sea la primera ofensa, dado que es hombre
  p_po_hombre = hombre_po / (hombre_po + hombre_re)

  # Resultado en tupla
  resultado = (p_hombre, p_po_hombre)
  resultado
  return resultado

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
  return "en una empresa se tiene una gran cantidad de productos con cierto ID pero no se tiene la cantidad exacta de cuales productos se venden y los dias especificos o temporadas en los que se vende mas cierto producto"

def importancia():
  return" este problema es importante resolver para poder ver que productos se venden mas en determinadas fechas para poder hacer una mayor produccion de esos productos es especifico en esas fechas"

def objetivos():
  return "mejor las ventas de los productos y disminuir el costo de produccion evitando hacer productos de baja demanda, como resultado se espera una mayor venta de productos"

def tipo_de_datos():
  return" los datos necesarios son el total de productos y descripciones de cada uno, numero de ventas y fechas de ventas de cada venta"