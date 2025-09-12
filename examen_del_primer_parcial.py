
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
  Rango=np.ptp(Aguilas)
 
  # Varianza
  Varianza=np.var(Aguilas)
 
  # Desviación estandar
  DevStd=np.std(Aguilas)
 
  datosAguilas=(Rango, Varianza, DevStd)
 
  return datosAguilas
 
asistencia_dispersion()


