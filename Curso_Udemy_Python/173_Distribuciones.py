#combinando estilos

import pandas as pd
import numpy as np
import matplotlib.pyplot as mpl
import seaborn as sns

datos =np.random.randn(1000)
#print(datos)

sns.distplot(datos,color="blue")
mpl.show()

#se quita el grafico de barras y dejar la curva
sns.distplot(datos,color="blue", rug=False,hist=False)
mpl.show()

#configurar un color la curva y otro las barras

argumentos_curva = {'color':'black','label':'Curva'}
argumentos_histograma = {'color':'grey','label':'Histograma'}
sns.distplot(datos,bins=25,kde_kws=argumentos_curva,hist_kws=argumentos_histograma)
mpl.legend()
mpl.show()

######se crea una serie y se representa en un histrograma

serie = pd.Series(datos)
#print(serie)

sns.displot(serie,bins=25,color='Blue')
mpl.show()