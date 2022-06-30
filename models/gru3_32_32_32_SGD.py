from keras.models import Sequential
from keras.layers import GRU
from keras.layers import Dense
from keras.optimizers import SGD
import time
from sklearn.preprocessing import MinMaxScaler
import numpy as np

from config.config import *

from utils.drawPlots import drawPlots
from utils.saveHistory import saveHistory
from utils.saveWeights import saveWeights
from utils.saveTime import saveTime
from utils.saveAverageDistance import saveAverageDistance

def gru3_32_32_32_SGD(x_train, y_train, x_validation, y_validation, x_test, y_test, spec_count, dataset, sc):
    model = Sequential()

    model.add(GRU(32, input_shape=(x_train.shape[1], spec_count)))
    model.add(GRU(32, input_shape=(x_train.shape[1], spec_count)))
    model.add(GRU(32, input_shape=(x_train.shape[1], spec_count)))
    model.add(Dense(1))

    model.compile(optimizer=SGD(), loss='mae')
    
    model.summary()

    start_time = time.time()

    history = model.fit(x_train, y_train, 
                        epochs=epochs,
                        verbose=verbose,
                        batch_size = batch_size,
                        validation_data=(x_validation, y_validation))
    
    end_time = round(time.time() - start_time, 2)

    print("time: ", end_time)
    
    saveHistory(model, history)
    saveWeights(model)
    saveTime(model, end_time)
    
    y_predicted = model.predict(x_test)
    
    if spec_count>1:
        help_array = np.zeros((y_predicted.shape[0], spec_count))
        help_array[:,:-1] = y_predicted
        y_predicted_descaled = sc.inverse_transform(help_array)
        y_predicted_descaled = y_predicted_descaled[:,:1]

        help_array = np.zeros((y_train.shape[0], spec_count))
        help_array[:,:-1] = y_train
        y_train_descaled = sc.inverse_transform(help_array)
        y_train_descaled = y_train_descaled[:,:1]
    
        help_array = np.zeros((y_test.shape[0], spec_count))
        help_array[:,:-1] = y_test

        y_test_descaled = sc.inverse_transform(help_array)
        y_test_descaled = y_test_descaled[:,:1]
    else:
        y_predicted_descaled = sc.inverse_transform(y_predicted)
        y_train_descaled = sc.inverse_transform(y_train)
        y_test_descaled = sc.inverse_transform(y_test)

    saveAverageDistance(model, y_predicted_descaled, y_test_descaled)
    drawPlots(dataset, history, y_test_descaled, y_predicted_descaled, model)