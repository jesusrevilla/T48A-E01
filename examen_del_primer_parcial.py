import numpy as np

# Importante: verifica que tu nombre y número de matrícula esten correctos

nombre = "Jose Armando Palomo Cerda"
numero_de_matricula = 175932
fecha = '2025-11-09'

# 2 El 30 de junio de 1992, la capitalización de mercados de valores del Pacífico y Asia fue:

def capitalizacion():
    data = np.array([17, 21, 44, 50, 79, 86, 140, 178, 203])
# a) Encuentre la media aritmética de los datos
    media = data.mean()
  # b) Encuentre la mediana de los datos
    mediana = np.median(data)
# c) Encuentre la moda de los datos
    # Verificar si hay moda
    if len(np.unique(data)) == len(data):
        moda = None   # No hay moda
    else:
        moda = np.bincount(data).argmax()
# e) Encuentre la desviación estándar de los datos 
    desv_est = data.std()

    return (media, mediana, moda, desv_est)

# 3 Utiliza los datos proporcionados para calcular lo que se te solicita en el docstring
def asistencia_dispersion():
  """
    La asistencia a los 10 últimos partidos en casa de las Águilas de Baltimore fue la siguiente:   

    [20100, 24500, 31600, 28400, 49500, 19350, 25600, 30600, 11300, 28560]    

    Calcule el rango, la varianza y la desviación estándar para estos datos   
    Regrese una tupla con el siguiente orden, como se muestra a continuación:
    (rango, varianza, desv_est)
    """
    datos = np.array([20100, 24500, 31600, 28400, 49500, 19350, 25600, 30600, 11300, 28560])
    rango = datos.max() - data.min()
    varianza = datos.var()
    desv_est = datos.std()
    return (rango, varianza, desv_est)

# 4 Genere un histograma de las siguientes calificaciones en el examen parcial:
def histograma_np():
    """
    Nota: regrese el histograma generado con la función de numpy, no genere la gráfica
    """
    calificaciones = [7.9, 7.8, 7.8, 6.7, 7.6, 8.7, 8.5, 7.3, 6.6, 9.9, 8.4, 7.2,
                     6.6, 5.7, 9.4, 8.4, 7.2, 6.3, 5.1, 4.8, 5.0, 6.1, 7.1, 8.2,
                     9.3, 10.0, 8.9]
    histograma = np.histogram(calificaciones, bins=5)
    return histograma
    pass

# 5 Analiza la correlación entre los datos de Tamaño y Precio y Regresa el coeficiente de Pearson
def correlacion():  
    tam = np.array([100,120,140,160,180,200,220,240,260,280])
    cost = np.array([1305710, 1658277, 1894167, 2136552, 2298267, 2553624, 2780503, 3289726, 3472743, 3779477])
    coeficiente = np.corrcoef(tam, cost)[0,1]

    return coeficiente
    pass

# 6 Resuelve el siguiente ejercicio de probabilidad condicional
"""
La tienda de departamentos Friendly ha sido objeto de muchos robos durante el último mes; 
pero debido al aumento a las medidas de seguridad, se han detenido 250 ladrones. 
Se registró el sexo de cada ladrón; también se anotó si se trataba de un primer delito o era reincidente. 
Los datos se resumen en la siguiente tabla.
Sexo	Primera ofensa	Reincidente
Hombre	60	70
Mujer	44	76
Suponga que se selecciona al azar un ladrón detenido, calcule
la probabilidad de que el ladrón sea hombre: p_hombre
la probabilidad de que sea la primera ofensa, dado que es hombre: p_po_hombre
Regrese ambos datos en una tupla con el siguiente orden (p_hombre, p_po_hombre)
"""
  def probabilidad_condicional():
    total = 250
    hombres = 130
    mujeres = 120
    # prob de que sea H
    p_hombre = hombres / total
    #prob de primera ofensa que sea hom
    p_po_hom = 60 / hombres
    return (p_hombre, p_po_hombre)

"""
7. ¿Cuál es el problema específico que se desea resolver con la minería de datos?

yo opino que sirven ppara manejar de forma eficiente una cantidad muy grande de datos y convertirla ern algo 
util paraa lo que sea que estemos investiganco como
Predicción de comportamientos
Detección de anomalías
Segmentación de datos
Descubrimiento de relaciones
Optimización de procesos
podria escoger el de optimizacion de procesos

8.  ¿Por qué es importante resolver este problema?
Trabajar en una optimizacion de procesos en base a una gama alta de datos en un club deportivo donde se hacen inscripciones de muchos niños es  importante el problema a resolver ya que se podria hacer una optimizacion de datos avismal lo que es invertir dinero y tiempo en personas que lo hagan fisicamente


. ¿Cuáles son los objetivos principales del anteproyecto?

Definir un problema, atacarlo y resolver ayudando a las pérsonas a que esto sea maseficiente

. ¿Qué resultados esperas obtener al final del proyecto?
en base a la recoleccion de datos entender que es lo mas importante y en base a esto crear una propuesta  yn despues una solucion

¿Qué tipo de datos se necesitarán para este proyecto?
datos como nombres, edades, fechas de naciimiento, gustos de cada niño de actividades depórtivas y juegosentre m,uchas cosas mas.
"""

def problema_especifico():
    return "yo opino que sirven ppara manejar de forma eficiente una cantidad muy grande de datos y convertirla ern algo ,util paraa lo que sea que estemos investiganco como Predicción de comportamientosDetección de anomalías,Segmentación de datos,Descubrimiento de relaciones,Optimización de procesos,podria escoger el de optimizacion de procesos"

def importancia():
    return "Trabajar en una optimizacion de procesos en base a una gama alta de datos en un club deportivo donde se hacen inscripciones de muchos niños es  importante el problema a resolver ya que se podria hacer una optimizacion de datos avismal lo que es invertir dinero y tiempo en personas que lo hagan fisicamente"

def objetivos():
    return "en base a la recoleccion de datos entender que es lo mas importante y en base a esto crear una propuesta  yn despues una solucion"

def tipo_de_datos():
    return "datos como nombres, edades, fechas de naciimiento, gustos de cada niño de actividades depórtivas y juegosentre m,uchas cosas mas."



  
