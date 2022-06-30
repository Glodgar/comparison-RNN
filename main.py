import os
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from config.config import *

from utils.dataSplit import dataSplit

from models.simpleRNN1_32_RMSprop import simpleRNN1_32_RMSprop
from models.lstm1_32_RMSprop import LSTM1_32_RMSprop
from models.gru1_32_RMSprop import GRU1_32_RMSprop

spec_count = sum([dateTime, T, Tpot, p, Tdew, rh, VPmax, VPact, VPdef, sh, H2OC, rho, wv, max_wv, wd])

sc = MinMaxScaler(feature_range = (0, 1))

#load data of in directory
fname = os.path.join('data\\jena_climate_2009_2016.csv')
#or if downloaded from the repository
#fname = os.path.join('https://raw.githubusercontent.com/Glodgar/comparison-RNN/master/data/jena_climate_2009_2016.csv')

data = pd.read_csv(fname)
#print(data)

#changing the order of columns for easier data splitting
data = data.loc[:, ["Date Time", "T (degC)", "Tpot (K)", "p (mbar)", "Tdew (degC)", "rh (%)", "VPmax (mbar)", "VPact (mbar)", "VPdef (mbar)", "sh (g/kg)", "H2OC (mmol/mol)", "rho (g/m**3)", "wv (m/s)", "max. wv (m/s)", "wd (deg)"]]
data = data.iloc[:, [dateTime, T, Tpot, p, Tdew, rh, VPmax, VPact, VPdef, sh, H2OC, rho, wv, max_wv, wd]]
#print(data)

#normalize data
data = pd.DataFrame(sc.fit_transform(data))

dataset = pd.DataFrame({})
index = 0
while index < len(data):
    dataset = dataset.append(data[index:index+1], ignore_index=True)
    index=index+step
#print(dataset)

train_set = dataset[0:train_days].reset_index(drop=True)
validation_set = dataset[train_days:train_days+validation_days].reset_index(drop=True)
test_set = dataset[train_days+validation_days:train_days+validation_days+test_days].reset_index(drop=True)

train_set = train_set.to_numpy()
validation_set = validation_set.to_numpy()
test_set = test_set.to_numpy()

x_train, y_train = dataSplit(train_set, lookback)
x_validation, y_validation = dataSplit(validation_set, lookback)
x_test, y_test = dataSplit(test_set, lookback)

# print(x_train.shape)
# print(x_validation.shape)
# print(x_test.shape)

simpleRNN1_32_RMSprop(x_train, y_train, x_validation, y_validation, x_test, y_test, spec_count, dataset, sc)

LSTM1_32_RMSprop(x_train, y_train, x_validation, y_validation, x_test, y_test, spec_count, dataset, sc)

GRU1_32_RMSprop(x_train, y_train, x_validation, y_validation, x_test, y_test, spec_count, dataset, sc)



print("DONE")


