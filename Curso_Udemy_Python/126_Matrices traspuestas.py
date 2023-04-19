#Arrays  o matrices traspuestas (cambiar ordenadamente las filas por las columnas)

import numpy as np

array = np.arange(15).reshape((3,5))
print(array)

array1 = array[0][1]
print(array1)

aray_trasp = array.T #trasnponer filas por columnas
print(aray_trasp)