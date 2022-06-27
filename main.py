import os
import pandas as pd

os.environ['CUDA_VISIBLE_DEVICES']='-1' 

fname = os.path.join('data\\jena_climate_2009_2016.csv')

data = pd.read_csv(fname)
print(data)