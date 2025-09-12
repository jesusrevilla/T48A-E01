
import numpy as np
import pandas as pd

# Importante: verifica que tu nombre y número de matrícula esten correctos

nombre = "Moreno Solis Gisela Geraldine"
numero_de_matricula = 176522
fecha = '2025-11-09'

## 2.   El 30 de junio de 1992, la capitalización de mercados de valores del Pacífico y Asia fue:   

def capitalizacion():
    datos = [17, 21, 44, 50, 79, 86, 140, 178, 203]
    
    media = np.mean(datos)
    mediana = np.median(datos)
    moda = pd.Series(datos).mode()[0]  
    desviacion = np.std(datos, ddof=1) 
    
    return (media, mediana, moda, desviacion)


resultado = capitalizacion()
print(resultado)

## 3. Utiliza los datos proporcionados para calcular lo que se te solicita en el docstring

def asistencia_dispersion():
    """
    La asistencia a los 10 últimos partidos en casa de las Águilas de Baltimore fue la siguiente:   
    [20100, 24500, 31600, 28400, 49500, 19350, 25600, 30600, 11300, 28560]    

    Calcula rango, varianza y desviación estándar.  
    Regresa una tupla: (rango, varianza, desv_est)
    """
    datos = np.array([20100, 24500, 31600, 28400, 49500, 19350, 25600, 30600, 11300, 28560])
    
    rango = np.max(datos) - np.min(datos)
    varianza = np.var(datos, ddof=1)  # varianza muestral
    desv_est = np.std(datos, ddof=1)  # desviación estándar muestral
    
    return (rango, varianza, desv_est)

# Ejecutar la función
resultado = asistencia_dispersion()
print(resultado)

## 4.    Genere un histograma de las siguientes calificaciones en el examen parcial:

def histograma_np():
    """
    Nota: regrese el histograma generado con la función de numpy, no genere la gráfica
    """
    calificaciones = [7.9, 7.8, 7.8, 6.7, 7.6, 8.7, 8.5, 7.3, 6.6, 9.9, 8.4, 7.2,
                     6.6, 5.7, 9.4, 8.4, 7.2, 6.3, 5.1, 4.8, 5.0, 6.1, 7.1, 8.2,
                     9.3, 10.0, 8.9]
    
    # np.histogram devuelve: (frecuencias, bins)
    hist, bins = np.histogram(calificaciones, bins='auto')  # 'auto' deja que numpy decida
    return hist, bins

# Ejecutar la función
frecuencias, intervalos = histograma_np()
print("Frecuencias:", frecuencias)
print("Bins:", intervalos)


## 5.    Analiza la correlación entre los datos de Tamaño y Precio y Regresa el coeficiente de Pearson

def correlacion():
    # Datos
    tamaño = np.array([100, 120, 140, 160, 180, 200, 220, 240, 260, 280])
    precio = np.array([1305710, 1658277, 1894167, 2136552, 2298267, 
                       2553624, 2780503, 3289726, 3472743, 3779477])
    
    # Matriz de correlación
    coef_matrix = np.corrcoef(tamaño, precio)
    
    # Coeficiente de Pearson entre las dos variables
    coef_pearson = coef_matrix[0, 1]
    
    return coef_pearson

# Ejecutar la función
resultado = correlacion()
print("Coeficiente de Pearson:", resultado)

## 6.        Resuelve el siguiente ejercicio de probabilidad condicional

def probabilidad_condicional():
    # Datos
    hombres_primera = 60
    hombres_reincidente = 70
    mujeres_primera = 44
    mujeres_reincidente = 76

    total_hombres = hombres_primera + hombres_reincidente
    total_ladrones = total_hombres + mujeres_primera + mujeres_reincidente

    # Probabilidad de que sea hombre
    p_hombre = total_hombres / total_ladrones

    # Probabilidad de primera ofensa dado que es hombre
    p_po_hombre = hombres_primera / total_hombres

    return (p_hombre, p_po_hombre)

resultado = probabilidad_condicional()
print(resultado)


# -------------------------------------------------------
# Definición del Problema
# -------------------------------------------------------

# 7. ¿Cuál es el problema específico que se desea resolver con la minería de datos?
# Una tienda en línea quiere predecir qué clientes tienen mayor probabilidad de abandonar el servicio
# o dejar de comprar, para implementar estrategias de retención antes de que esto ocurra.

# 8. ¿Por qué es importante resolver este problema?
# Resolver este problema permite a la tienda reducir la pérdida de clientes, aumentar ingresos,
# personalizar estrategias de marketing y tomar decisiones basadas en datos reales.

# -------------------------------------------------------
# Objetivos del Proyecto
# -------------------------------------------------------

# 9. ¿Cuáles son los objetivos principales del anteproyecto?
# - Analizar los datos históricos de los clientes y compras.
# - Detectar patrones de comportamiento que indiquen riesgo de abandono.
# - Construir un modelo predictivo que identifique clientes con alta probabilidad de abandono.
# - Proporcionar recomendaciones para acciones preventivas (ofertas, recordatorios, incentivos).

# 10. ¿Qué resultados esperas obtener al final del proyecto?
# - Un modelo que clasifique clientes según su riesgo de abandono.
# - Reportes claros con visualizaciones de los patrones más relevantes.
# - Estrategias concretas para retener clientes con alta probabilidad de dejar de comprar.

# -------------------------------------------------------
# Recolección de Datos
# -------------------------------------------------------

# 11. ¿Qué tipo de datos se necesitarán para este proyecto?
# - Datos cuantitativos: cantidad de compras, frecuencia de visitas, gasto promedio.
# - Datos cualitativos: tipo de cliente, región, canal de compra preferido.
# - Datos históricos de comportamiento y compras recientes.
# - Fuentes confiables: base de datos de la tienda, registros de transacciones, encuestas de satisfacción.


def problema_especifico():
    return ("Una tienda en línea quiere predecir qué clientes tienen mayor "
            "probabilidad de abandonar el servicio o dejar de comprar, para implementar estrategias de retención.")

def importancia():
    return ("Resolver este problema permite reducir la pérdida de clientes, aumentar ingresos, "
            "personalizar estrategias de marketing y tomar decisiones basadas en datos reales.")

def objetivos():
    return ("1. Analizar datos históricos de clientes y compras.\n"
            "2. Detectar patrones de comportamiento que indiquen riesgo de abandono.\n"
            "3. Construir un modelo predictivo que identifique clientes con alta probabilidad de abandono.\n"
            "4. Proporcionar recomendaciones para acciones preventivas (ofertas, recordatorios, incentivos).")

def tipo_de_datos():
    return ("Se necesitarán datos cuantitativos (frecuencia de compras, gasto promedio), "
            "cualitativos (tipo de cliente, región, canal de compra), históricos de comportamiento "
            "y compras recientes, provenientes de bases de datos internas y encuestas de satisfacción.")

# Ejecutar y mostrar resultados
print(problema_especifico())
print(importancia())
print(objetivos())
print(tipo_de_datos())
