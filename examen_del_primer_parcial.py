
import numpy as np

# Importante: verifica que tu nombre y número de matrícula esten correctos

nombre = "Saúl Eduardo Juárez Villela"
numero_de_matricula = 179263
fecha = '2025-11-09'

def capitalizacion():
  # inserta tu código aquí
  datos =[17, 21, 44, 50, 79, 86, 140, 178, 203]
 
  # Media
  media = np.mean(data)
 
  # Mediana
  mediana = np.median(data)

  #moda
  moda = 0
  
  # Desviación estándar
  desv_est = np.std(data)
 
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
