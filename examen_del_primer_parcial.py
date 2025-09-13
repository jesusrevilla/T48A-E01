import numpy as np
import pandas as pd

# Importante: verifica que tu nombre y número de matrícula esten correctos

nombre = "Axel De Avila Martinez"
numero_de_matricula = 177499
fecha = '2025-11-09'

def capitalizacion():
    # inserta tu código aquí
    datos = [17, 21, 44, 50, 79, 86, 140, 178, 203]
    media = np.mean(datos)
    mediana = np.median(datos)
    moda = pd.Series(datos).mode()[0]
    desv_est = np.std(datos)
    return (media, mediana, desv_est, moda)

def asistencia_dispersion():
    # inserta tu código aquí:
    asistencias = [20100, 24500, 31600, 28400, 49500, 19350, 25600, 30600, 11300, 28560]
    rango = np.max(asistencias) - np.min(asistencias)
    varianza = np.var(asistencias)
    desv_est = np.std(asistencias)
    return (rango, varianza, desv_est)

def histograma_np():
    """
    Nota: regrese el histograma generado con la función de numpy, no genere la gráfica
    """
    calificaciones = [7.9, 7.8, 7.8, 6.7, 7.6, 8.7, 8.5, 7.3, 6.6, 9.9, 8.4, 7.2,
                     6.6, 5.7, 9.4, 8.4, 7.2, 6.3, 5.1, 4.8, 5.0, 6.1, 7.1, 8.2,
                     9.3, 10.0, 8.9]

    hist = np.histogram(calificaciones)  
    
    return (hist)


from scipy.stats import pearsonr
def correlacion():
    tamano = [100, 120, 140, 160, 180, 200, 220, 240, 260, 280]
    precio = [1385710, 1658277, 1894167, 2136552, 2298267, 2553624, 2788053, 3289726, 3472743, 3779477]

    coeficiente, _ = pearsonr(tamano, precio)
    
    return coeficiente


def probabilidad_condicional():
    hombres_primera_ofensa = 60
    hombres_reincidente = 70
    mujeres_primera_ofensa = 44
    mujeres_reincidente = 76

    total_ladrones = hombres_primera_ofensa + hombres_reincidente + mujeres_primera_ofensa + mujeres_reincidente
    total_hombres = hombres_primera_ofensa + hombres_reincidente

    p_hombre = total_hombres / total_ladrones
    p_po_hombre = hombres_primera_ofensa / total_hombres

    return (p_hombre, p_po_hombre)


def pregunta_7():
    ''' 7. ¿Cuál es el problema específico que se desea resolver con la minería de datos?'''
    respuesta = "la mala administracion y resolucion de probelmas que reflejan esos datos con los que se trabajan, trata de optimizar y entender para la correcta interpretacion de los y dar resolucion atraves de herramientas de programacion, estadisticas, etc."
    return respuesta

def pregunta_8():
    ''' ¿Por qué es importante resolver este problema?'''
    respuesta = "es importante para poder dar prediciones, para evitar o garantizar un futuro camino a exito para donde trabajas; e importante para que haya una correcta administracion y arrojamineto de los datos en casos especificos que se piden"
    return respuesta

def pregunta_9():
    ''' ¿Cuáles son los objetivos principales del anteproyecto?'''
    respuesta = "Establecer bien la problematica que hay ya sea en un entorno laboral o de proyecto, definir una solicion y plantear como se llevaria a cabo dicho proyecto para su mejora"
    return respuesta

def pregunta_10():
    ''' ¿Qué resultados esperas obtener al final del proyecto?'''
    respuesta = "Haber resuelto la problematica inicial que se identifico atraves de lo que se planteo para su solucion y llevado a cabo, de manera satisfactoria y puesto en marcha"
    return respuesta

'''11. ¿Qué tipo de datos se necesitarán para este proyecto?'''

# Regresa una cadena de caracteres en cada función

def problema_especifico():
    respuesta = "su origen, lo que le va ligado derivado de ese problema, o bien sus consecuencias, su causa, por ejemplo un mal manejo y erroneo de datos para una empresa de venta de consolas"
    return respuesta

def importancia():
    respuesta = "debido a los malos calculos de los datos, el muestreo o los histogramas no presentan bien los calculos de los datos o incluso hubo mal administracion de los datos, afectando asi sus ventas, predicciones y prevenciones"
    return respuesta

def objetivos():
    respuesta = "proporcionar la solucion de formulas, sofware y atajos para calculos basados en lo que administra la empresa de sus ventas; capacitar en el manejo de las nuevas herramientas; llevar a cabo el proceso asi de la mejora continua de lo ya implementado"
    return respuesta

def tipo_de_datos():
    respuesta = "numericos, listas, cadenas, graficos, de fechas incluso"
    return respuesta
