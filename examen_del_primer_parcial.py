#1. Importe numpy solo una vez, como se muestra a continuación:
import numpy as np

# Importante: verifica que tu nombre y número de matrícula esten correctos
nombre = "Cristopher Leonardo Bustamante Rocha"
numero_de_matricula = 173754
fecha = '2025-11-09'

#2. El 30 de junio de 1992, la capitalización de mercados de valores del Pacífico y Asia fue:
"""
País	Capitalización (en miles de millones de dólares)
Filipinas	17
Indonesia	21
Tailandia	44
Singapur	50
Malasia	79
Corea del Sur	86
Taiwan	140
Hong Kong	178
Australia	203
a) Encuentre la media aritmética de los datos
b) Encuentre la mediana de los datos
c) Encuentre la moda de los datos
e) Encuentre la desviación estándar de los datos

regrese una tupla en el siguiente orden, como se muestra abajo:
"""
def capitalizacion():
    datos_paises = np.array([17, 21, 44, 50, 79, 86, 140, 178, 203], dtype=float)
    media = float(np.mean(datos_paises))
    mediana = float(np.median(datos_paises))
    valores, cuentas = np.unique(datos_paises, return_counts=True)
    max_cuenta = np.max(cuentas)
    
    if max_cuenta == 1:
        moda = np.nan
    else:
        moda = float(valores[np.argmax(cuentas)])

    desv_est = float(np.std(datos_paises, ddof=0)) 
    return (media, mediana, desv_est)

#3. Utiliza los datos proporcionados para calcular lo que se te solicita en el docstring
    """
    La aistencia a los 10 últimos partidos en casa de las Águilas de Baltimore fue la siguiente:   

    [20100, 24500, 31600, 28400, 49500, 19350, 25600, 30600, 11300, 28560]    

    Calcule el rango, la varianza y la desviación stándard para estos datos   
    Regrese una tupla con el siguiente orden, como se muestra a continuación:
    """
def asistencia_dispersion():
    asistencia = np.array([20100, 24500, 31600, 28400, 49500, 19350, 25600, 30600, 11300, 28560], dtype=float)
    rango = float(np.max(asistencia) - np.min(asistencia))
    varianza = float(np.var(asistencia, ddof=0))  
    desv_est = float(np.std(asistencia, ddof=0))  
    return (rango, varianza, desv_est)

#4. Genere un histograma de las siguientes calificaciones en el examen parcial:
"""
    Nota: regrese el histograma generado con la función de numpy, no genere la gráfica
    """
def histograma_np():
    calificaciones = [7.9, 7.8, 7.8, 6.7, 7.6, 8.7, 8.5, 7.3, 6.6, 9.9, 8.4, 7.2,
                     6.6, 5.7, 9.4, 8.4, 7.2, 6.3, 5.1, 4.8, 5.0, 6.1, 7.1, 8.2,
                     9.3, 10.0, 8.9]
    histo = np.histogram(np.array(calificaciones, dtype=float))
    return histo

#5. Analiza la correlación entre los datos de Tamaño y Precio y Regresa el coeficiente de Pearson
"""
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
    tam = np.array([100, 120, 140, 160, 180, 200, 220, 240, 260, 280], dtype=float)
    precio = np.array([1305710, 1658277, 1894167, 2136552, 2298267, 2553624, 2780503, 3289726, 3472743, 3779477], dtype=float)
    cope = float(np.corrcoef(tam, precio)[0, 1])
    return cope

#6. Resuelve el siguiente ejercicio de probabilidad condicional
"""
La tienda de departamentos Friendly ha sido objeto de muchos robos durante el último mes; pero debido al aumento a las medidas de seguridad, 
se han detenido 250 ladrones. Se registró el sexo de cada ladrón; también se anotó si se trataba de un primer delito o era reincidente. 
Los datos se resumen en la siguiente tabla

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
    total_hombres = 130
    p_hombre = total_hombres / total  
    p_po_hombre = 60 / total_hombres  

    return (p_hombre, p_po_hombre)

#Contesta las siguientes preguntas
"""
Definicion del problema: El problema específico que se desea resolver es predecir la asistencia a las salas de cine considerando factores como género de la película, 
clasificación, día de la semana, temporada del año, precio del boleto y promociones. Con esta información, las cadenas de cine podrán anticipar la demanda 
y optimizar sus recursos
"""
#7. ¿Cuál es el problema específico que se desea resolver con la minería de datos?
#8. ¿Por qué es importante resolver este problema?
"""
Objetivos del Proyecto: 
Analizar los patrones de asistencia a funciones de cine en diferentes contextos (género, horarios, promociones, temporadas)
Identificar los factores clave que más influyen en la asistencia
Construir un modelo predictivo que estime la cantidad de asistentes a una función determinada
Generar recomendaciones para maximizar la ocupación de las salas y mejorar la rentabilidad
"""

#9. ¿Cuáles son los objetivos principales del anteproyecto?
#10. ¿Qué resultados esperas obtener al final del proyecto?
"""
Recoleccion de datos:
Datos históricos de boletos vendidos por función (fecha, hora, sala)
Información de cada película (título, género, duración, clasificación, productora)
Variables externas: precio del boleto, promociones, días festivos, estrenos importantes
Datos demográficos de la zona: edad, nivel socioeconómico, hábitos de consumo de cine
"""
#11. ¿Qué tipo de datos se necesitarán para este proyecto?
# Regresa una cadena de caracteres en cada función


def problema_especifico():
    return "Predecir la demanda diaria por tienda y por categoría/SKU en una cadena tipo OXXO para optimizar inventarios, reducir quiebres de stock y minimizar mermas"

def importancia():
    return "Permite mejorar la disponibilidad en anaquel, disminuir pérdidas por sobreinventario y caducidad, optimizar la logística de reposición y aumentar ventas y satisfacción del cliente"

def objetivos():
    return ("1) Analizar patrones de venta por tienda, día y categoría (horas pico, estacionalidad, promociones) "
            "2) Factores que influyen (clima, festividades, cercanía a escuelas/oficinas) "
            "3) Construir un modelo predictivo de demanda por tienda "
            "4) Diseñar una política de reabastecimiento basada en los pronósticos")

def tipo_de_datos():
    return ("Histórico de ventas por tienda (fecha, hora, cantidad, precio), inventario inicial y final, "
            "aplicación de descuentos, calendario de festividades, datos de clima por zona, "
            "atributos de tienda (ubicación, afluencia, formato, horario) y catálogo de productos (categoría, vida útil)")
