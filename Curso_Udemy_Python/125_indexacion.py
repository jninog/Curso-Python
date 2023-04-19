#indexacion de array

import numpy as np

array = np.arange(0,11)
print (array)

array2 =array[2:5]
print(array2)


array2 =array[:]
print(array2)

array_copia = array.copy()
print(array_copia)

array_copia[0:3] = 20
print(array_copia)

array3 = np.array((([1,2,3],[4,5,6],[7,8,9])))
print(array3)

#acceder a una posición
array4 = array3[1][2]
print(array4)
