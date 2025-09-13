import numpy as np
from collections import Counter

# Importante: verifica que tu nombre y número de matrícula esten correctos

nombre = "José de Jeús González Rodríguez"
numero_de_matricula = 171877
fecha = '2025-11-09'

def capitalizacion():
    arr=np.array([17,21,44,50,79,86,140,178,203])
    media = np.mean(arr)
    mediana = np.median(arr)
    desv_est =np.std(arr)
    return (media, mediana, desv_est)
  
capitalizacion()


def asistencia_dispersion():
    """
    La aistencia a los 10 últimos partidos en casa de las Águilas de Baltimore fue la siguiente:   

    [20100, 24500, 31600, 28400, 49500, 19350, 25600, 30600, 11300, 28560]    

    Calcule el rango, la varianza y la desviación stándard para estos datos   
    Regrese una tupla con el siguiente orden, como se muestra a continuación:
    """
    arr = np.array([20100, 24500, 31600, 28400, 49500, 19350, 25600, 30600, 11300, 28560])

    rango = np.ptp(arr) 
    varianza = np.var(arr)
    desv_est = np.std(arr)
    return (rango, varianza, desv_est)
  
asistencia_dispersion()

def histograma_np():
    """
    Nota: regrese el histograma generado con la función de numpy, no genere la gráfica
    """
    calificaciones = [7.9, 7.8, 7.8, 6.7, 7.6, 8.7, 8.5, 7.3, 6.6, 9.9, 8.4, 7.2,
                     6.6, 5.7, 9.4, 8.4, 7.2, 6.3, 5.1, 4.8, 5.0, 6.1, 7.1, 8.2,
                     9.3, 10.0, 8.9]
    calificaciones_np = np.array(calificaciones)
    
    hist, bin_edges = np.histogram(calificaciones_np)
    return hist, bin_edges


histogram_data, bin_edges_data = histograma_np()
print("Histogram data:", histogram_data)
print("Bin edges:", bin_edges_data)


def correlacion():
    tamaño = np.array([100, 120, 140, 160, 180, 200, 220, 240, 260, 280])
    precio = np.array([1305710, 1658277, 1894167, 2136552, 2298267, 2553624, 2780503, 3289726, 3472743, 3779477])

    # Calcular el coeficiente de correlación de Pearson
    c= np.corrcoef(tamaño, precio)[0, 1]
    return c

    
    
correlacion()

def probabilidad_condicional():
    # Datos de la tabla
    hombres_primera = 60
    hombres_reincidente = 70
    mujeres_primera = 44
    mujeres_reincidente = 76
    
    # Total de ladrones detenidos
    total_ladrones = hombres_primera + hombres_reincidente + mujeres_primera + mujeres_reincidente
    
    # Probabilidad de que el ladrón sea hombre
    p_hombre = (hombres_primera + hombres_reincidente) / total_ladrones
    
    # Probabilidad de que sea primera ofensa dado que es hombre
    total_hombres = hombres_primera + hombres_reincidente
    p_po_hombre = hombres_primera / total_hombres
    
    return (p_hombre, p_po_hombre)

# Calcular y mostrar los resultados
p_hombre, p_po_hombre = probabilidad_condicional()
print(f"Probabilidad de que sea hombre: {p_hombre:.4f} ({p_hombre*100:.2f}%)")
print(f"Probabilidad de primera ofensa dado que es hombre: {p_po_hombre:.4f} ({p_po_hombre*100:.2f}%)")

# Regresa una cadena de caracteres en cada función

def problema_especifico():
    respuesta="El problema que se quiere resolver es predecir el exito comercial de los videojuegos"
    return respuesta

def importancia():
    respuesta="Es importante porque muchos juegos buenos fracasan por mal marketing o por salir en fechas malas, y otros juegos mid se venden como pan caliente. Así podemos ayudar a los devs a no quebrar"
    return respuesta

def objetivos():
    respuesta="Hacer una IA que sepa qué juegos van a sobresalir, Descubrir qué hace que un juego sea popular, y  Dar tips para que los juegos tengan más éxito en su lanzamiento."
    return respuesta

def tipo_de_datos():
    respuesta="Se necesitara el presupuesto de los juegos, cuánto tardaron en hacerlos, reviews de usuarios, horas que juega la gente, memes que genera el juego, y datos de ventas en diferentes plataformas"
    return respuesta

print("Problema específico:")
print(problema_especifico())
print("\nImportancia:")
print(importancia())
print("\nObjetivos:")
print(objetivos())
print("\nTipo de datos:")
print(tipo_de_datos())
