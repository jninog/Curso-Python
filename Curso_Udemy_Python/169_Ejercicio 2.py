import numpy as np
import pandas as pd

array1 = np.random.randint(1,100,9)
array2 = np.random.randint(1,100,9)
#print(array1)
#print(array2)

array1.resize(3,3)
array2.resize(3,3)
print(array1)
print(array2)

dataframe1= pd.DataFrame(array1)
dataframe2= pd.DataFrame(array2)

dataframe_concat = pd.concat([dataframe1,dataframe2],ignore_index=True)
print(dataframe_concat)
