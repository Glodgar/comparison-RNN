import matplotlib.pyplot as plt
import numpy as np
from utils.savePlots import savePlots

from config.config import *

def drawPlots(dataset, history, y_test_descaled, y_predicted_descaled, model):   
    loss = history.history['loss']
    val_loss = history.history['val_loss']
    epochs_plot = range(len(loss))

    #train & validation loss
    plt.figure()
    plt.plot(epochs_plot, loss, 'r', label='train loss')
    plt.plot(epochs_plot, val_loss, 'b', label='val loss')
    plt.legend(loc="upper left")
    plt_title = "train & validation loss"
    plt.title(plt_title)
    savePlots(model, plt_title)
    
    
    #All data
    plt.figure()
    plt.plot(dataset[0], color = 'black', linewidth=1, label = 'True value')
    plt.ylabel("T (degC)")
    plt.xlabel("Day")
    plt_title = "All data"
    plt.title(plt_title)
    savePlots(model, plt_title)


    #Predicted data
    plt.figure(plt_title)
    plt.plot(y_test_descaled, color = 'black', linewidth=1, label = 'True value')
    plt.plot(y_predicted_descaled, color = 'red',  linewidth=1, label = 'Predicted')
    plt.legend(frameon=False)
    plt.ylabel("Temperature")
    plt.xlabel("Day")
    plt_title = "Predicted data"
    plt.title(plt_title)
    savePlots(model, plt_title)

    
    #Predicted data for 75 days
    plt.figure()
    plt.plot(y_test_descaled[0:75], 'b', linewidth=1, label = 'True value')
    plt.plot(y_predicted_descaled[0:75], '--r', label = 'Predicted')
    plt.legend(frameon=False)
    plt.ylabel("Temperature")
    plt.xlabel("Day")
    plt_title = "Predicted data for first 75 days"
    plt.title(plt_title)
    savePlots(model, plt_title)

    
    #Training curve
    plt.figure()
    plt.plot(epochs_plot, loss, color='black')
    plt.ylabel("Loss (MSE)")
    plt.xlabel("Epoch")
    plt_title = "Training curve"
    plt.title(plt_title)
    savePlots(model, plt_title)

    
    #Residual plot
    plt.figure()
    plt.plot(y_test_descaled-y_predicted_descaled, color='black')
    plt.ylabel("Residual")
    plt.xlabel("Day")
    plt_title = "Residual plot"
    plt.title(plt_title)
    savePlots(model, plt_title)

    
    #Scatter plot
    plt.figure()
    plt.scatter(y_predicted_descaled, y_test_descaled, s=2, color='black')
    plt.ylabel("Y true")
    plt.xlabel("Y predicted")
    plt_title = "Scatter plot" 
    plt.title(plt_title)
    savePlots(model, plt_title)    


    predicted_range = np.arange(len(y_predicted_descaled[0:75]))
    difference = abs((y_test_descaled[0:75] - y_predicted_descaled[0:75]) / y_test_descaled[0:75] * 100)
    tab_difference = []
    for i in range(len(y_predicted_descaled[0:75])):
        tab_difference.append(difference[i][0])
    plt.figure()
    plt.bar(predicted_range, tab_difference)
    plt.ylabel("%")
    plt.xlabel("Days")
    plt_title = "Prediction mistake" 
    plt.title(plt_title)
    savePlots(model, plt_title)
    

        
    #plt.subplots_adjust(hspace = 0.5, wspace=0.3)

    #plt.show()
    
    