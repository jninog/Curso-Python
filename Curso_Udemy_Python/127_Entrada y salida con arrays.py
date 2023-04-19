# 127_Entrada y salida con arrays

import numpy as np

array1 = np.arange(6)
#print(array1)

np.save('array1s',array1) # salvar el array

recuperado = np.load('array1s.npy') #recuperar array 
#print(recuperado)

array1 = np.arange(6)
array2 = np.arange(8)

np.savez('arrays1', x=array1,y=array2)

array_recuperado = np.load('arrays1.npz')
print(array_recuperado['x'])
print(array_recuperado['y'])

#guardar en un fichero de texto

np.savetxt('Mificherodetexto.txt',array2,delimiter=',')
print(np.loadtxt('Mificherodetexto.txt',delimiter=','))