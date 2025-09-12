
import numpy as np

# Importante: verifica que tu nombre y número de matrícula esten correctos

nombre = "Saúl Eduardo Juárez Villela"
numero_de_matricula = 179263
fecha = '2025-11-09'

def capitalizacion():
  # inserta tu código aquí
  datos =[17, 21, 44, 50, 79, 86, 140, 178, 203]
 
  # Media
  media = np.mean(datos)
 
  # Mediana
  mediana = np.median(datos)

  #moda
  moda = 0
  
  # Desviación estándar
  desv_est = np.std(datos)
 
  return (media, mediana, moda, desv_est)
 
capitalizacion()

def asistencia_dispersion():
  Aguilas =[20100, 24500, 31600, 28400, 49500, 19350, 25600, 30600, 11300, 28560]
  # Rango
  rango=np.ptp(Aguilas)
 
  # Varianza
  varianza=np.var(Aguilas)
 
  # Desviación estandar
  desv_est=np.std(Aguilas)
 
  return (rango, varianza, desv_est)
 
asistencia_dispersion()


def histograma_np():
    """
    Nota: regrese el histograma generado con la función de numpy, no genere la gráfica
    """
    calificaciones = [7.9, 7.8, 7.8, 6.7, 7.6, 8.7, 8.5, 7.3, 6.6, 9.9, 8.4, 7.2,
                      6.6, 5.7, 9.4, 8.4, 7.2, 6.3, 5.1, 4.8, 5.0, 6.1, 7.1, 8.2,
                      9.3, 10.0, 8.9]

    histograma = np.histogram(calificaciones, bins=10)
    return histograma

histograma_np()

def correlacion():
  # Datos de ejemplo
  x = np.array([100,120,140,160,180,200,220,240,260,280])
  y = np.array([1305710, 1658277, 1894167, 2136552, 2298267, 2553624, 2780503, 3289726, 3472743, 3779477])
 
  # Calcular la media
  mean_x = np.mean(x)
  mean_y = np.mean(y)
 
  # Calcular las desviaciones
  deviation_x = x - mean_x
  deviation_y = y - mean_y
 
  # Calcular el producto de las desviaciones
  product_deviations = deviation_x * deviation_y
 
  # Sumar los productos de las desviaciones
  sum_product_deviations = np.sum(product_deviations)
 
  # Calcular la desviación estándar
  std_x = np.std(x, ddof=1)
  std_y = np.std(y, ddof=1)

  r = sum_product_deviations / ((len(x) - 1) * std_x * std_y)
 
  return r
 
correlacion()

def probabilidad_condicional():
    total_ladrones = 250
    hombres_primera_ofensa = 60
    hombres_reincidente = 70
    total_hombres = hombres_primera_ofensa + hombres_reincidente

    p_hombre = total_hombres / total_ladrones
    p_po_hombre = hombres_primera_ofensa / total_hombres

    return (p_hombre, p_po_hombre)
probabilidad_condicional()

## 7.     ¿Cuál es el problema específico que se desea resolver con la minería de datos?
## 8.     ¿Por qué es importante resolver este problema?


## 9.     ¿Cuáles son los objetivos principales del anteproyecto?
## 10.     ¿Qué resultados esperas obtener al final del proyecto?


## 11.    ¿Qué tipo de datos se necesitarán para este proyecto?

def problema_especifico():
  texto=""
  return texto

def importancia():
  texto=""
  return texto
  
def objetivos():
  texto=""
  return texto

def tipo_de_datos():
  texto=""
  return texto
