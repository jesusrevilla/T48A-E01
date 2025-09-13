import numpy as np

# Importante: verifica que tu nombre y número de matrícula esten correctos

nombre = "Mayeli Sánchez Ramírez"
numero_de_matricula = 173030
fecha = '2025-11-09'

def capitalizacion():
    datos = [17, 21, 44, 50, 79, 86, 140, 178, 203]
    media = np.mean(datos)
    mediana = np.median(datos)
    desv_est = np.std(datos, ddof=1)
    desv_est = np.std(datos)
    
    return (media, mediana, desv_est)

resultado = capitalizacion()
print(resultado)
  
def asistencia_dispersion():
    """
    La aistencia a los 10 últimos partidos en casa de las Águilas de Baltimore fue la siguiente:   

    [20100, 24500, 31600, 28400, 49500, 19350, 25600, 30600, 11300, 28560]    

    Calcule el rango, la varianza y la desviación stándard para estos datos   
    Regrese una tupla con el siguiente orden, como se muestra a continuación:
    """
    asistencias = [20100, 24500, 31600, 28400, 49500, 
                   19350, 25600, 30600, 11300, 28560]
    
    rango = max(asistencias) - min(asistencias)
    varianza = np.var(asistencias)         
    desv_est = np.std(asistencias)       
    return (rango, varianza, desv_est)

def histograma_np():
    """
    Nota: regrese el histograma generado con la función de numpy, no genere la gráfica
    """
    calis = [7.9, 7.8, 7.8, 6.7, 7.6, 8.7, 8.5, 7.3, 6.6, 9.9, 8.4, 7.2,
                      6.6, 5.7, 9.4, 8.4, 7.2, 6.3, 5.1, 4.8, 5.0, 6.1, 7.1, 8.2,
                      9.3, 10.0, 8.9]
    hist = np.histogram(np.array(calis, dtype=float))
    return hist


def correlacion():
    tamanio = np.array([100, 120, 140, 160, 180, 200, 220, 240, 260, 280])
    precio = np.array([1305710, 1658277, 1894167, 2136552, 2298267, 
                       2553624, 2780593, 3289726, 3472743, 3779477])
    
    coef = np.corrcoef(tamanio, precio)[0, 1]
    
    return coef

def probabilidad_condicional():
    total = 250
    hombres = 130
    primera_hombres = 60

    p_hombre = hombres / total

    p_po_hombre = primera_hombres / hombres

    return (p_hombre, p_po_hombre)

# Regresa una cadena de caracteres en cada función

def problema_especifico():
    return "Determinar la edad promedio de los alumnos y calcular el tiempo que tardan en graduarse, con el fin de identificar patrones y posibles retrasos en la conclusión de los estudios."

def importancia():
    return "Es importante porque permite detectar si los alumnos están tardando más de lo esperado en graduarse, lo cual ayuda a la universidad a implementar estrategias para mejorar la eficiencia terminal y apoyar a los estudiantes."

def objetivos():
    return "Analizar la distribución de edad de los estudiantes, calcular el tiempo promedio de graduación y detectar factores que influyen en el retraso, para ofrecer recomendaciones que mejoren la planeación académica."

def tipo_de_datos():
    return "Se necesitarán datos de edad, fecha de ingreso, fecha de egreso o graduación, carrera, semestre actual y estatus académico de los estudiantes."


