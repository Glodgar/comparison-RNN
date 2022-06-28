import os
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from default_config import *

os.environ['CUDA_VISIBLE_DEVICES']='-1' 

step = 144 #skip the measurements (6 measurements per hour * 24 hours)

train_days = 1500
validation_days = 500
test_days = 500

T = True #temperatura w stopniach celsjusza "temperature"
# Tpot = True #temperatura w kelvinach "temperature in klevin"
p = True #cisnienie "pressure"
# Tdew = True #"temperature (dew point)"
# rh = True #"relative humidity"
# VPmax = True #"saturation vapor pressure"
# VPact = True #"vaport pressure"
# VPdef = True #"vaport pressure deficit"
# sh  = True #"specific humidity"
H2OC = True #water vaport concetraton
# rho = True # "airtight"
# wv = True #predkosc wiatru "wind speed"
max_wv = True #max predkosc wiatru "max wind speed"
# wd = True #kierunek wiatru "wind direction in degrees"

sc = MinMaxScaler(feature_range = (0, 1))

#load data
fname = os.path.join('data\\jena_climate_2009_2016.csv')
#or
#fname = os.path.join('https://raw.githubusercontent.com/Glodgar/comparison-RNN/master/data/jena_climate_2009_2016.csv')

data = pd.read_csv(fname)
print(data)

#changing the order of columns for easier data splitting
data = data.loc[:, ["Date Time", "T (degC)", "Tpot (K)", "p (mbar)", "Tdew (degC)", "rh (%)", "VPmax (mbar)", "VPact (mbar)", "VPdef (mbar)", "sh (g/kg)", "H2OC (mmol/mol)", "rho (g/m**3)", "wv (m/s)", "max. wv (m/s)", "wd (deg)"]]
data = data.iloc[:, [dateTime, T, Tpot, p, Tdew, rh, VPmax, VPact, VPdef, sh, H2OC, rho, wv, max_wv, wd]]
print(data)

#normalize data
data = pd.DataFrame(sc.fit_transform(data))

dataset = pd.DataFrame({})
index = 0
while index < len(data):
    dataset = dataset.append(data[index:index+1], ignore_index=True)
    index=index+step
print(dataset)


