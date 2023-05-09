#diagramas de caja
#sirve para representar graficamente una serie de datos numericos a traves sus cuarties

import numpy as np
import pandas as pd
import matplotlib.pyplot as mpl
import seaborn as sns

datos = np.random.randn(1000)

sns.boxplot(datos)
mpl.show()

