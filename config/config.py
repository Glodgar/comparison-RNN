import os
from config.default_config import *

os.environ['CUDA_VISIBLE_DEVICES']='-1' 

step = 144 #skip the measurements (6 measurements per hour * 24 hours)
lookback = 10 #number of days which the prediction is based
epochs = 500
batch_size = 100

train_days = 1500
validation_days = 500
test_days = 500

verbose = 1

# modify_data_EMA = True

T = True #temperature
# Tpot = True #temperature in klevin
# p = True #pressure
# Tdew = True #temperature (dew point)
# rh = True #relative humidity
# VPmax = True #saturation vapor pressure
# VPact = True #vaport pressure
# VPdef = True #vaport pressure deficit
# sh  = True #specific humidity
# H2OC = True #water vaport concetraton
# rho = True #airtight
# wv = True #wind speed
# max_wv = True #max wind speed
# wd = True #wind direction in degrees