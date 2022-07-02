import os
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
from config.config import *

from utils.dataSplit import dataSplit
from utils.EMA import EMA

# 32 RMSprop
from models.simpleRNN1_32_RMSprop import simpleRNN1_32_RMSprop
from models.lstm1_32_RMSprop import lstm1_32_RMSprop
from models.gru1_32_RMSprop import gru1_32_RMSprop
# 32 SGD
from models.simpleRNN1_32_SGD import simpleRNN1_32_SGD
from models.lstm1_32_SGD import lstm1_32_SGD
from models.gru1_32_SGD import gru1_32_SGD

# 32 32 32 RMSprop
from models.simpleRNN3_32_32_32_RMSprop import simpleRNN3_32_32_32_RMSprop
from models.lstm3_32_32_32_RMSprop import lstm3_32_32_32_RMSprop
from models.gru3_32_32_32_RMSprop import gru3_32_32_32_RMSprop
# 32 32 32SGD
from models.simpleRNN3_32_32_32_SGD import simpleRNN3_32_32_32_SGD
from models.lstm3_32_32_32_SGD import lstm3_32_32_32_SGD
from models.gru3_32_32_32_SGD import gru3_32_32_32_SGD

# 16 32 64 RMSprop
from models.simpleRNN3_16_32_64_RMSprop import simpleRNN3_16_32_64_RMSprop
from models.lstm3_16_32_64_RMSprop import lstm3_16_32_64_RMSprop
from models.gru3_16_32_64_RMSprop import gru3_16_32_64_RMSprop
# 16 32 64SGD
from models.simpleRNN3_16_32_64_SGD import simpleRNN3_16_32_64_SGD
from models.lstm3_16_32_64_SGD import lstm3_16_32_64_SGD
from models.gru3_16_32_64_SGD import gru3_16_32_64_SGD

# 64 32 16 RMSprop
from models.simpleRNN3_64_32_16_RMSprop import simpleRNN3_64_32_16_RMSprop
from models.lstm3_64_32_16_RMSprop import lstm3_64_32_16_RMSprop
from models.gru3_64_32_16_RMSprop import gru3_64_32_16_RMSprop
# 64 32 16 SGD
from models.simpleRNN3_64_32_16_SGD import simpleRNN3_64_32_16_SGD
from models.lstm3_64_32_16_SGD import lstm3_64_32_16_SGD
from models.gru3_64_32_16_SGD import gru3_64_32_16_SGD

spec_count = sum([dateTime, T, Tpot, p, Tdew, rh, VPmax, VPact, VPdef, sh, H2OC, rho, wv, max_wv, wd])

sc = MinMaxScaler(feature_range = (0, 1))

#load data of in directory
fname = os.path.join('data\\jena_climate_2009_2016.csv')
#or if downloaded from the repository
#fname = os.path.join('https://raw.githubusercontent.com/Glodgar/comparison-RNN/master/data/jena_climate_2009_2016.csv')

data = pd.read_csv(fname)

#changing the order of columns for easier data splitting
data = data.loc[:, ["Date Time", "T (degC)", "Tpot (K)", "p (mbar)", "Tdew (degC)", "rh (%)", "VPmax (mbar)", "VPact (mbar)", "VPdef (mbar)", "sh (g/kg)", "H2OC (mmol/mol)", "rho (g/m**3)", "wv (m/s)", "max. wv (m/s)", "wd (deg)"]]
data = data.iloc[:, [dateTime, T, Tpot, p, Tdew, rh, VPmax, VPact, VPdef, sh, H2OC, rho, wv, max_wv, wd]]

#normalize data
#data = pd.DataFrame(sc.fit_transform(data))

dataset = pd.DataFrame({})
index = 0
while index < len(data):
    dataset = dataset.append(data[index:index+1], ignore_index=True)
    index=index+step

dataset = pd.DataFrame(sc.fit_transform(dataset))

#---------------------------------------------------------------------
if modify_data_EMA:
    datasetEMA = EMA(dataset)
    print(dataset[0])
    plt.figure()
    plt.plot(dataset[0:75][0], color = 'b', linewidth=1, label = 'dataset')
    plt.plot(datasetEMA[0:75][0], color = 'r', label = 'datasetEMA')
    plt.legend(frameon=False)
    plt.ylabel("Normalized temperature")
    plt.xlabel("Days")
    plt_title = "oryginal temperature vs EMA temperature"
    plt.title(plt_title)
    plt.show()
