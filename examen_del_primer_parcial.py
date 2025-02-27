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

  # Calcular el coeficiente de correlación de Pearson
  r = sum_product_deviations / ((len(x) - 1) * std_x * std_y)

  return r
