# 1. Importe numpy solo una vez, como se muestra a continuación:
import numpy as np
# Importante: verifica que tu nombre y número de matrícula estén correctos
nombre = "Flores García Yahir Gerardo"
numero_de_matricula = 177887
fecha = '2025-09-11'

"""2. El 30 de junio de 1992, la capitalización de mercados de valores del Pacífico y Asia fue:

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

a) Encuentre la media aritmética de los datos
b) Encuentre la mediana de los datos
c) Encuentre la moda de los datos
e) Encuentre la desviación estándar de los datos

regrese una tupla en el siguiente orden:
(media, mediana, moda, desv_est)
"""

def capitalizacion():
    data = [17, 21, 44, 50, 79, 86, 140, 178, 203]
    
    media = np.mean(data)
    mediana = np.median(data)
    
    counts = {}
    for num in data:
        counts[num] = counts.get(num, 0) + 1
    moda = max(counts, key=counts.get)
    
    desv_est = np.std(data)

    return (media, mediana, desv_est)

capitalizacion()


"""3. La asistencia a los 10 últimos partidos en casa de las Águilas de Baltimore fue la siguiente:

20100, 24500, 31600, 28400, 49500, 19350, 25600, 30600, 11300, 28560

Calcule el rango, la varianza y la desviación estándar para estos datos

Regrese una tupla con el siguiente orden:

(rango, varianza, desv_est)
"""

def asistencia_dispersion():
    data_Aguilas = [20100, 24500, 31600, 28400, 49500, 19350, 25600, 30600, 11300, 28560]
    
    rango = np.ptp(data_Aguilas)
    varianza = np.var(data_Aguilas)
    desv_est = np.std(data_Aguilas)
    
    return (rango, varianza, desv_est)

asistencia_dispersion()


"""4. Genere un histograma de las siguientes calificaciones en el examen parcial:

7.9, 7.8, 7.8, 6.7, 7.6, 8.7, 8.5, 7.3, 6.6, 9.9, 8.4, 7.2, 6.6, 5.7, 9.4, 8.4, 7.2, 6.3, 5.1, 4.8, 5.0, 6.1, 7.1, 8.2, 9.3, 10.0, 8.9

Nota: regrese el histograma generado con la función de numpy, no genere la gráfica
"""

def histograma_np():
    calificaciones = np.array([7.9, 7.8, 7.8, 6.7, 7.6, 8.7, 8.5, 7.3, 6.6, 9.9, 8.4, 7.2, 6.6, 5.7, 9.4, 8.4, 7.2, 6.3, 5.1, 4.8, 5.0, 6.1, 7.1, 8.2, 9.3, 10.0, 8.9])
    histograma = np.histogram(calificaciones, bins=10)
    return histograma

histograma_np()


"""5. Analiza la correlación entre los datos de Tamaño y Precio y

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
    x = np.array([100, 120, 140, 160, 180, 200, 220, 240, 260, 280])
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

    # Calcular la desviación estándar (muestra)
    std_x = np.std(x, ddof=1)
    std_y = np.std(y, ddof=1)

    # Calcular el coeficiente de correlación de Pearson
    r = sum_product_deviations / ((len(x) - 1) * std_x * std_y)

    return r

correlacion()


"""6.  La tienda de departamentos Friendly ha sido objeto de muchos robos durante el último mes; pero debido al aumento a las medidas de seguridad, se han detenido 250 ladrones. Se registró el sexo de cada ladrón; también se anotó si se trataba de un primer delito o era reincidente. Los datos se resumen en la siguiente tabla.

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
    # Datos correctos
    hombres = np.array([60, 70])   # Primera ofensa, reincidente
    mujeres = np.array([44, 76])   # Primera ofensa, reincidente

    total_hombres = np.sum(hombres)     # 130
    total_mujeres = np.sum(mujeres)     # 120
    total_ladrones = total_hombres + total_mujeres  # 250

    # Probabilidad de que sea hombre
    p_hombre = total_hombres / total_ladrones

    # Probabilidad de primera ofensa dado que es hombre
    # P(Primera ofensa | Hombre) = (Número hombres primera ofensa) / (Total hombres)
    p_po_hombre = hombres[0] / total_hombres

    return (p_hombre, p_po_hombre)

probabilidad_condicional()


"""Contesta las siguientes preguntas
Definición del Problema:

7. ¿Cuál es el problema específico que se desea resolver con la minería de datos?
8. ¿Por qué es importante resolver este problema?

Objetivos del Proyecto:

9. ¿Cuáles son los objetivos principales del anteproyecto?
10. ¿Qué resultados esperas obtener al final del proyecto?

Recolección de Datos:

11. ¿Qué tipo de datos se necesitarán para este proyecto?

"""
# Regresa una cadena de caracteres en cada función

def problema_especifico():
    cadena = "Predecir los resultados de los partidos de la MLS utilizando datos históricos y estadísticas actuales."
    return cadena

def importancia():
    cadena = "Porque permite mejorar la toma de decisiones en apuestas deportivas, estrategias de equipos y análisis de rendimiento."
    return cadena

def objetivos():
    cadena = ("Recolectar datos históricos de partidos, estadísticas de jugadores y equipos, "
              "entrenar modelos predictivos y evaluar su precisión para pronosticar resultados.")
    return cadena

def tipo_de_datos():
    cadena = ("Datos históricos de partidos, estadísticas individuales y de equipo, información de lesiones y condiciones del partido.")
    return cadena
