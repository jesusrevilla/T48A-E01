import numpy as np

# Importante: verifica que tu nombre y número de matrícula esten correctos

nombre = "Karla Julieta Torres Elias"
numero_de_matricula = 176336
fecha = '2025-11-09'

def capitalizacion():
    datos = np.array([17, 21, 44, 50, 79, 86, 140, 178, 203])
    media = np.mean(datos)
    mediana = np.median(datos)
    elementos_unicos, conteos = np.unique(datos, return_counts=True)
    moda = elementos_unicos[np.argmax(conteos)]
    desv_est = np.std(datos)
    return float (media, mediana,desv_est)

def asistencia_dispersion():
    """
    La aistencia a los 10 últimos partidos en casa de las Águilas de Baltimore fue la siguiente:

    [20100, 24500, 31600, 28400, 49500, 19350, 25600, 30600, 11300, 28560]

    Calcule el rango, la varianza y la desviación stándard para estos datos
    Regrese una tupla con el siguiente orden, como se muestra a continuación:
    """
    datos = np.array([20100, 24500, 31600, 28400, 49500, 19350, 25600, 30600, 11300, 28560])
    rango = np.ptp(datos) 
    varianza = np.var(datos)
    desv_est = np.std(datos)
    return (rango, varianza, desv_est)

def asistencia_dispersion():
    """
    La aistencia a los 10 últimos partidos en casa de las Águilas de Baltimore fue la siguiente:

    [20100, 24500, 31600, 28400, 49500, 19350, 25600, 30600, 11300, 28560]

    Calcule el rango, la varianza y la desviación stándard para estos datos
    Regrese una tupla con el siguiente orden, como se muestra a continuación:
    """
    datos = np.array([20100, 24500, 31600, 28400, 49500, 19350, 25600, 30600, 11300, 28560])
    rango = np.ptp(datos) # Peak-to-peak range
    varianza = np.var(datos)
    desv_est = np.std(datos)
    return (rango, varianza, desv_est)

def histograma_np():
    """
    Nota: regrese el histograma generado con la función de numpy, no genere la gráfica
    """
    calificaciones = [7.9, 7.8, 7.8, 6.7, 7.6, 8.7, 8.5, 7.3, 6.6, 9.9, 8.4, 7.2,
                     6.6, 5.7, 9.4, 8.4, 7.2, 6.3, 5.1, 4.8, 5.0, 6.1, 7.1, 8.2,
                     9.3, 10.0, 8.9]
    hist, bin_edges = np.histogram(calificaciones)
    return hist, bin_edges


def correlacion():
    tamaño = np.array([100, 120, 140, 160, 180, 200, 220, 240, 260, 280])
    precio = np.array([1305710, 1658277, 1894167, 2136552, 2298267, 2553624, 2780503, 3289726, 3472743, 3779477])
    coeficiente_pearson = np.corrcoef(tamaño, precio)[0, 1]
    return coeficiente_pearson

def probabilidad_condicional():
    hombres_primera = 60
    hombres_reincidente = 70
    mujeres_primera = 44
    mujeres_reincidente = 76
    total_ladrones = hombres_primera + hombres_reincidente + mujeres_primera + mujeres_reincidente

    # Calcular la probabilidad de que el ladron sea hombre
    total_hombres = hombres_primera + hombres_reincidente
    p_hombre = total_hombres / total_ladrones

    # Calcular la probabilidad de que sea el primer odensa
    p_primera_ofensa_y_hombre = hombres_primera / total_ladrones
    p_po_hombre = p_primera_ofensa_y_hombre / p_hombre
    return (p_hombre, p_po_hombre)

# Regresa una cadena de caracteres en cada función

def problema_especifico():
    respuesta = "ver como cambian el significado de os signos y planetas o que cosas tienen en comun con base a textos astrologicos pre-uranianos"
    return(respuesta)

def importancia():
    respuesta = "estandarizar las distintas tradiciones astrologicas asi como el rescate de el conocimietno antigua, tambien podria servir como apoyo para los estudios de astrologia moderna"
    return(respuesta)

def objetivos():
    respuesta = "comparar similitudes y diferenicas entre los diversos textos,recolectar y digitalizar estos textos,, identificar patrones de correspondencias, reprocesar los textos"
    return(respuesta)

def resultados():
    respuesta = "patrones escondidos revelados, que sea herramienta para investigadores, el ordenamiento de las correspondencias magicas en una base de datos"

def tipo_de_datos():
    respuesta = "los textos fuentes,datos contextuales como los diversos traductores y como se pudo perder el significado entre traducciones, datos linguisticos como los sinonimos o palabras especializadas (como conjunciones, oposiciones, encuadre etc),fechas, datos de correspondencia entre distintos textos"
    return(respuesta)
