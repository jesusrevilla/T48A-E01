import numpy as np
from scipy import stats
# Importante: verifica que tu nombre y número de matrícula esten correctos

nombre = "Yeray Alejandro Ojeda Rodriguez"
numero_de_matricula = 173357
fecha = '2025-11-09'

#Ejercicio 2
def capitalizacion():
    # inserta tu código aquí
    arr=np.array([17, 21, 44, 50, 79, 86, 140, 178, 203])

    media = np.mean(arr)
    mediana = np.median(arr)
    moda=stats.mode(arr)
    desv_est = np.std(arr)
    return (media, mediana, moda, desv_est)

#Ejercicio 3

def asistencia_dispersion():
    """
    La aistencia a los 10 últimos partidos en casa de las Águilas de Baltimore fue la siguiente:   

    [20100, 24500, 31600, 28400, 49500, 19350, 25600, 30600, 11300, 28560]    

    Calcule el rango, la varianza y la desviación stándard para estos datos   
    Regrese una tupla con el siguiente orden, como se muestra a continuación:
    """
    # inserta tu código aquí
    asistencia = [20100, 24500, 31600, 28400, 49500, 19350, 25600, 30600, 11300, 28560]
    rango = np.max(asistencia) - np.min(asistencia)
    varianza = np.var(asistencia)
    desv_est = np.std(asistencia)
    return (rango, varianza, desv_est)

#Ejercicio 4
def histograma_np():
    """
    Nota: regrese el histograma generado con la función de numpy, no genere la gráfica
    """
    calificaciones = [7.9, 7.8, 7.8, 6.7, 7.6, 8.7, 8.5, 7.3, 6.6, 9.9, 8.4, 7.2,
                      6.6, 5.7, 9.4, 8.4, 7.2, 6.3, 5.1, 4.8, 5.0, 6.1, 7.1, 8.2,
                      9.3, 10.0, 8.9]

    histograma= np.histogram(calificaciones)
    return (histograma)

#Ejercicio 5
def correlacion():
    """
    Analiza la correlación entre los datos de Tamaño y Precio y Regresa el coeficiente de Pearson
    """
    tamaño = np.array([100, 120, 140, 160, 180, 200, 220, 240, 260, 280])
    precio = np.array([1305710, 1658277, 1894167, 2136552, 2298267, 2553624, 2780503, 3289726, 3472743, 3779477])
    coeficiente_pearson = np.corrcoef(tamaño, precio)[0, 1]
    
    return coeficiente_pearson  

#Ejercicio 6
def probabilidad_condicional():
    hombres_primera_ofensa = 60
    hombres_reincidente = 70
    mujeres_primera_ofensa = 44
    mujeres_reincidente = 76

    total_hombres = hombres_primera_ofensa + hombres_reincidente
    total_ladrones = total_hombres + mujeres_primera_ofensa + mujeres_reincidente

    p_hombre = total_hombres / total_ladrones

    p_po_hombre = hombres_primera_ofensa / total_hombres
    
    return (p_hombre, p_po_hombre)

#Ejercicio 7, 8, 9, 10 y 11

# Regresa una cadena de caracteres en cada función

def problema_especifico():
    return "El problema especifico que busca resolver la minería de datos es descubrir patrones, tendencias, anomalías y conocimiento útil que están ocultos en grandes volúmenes de datos "

def importancia():
    return "La importancia de resolver este problema viene de encontrar los patrones, anomalías y correlaciones ocultas para obtener conocimiento"

def objetivos():
    return "Sus objetivos principales son: Descubrir patrones y tendencias, realizar predicciones, extraer conocimiento, mejorar tomas de decisiones"

def resultados():
    return "Se espera que al finalizar el proyecto se pueda concluir con un conocimiento adquirido útil para mí como alumno y poder usarlo en ambitos laborales"

def tipo_de_datos():
    return "Se necesitarán datos estructurados, semiestructurados, no estructurados, númericos, categóricos, boleanos, de texto y temporales"
