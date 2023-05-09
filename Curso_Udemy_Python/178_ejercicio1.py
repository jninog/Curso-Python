import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as mpl

#1)
lista = np.random.randn(1000) #randn es distribución normal
#print(lista)
#2()
mpl.hist(lista,color='Blue',alpha=0.8)
mpl.show()

#3)
sns.boxplot(lista)
mpl.show()

