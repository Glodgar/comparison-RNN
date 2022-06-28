from keras.models import Sequential
from keras.layers import SimpleRNN
from keras.layers import Dense
from keras.optimizers import RMSprop
import time

def simpleRNN_32_RMSprop(x_train, y_train, x_validation, y_validation, x_test, y_test, spec_count, batch_size, epochs, verbose):
    model = Sequential()
    model.add(SimpleRNN(32, input_shape=(x_train.shape[1], spec_count)))
    model.add(Dense(1))
    model.compile(optimizer=RMSprop(), loss='mae')
    model.summary()

    start_time = time.time()

    history = model.fit(x_train, y_train, 
                        epochs=epochs,
                        verbose=verbose,
                        batch_size = batch_size,
                        validation_data=(x_validation, y_validation))
    
    end_time = round(time.time() - start_time, 2)
    
    print("time: ", end_time)

    y_predicted = model.predict(x_test)