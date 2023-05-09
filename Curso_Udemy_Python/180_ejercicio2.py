import numpy as np
import pandas as pd
import matplotlib.pyplot as mlp
import seaborn as sns 


lista_valores = np.random.randint(0,500,100) # array de 100 numeros aleatorios entre el rango 0 a 500
print(lista_valores)

sns.boxplot(lista_valores)
mlp.show()