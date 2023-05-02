
import pandas as pd
import numpy as np

minimo = 10
maximo = 40
numero = 3

alunmos = np.random.randint(minimo,maximo,numero)
print(alunmos)

clases = ['clase1','clase2','clase3']

serie = pd.Series(alunmos,index=clases)
print(serie)
print(serie['clase2'])

