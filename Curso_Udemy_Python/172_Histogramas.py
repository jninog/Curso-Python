#histrogramas

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

datos1 = np.random.randn(100)
plt.hist(datos1,color="Red",alpha=0.8) #genera el histograma teniendo en cuenta la libreria plt
#plt.show() # imprime el histograma

sns.distplot(datos1)
#plt.show()

#cambiar de color

sns.distplot(datos1,color="Blue")
#plt.show()

#combinar histogramas

datos2 = np.random.rand(80)
plt.hist(datos2,color="yellow",alpha = 0.5)
#plt.show()

#unir dos histogramas en una sola visualización con la libreria plt
plt.hist(datos1,color='green',alpha=0.3,bins=20) #bin es el numero de barras que va a graficar
plt.hist(datos2,color='blue',alpha=0.3,bins=20)
#plt.show()

plt.hist(datos1,color='green',alpha=0.3,bins=20,density=True) #bin es el numero de barras que va a graficar
plt.hist(datos2,color='blue',alpha=0.3,bins=20,density=True)
#plt.show()

#unir dos histogramas en una sola visualización con la libreria sns

datos3 = np.random.randn(1000)
datos4 = np.random.randn(1000)

sns.jointplot(x=datos3,y=datos4,kind="hex") #une las dos variables y las muestra en un solo histograma
plt.show()