import numpy as np
import matplotlib.pyplot as plt

# Importante: verifica que tu nombre y número de matrícula estén correctos
nombre = "César Alejandro Cerrillo Domínguez"
numero_de_matricula = 179289
fecha = '2025-02-26'

# 1. Capitalización de mercados de valores del Pacífico y Asia
datos = np.array([17, 21, 44, 50, 79, 86, 140, 178, 203])

def capitalizacion():
    media = np.mean(datos)
    mediana = np.median(datos)
    desv_est = np.std(datos)
    return (media, mediana, desv_est)

# 2. Asistencia a los 10 últimos partidos en casa de las Águilas de Baltimore
partidos = np.array([20100, 24500, 31600, 28400, 49500, 19350, 25600, 30600, 11300, 28560])

def asistencia_dispersion():
    rango = np.max(partidos) - np.min(partidos)
    varianza = np.var(partidos)
    desv_est = np.std(partidos)
    return (rango, varianza, desv_est)

# 3. Histograma de calificaciones en el examen parcial
data = np.array([7.9, 7.8, 7.8, 6.7, 7.6, 8.7, 8.5, 7.3, 6.6, 9.9, 8.4, 7.2, 6.6, 5.7, 9.4, 8.4, 7.2, 6.3, 5.1, 4.8, 5.0, 6.1, 7.1, 8.2, 9.3, 10.0, 8.9])

def histograma_np():
    return np.histogram(data, bins=10)

# 4. Correlación entre Tamaño y Precio
def correlacion():
    x = np.array([100, 120, 140, 160, 180, 200, 220, 240, 260, 280])
    y = np.array([1305710, 1658277, 1894167, 2136552, 2298267, 2553624, 2780503, 3289726, 3472743, 3779477])

    mean_x = np.mean(x)
    mean_y = np.mean(y)

    deviation_x = x - mean_x
    deviation_y = y - mean_y

    product_deviations = deviation_x * deviation_y

    sum_product_deviations = np.sum(product_deviations)

    std_x = np.std(x)
    std_y = np.std(y)

    r = sum_product_deviations / ((len(x) - 1) * std_x * std_y)
    return r

# 5. Probabilidades de ladrones detenidos
def calcular_probabilidades():
    hombres_primera_ofensa = 60
    hombres_reincidente = 70
    mujeres_primera_ofensa = 44
    mujeres_reincidente = 76

    total_ladrones = hombres_primera_ofensa + hombres_reincidente + mujeres_primera_ofensa + mujeres_reincidente

    p_hombre = (hombres_primera_ofensa + hombres_reincidente) / total_ladrones

    p_po_hombre = hombres_primera_ofensa / (hombres_primera_ofensa + hombres_reincidente)

    return (p_hombre, p_po_hombre)

# Respuestas a preguntas
def problema_especifico():
    return """
    El problema específico es cuando se requiere predecir valores futuros no conocibles, a partir de un gran conjunto de datos.
    """

def importancia():
    return """
    Permite tomar decisiones correctas y basadas en datos, para tener un mejor control de las acciones que se desean realizar.
    """

def objetivos():
    return """
    Descubrir posibles datos futuros, haciendo previsaulizaciones de datos futuros.
    """

def tipo_de_datos():
    return """
    Comportamiento, transaccionales, demográficos, etc.
    """
