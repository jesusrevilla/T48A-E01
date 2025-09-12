#1. Importe numpy solo una vez, como se muestra a continuación:
import numpy as np 
# Importante: verifica que tu nombre y número de matrícula esten correctos
nombre = "Areli Alejandra Cuevas González"
numero_de_matricula = 175454
fecha = '2025-11-09'


#2. El 30 de junio de 1992, la capitalización de mercados de valores del Pacífico y Asia fue....
#a)Encuentre la media aritmetica de los datos
#b)Encuentre la mediana de los datos
#c)Encuentre la moda de los datos
#d)Encuentre la desviacion estandar de los datos
#Regrese una tupla en el siguiente orden.

def capitalizacion():
    dat = np.array([17, 21, 44, 50, 79, 86, 140, 178, 203], dtype=float)
    media = float(np.mean(dat))
    mediana = float(np.median(dat))
    valores, cuentas = np.unique(dat, return_counts=True)
    max_cuenta = np.max(cuentas)
    if max_cuenta == 1:
        moda = np.nan
    else:
        moda = float(valores[np.argmax(cuentas)])
    desv_est = float(np.std(dat, ddof=0))
  
    return (media, mediana, moda, desv_est)
capitalizacion()


#3. Utiliza los datos proporcionados para calcular lo que se te solicita en el docstring

def asistencia_dispersion():
    """
    La aistencia a los 10 últimos partidos en casa de las Águilas de Baltimore fue la siguiente:   

    [20100, 24500, 31600, 28400, 49500, 19350, 25600, 30600, 11300, 28560]    

    Calcule el rango, la varianza y la desviación stándard para estos datos   
    Regrese una tupla con el siguiente orden, como se muestra a continuación:
    """
    visitas = np.array([20100, 24500, 31600, 28400, 49500, 19350, 25600, 30600, 11300, 28560], dtype=float)

    rango = float(np.max(visitas) - np.min(visitas)) #rango
    varianza = float(np.var(visitas, ddof=0))  # varianza poblacional
    desv_est = float(np.std(visitas, ddof=0))  # desviación estándar poblacional

    return (rango, varianza, desv_est)
asistencia_dispersion()


# 4. Genere un histograma de las siguientes calificaciones en el examen parcial
def histograma_np():
    """
    Nota: regrese el histograma generado con la función de numpy, no genere la gráfica
    """
    calis = [7.9, 7.8, 7.8, 6.7, 7.6, 8.7, 8.5, 7.3, 6.6, 9.9, 8.4, 7.2,
                      6.6, 5.7, 9.4, 8.4, 7.2, 6.3, 5.1, 4.8, 5.0, 6.1, 7.1, 8.2,
                      9.3, 10.0, 8.9]
    hist = np.histogram(np.array(calis, dtype=float))
    return hist


# 5. Analiza la correlación entre los datos de Tamaño y Precio y Regresa el coeficiente de Pearson
def correlacion():
    tam = np.array([100, 120, 140, 160, 180, 200, 220, 240, 260, 280], dtype=float)
    precio = np.array([1305710, 1658277, 1894167, 2136552, 2298267, 2553624, 2780503, 3289726, 3472743, 3779477], dtype=float)

    # Coeficiente de Pearson usando np.corrcoef
    r = float(np.corrcoef(tam, precio)[0, 1])
    return r

    
# 6. Resuelve el siguiente ejercicio de probabilidad condicional
def probabilidad_condicional():
    total = 250
    total_hombres = 60 + 70
    p_hombre = total_hombres / total  # 130/250 = 0.52

    p_po_hombre = 60 / total_hombres  # P(Primera | Hombre) = 60/130

    return (p_hombre, p_po_hombre)


# 7–11. Respuestas en cadena de texto
'''
Definición del Problema
El problema específico que se desea resolver es predecir la demanda de productos 
en tiendas OXXO para optimizar inventarios, reducir quiebres de stock y evitar pérdidas
por sobreinventario o productos caducos.
'''

# Regresa una cadena de caracteres en cada función

def problema_especifico():
    return "Predecir la demanda de productos en tiendas OXXO para optimizar inventarios, reducir quiebres de stock y evitar pérdidas por sobreinventario o productos caducos."


def importancia():
    return "Es importante porque ayuda a mantener la disponibilidad en anaquel, disminuir pérdidas económicas por mermas o caducidad, optimizar la logística de reabastecimiento y aumentar las ventas y la satisfacción del cliente."


def objetivos():
    return ("Analizar patrones de venta diarios por tienda y categoría, identificar factores que influyen en la demanda "
            "y proponer estrategias de reabastecimiento. Como resultados se espera lograr pronósticos más precisos, "
            "reducir quiebres de stock, minimizar mermas y mejorar la rentabilidad.")


def tipo_de_datos():
    return ("Histórico de ventas por tienda (fecha, hora, cantidad, precio), inventarios iniciales y finales, "
            "información de promociones y descuentos de la tienda, además del catálogo de productos con su categoría, vida útil y rotación.")
 

