import numpy as np

# Información del alumno
nombre = "Moreno Solis Gisela Geraldine"
numero_de_matricula = 176522
fecha = '2025-11-09'


# 2. Capitalización: media, mediana, desviación estándar poblacional
def capitalizacion():
    datos = [17, 21, 44, 50, 79, 86, 140, 178, 203]
    media = np.mean(datos)
    mediana = np.median(datos)
    desviacion = np.std(datos)  # Poblacional (ddof=0)
    return (media, mediana, desviacion)


# 3. Asistencia: rango, varianza y desviación poblacional
def asistencia_dispersion():
    datos = np.array([20100, 24500, 31600, 28400, 49500,
                      19350, 25600, 30600, 11300, 28560])
    rango = np.max(datos) - np.min(datos)
    varianza = np.var(datos)  # Poblacional
    desv_est = np.std(datos)  # Poblacional
    return (rango, varianza, desv_est)


# 4. Histograma con 10 bins en el rango [4.8, 10]
def histograma_np():
    calificaciones = [7.9, 7.8, 7.8, 6.7, 7.6, 8.7, 8.5, 7.3,
                      6.6, 9.9, 8.4, 7.2, 6.6, 5.7, 9.4, 8.4,
                      7.2, 6.3, 5.1, 4.8, 5.0, 6.1, 7.1, 8.2,
                      9.3, 10.0, 8.9]
    hist, bins = np.histogram(calificaciones, bins=10, range=(4.8, 10))
    return hist, bins


# 5. Correlación de Pearson
def correlacion():
    tamaño = np.array([100, 120, 140, 160, 180, 200, 220, 240, 260, 280])
    precio = np.array([1305710, 1658277, 1894167, 2136552, 2298267,
                       2553624, 2780503, 3289726, 3472743, 3779477])
    return np.corrcoef(tamaño, precio)[0, 1]


# 6. Probabilidad condicional
def probabilidad_condicional():
    hombres_primera = 60
    hombres_reincidente = 70
    mujeres_primera = 44
    mujeres_reincidente = 76

    total_hombres = hombres_primera + hombres_reincidente
    total_ladrones = total_hombres + mujeres_primera + mujeres_reincidente

    p_hombre = total_hombres / total_ladrones
    p_po_hombre = hombres_primera / total_hombres

    return (p_hombre, p_po_hombre)


# 7-11: Texto del proyecto
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