#---------------------------------------------------------------------

# train_set = dataset[0:train_days].reset_index(drop=True)
# validation_set = dataset[train_days:train_days+validation_days].reset_index(drop=True)
# test_set = dataset[train_days+validation_days:train_days+validation_days+test_days].reset_index(drop=True)

# train_set = train_set.to_numpy()
# validation_set = validation_set.to_numpy()
# test_set = test_set.to_numpy()

# x_train, y_train = dataSplit(train_set, lookback)
# x_validation, y_validation = dataSplit(validation_set, lookback)
# x_test, y_test = dataSplit(test_set, lookback)

# # 32 RMSprop
# simpleRNN1_32_RMSprop(x_train, y_train, x_validation, y_validation, x_test, y_test, spec_count, dataset, sc)
# lstm1_32_RMSprop(x_train, y_train, x_validation, y_validation, x_test, y_test, spec_count, dataset, sc)
# gru1_32_RMSprop(x_train, y_train, x_validation, y_validation, x_test, y_test, spec_count, dataset, sc)
# # 32 SGD
# simpleRNN1_32_SGD(x_train, y_train, x_validation, y_validation, x_test, y_test, spec_count, dataset, sc)
# lstm1_32_SGD(x_train, y_train, x_validation, y_validation, x_test, y_test, spec_count, dataset, sc)
# gru1_32_SGD(x_train, y_train, x_validation, y_validation, x_test, y_test, spec_count, dataset, sc)

# # 32 32 32 RMSprop
# simpleRNN3_32_32_32_RMSprop(x_train, y_train, x_validation, y_validation, x_test, y_test, spec_count, dataset, sc)
# lstm3_32_32_32_RMSprop(x_train, y_train, x_validation, y_validation, x_test, y_test, spec_count, dataset, sc)
# gru3_32_32_32_RMSprop(x_train, y_train, x_validation, y_validation, x_test, y_test, spec_count, dataset, sc)
# # 32 32 32SGD
# simpleRNN3_32_32_32_SGD(x_train, y_train, x_validation, y_validation, x_test, y_test, spec_count, dataset, sc)
# lstm3_32_32_32_SGD(x_train, y_train, x_validation, y_validation, x_test, y_test, spec_count, dataset, sc)
# gru3_32_32_32_SGD(x_train, y_train, x_validation, y_validation, x_test, y_test, spec_count, dataset, sc)

# # 16 32 64 RMSprop
# simpleRNN3_16_32_64_RMSprop(x_train, y_train, x_validation, y_validation, x_test, y_test, spec_count, dataset, sc)
# lstm3_16_32_64_RMSprop(x_train, y_train, x_validation, y_validation, x_test, y_test, spec_count, dataset, sc)
# gru3_16_32_64_RMSprop(x_train, y_train, x_validation, y_validation, x_test, y_test, spec_count, dataset, sc)
# # 16 32 64SGD
# simpleRNN3_16_32_64_SGD(x_train, y_train, x_validation, y_validation, x_test, y_test, spec_count, dataset, sc)
# lstm3_16_32_64_SGD(x_train, y_train, x_validation, y_validation, x_test, y_test, spec_count, dataset, sc)
# gru3_16_32_64_SGD(x_train, y_train, x_validation, y_validation, x_test, y_test, spec_count, dataset, sc)

# # 64 32 16 RMSprop
# simpleRNN3_64_32_16_RMSprop(x_train, y_train, x_validation, y_validation, x_test, y_test, spec_count, dataset, sc)
# lstm3_64_32_16_RMSprop(x_train, y_train, x_validation, y_validation, x_test, y_test, spec_count, dataset, sc)
# gru3_64_32_16_RMSprop(x_train, y_train, x_validation, y_validation, x_test, y_test, spec_count, dataset, sc)
# # 64 32 16 SGD
# simpleRNN3_64_32_16_SGD(x_train, y_train, x_validation, y_validation, x_test, y_test, spec_count, dataset, sc)
# lstm3_64_32_16_SGD(x_train, y_train, x_validation, y_validation, x_test, y_test, spec_count, dataset, sc)
# gru3_64_32_16_SGD(x_train, y_train, x_validation, y_validation, x_test, y_test, spec_count, dataset, sc)