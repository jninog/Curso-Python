import numpy as np
import pandas as pd

lista_valores = np.random.randint(0, 100, 50) #numero aleatorio 0 a 100 y 50 aleatorio
#print(lista_valores)

lista_valores.resize((5,10)) # reorganizar la matriz a 5X10
dataframe = pd.DataFrame(lista_valores)
print(dataframe)

print(dataframe[dataframe >50])
