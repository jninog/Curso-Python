#160. Reemplazar datos en Series

import pandas as pd
import numpy as np

serie = pd.Series([1,2,3,4,5],index=list('abcde'))
print(serie)
serieR= serie.replace(1,6) # remplaza un solo valor
print(serieR)
serieR= serie.replace({2:8,3:9}) # remplaza varios valores en las series 
print(serieR)
