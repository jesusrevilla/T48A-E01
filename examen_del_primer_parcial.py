import numpy as np

# Importante: verifica que tu nombre y número de matrícula esten correctos

nombre = "Saúl Eduardo Juárez Villela"
numero_de_matricula = 179263
fecha = '2025-11-09'

def capitalizacion():
  data =[17, 21, 44, 50, 79, 86, 140, 178, 203]
 
  # Media
  mean = np.mean(data)
 
  # Mediana
  median = np.median(data)
 
  # Desviación estándar
  std_dev = np.std(data)
 
  # Tupla
  tupla_datos=(mean, median, std_dev)
 
  return tupla_datos
 
capitalizacion()
