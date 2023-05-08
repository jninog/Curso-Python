#171. Instalaciones de seaborn y matplotlib

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

datos1 = np.random.randn(100)
plt.hist(datos1,color="Red",alpha=0.8) #genera el histograma teniendo en cuenta la libreria plt




datos2 = np.random.rand(80)


#unir dos histogramas en una sola visualización 
plt.hist(datos1,color='green',alpha=0.3,bins=20) #bin es el numero de barras que va a graficar
plt.hist(datos2,color='blue',alpha=0.3,bins=20)
plt.show()