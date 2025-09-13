import numpy as np

nombre = "Jair de Jesus Nieto"
numero_de_matricula = 171676
fecha = '2025-11-09'

def capitalizacion():
    data = np.array([17, 21, 44, 50, 79, 86, 140, 178, 203])
    media = np.mean(data)
    mediana = np.median(data)
    #moda = stats.mode(data).mode[0]
    desv_est = np.std(data)
    return (media, mediana, desv_est)

def asistencia_dispersion():
    data = np.array([20100, 24500, 31600, 28400, 49500, 19350, 25600, 30600, 11300, 28560])
    rango = np.ptp(data)
    varianza = np.var(data)
    desv_est = np.std(data)
    return (rango, varianza, desv_est)

def histograma_np():
    calificaciones = [7.9, 7.8, 7.8, 6.7, 7.6, 8.7, 8.5, 7.3, 6.6, 9.9, 8.4, 7.2,
                     6.6, 5.7, 9.4, 8.4, 7.2, 6.3, 5.1, 4.8, 5.0, 6.1, 7.1, 8.2,
                     9.3, 10.0, 8.9]
    hist, bin_edges = np.histogram(calificaciones)
    return (hist, bin_edges)

def correlacion():
    tamaño = np.array([100, 120, 140, 160, 180, 200, 220, 240, 260, 280])
    precio = np.array([1305710, 1658277, 1894167, 2136552, 2298267, 2553624, 2780503, 3289726, 3472743, 3779477])
    coeficiente_pearson = np.corrcoef(tamaño, precio)[0, 1]
    return coeficiente_pearson

def probabilidad_condicional():
    total_hombres = 60 + 70
    total_ladrones = 60 + 70 + 44 + 76
    p_hombre = total_hombres / total_ladrones
    p_po_y_hombre = 60 / total_ladrones
    p_po_hombre = p_po_y_hombre / p_hombre
    return (p_hombre, p_po_hombre)

# Contesta las siguientes preguntas
# Definición del Problema:

# 7. ¿Cuál es el problema específico que se desea resolver con la minería de datos?
#Extraer datos importantes de grandes cantidades de datos
# 8. ¿Por qué es importante resolver este problema?
#Porque nos permite manejar informacion relevante de cantidades enormes de datos
# Objetivos del Proyecto:

# 9. ¿Cuáles son los objetivos principales del anteproyecto?
#Definir los parametros con los que trabajara el proyecto y establecer su alcanze
# 10. ¿Qué resultados esperas obtener al final del proyecto?
#Un mejor entendimiento de la mineria de datos y sus aplicaciones
# Recolección de Datos:

# 11. ¿Qué tipo de datos se necesitarán para este proyecto?
#Informacion de contacto, calificaciones
# Regresa una cadena de caracteres en cada función
def problema_especifico():
    return "El problema especifico es usar mineria de datos en un entorno escolar"
    pass
def importancia():
    return "La importancia es aplicar mis conocimientos en un escenario controlado"
    pass
def objetivos():
    return "Los objetivos son practicar y entender mejor los temas de clase"
    pass
def tipo_de_datos():
    return "Informacion personal y calificaciones"
    pass
