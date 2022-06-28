import matplotlib.pyplot as plt

def drawPlots(dataset, history, y_test_descaled, y_predicted_descaled):   
    loss = history.history['loss']
    val_loss = history.history['val_loss']
    epochs_plot = range(len(loss))

    #train & validation loss
    plt.figure()
    plt.plot(epochs_plot, loss, 'r', label='train loss')
    plt.plot(epochs_plot, val_loss, 'b', label='val loss')
    plt.legend(loc="upper left")
    plt.title("train & validation loss")
    
    
    #All data
    plt.figure()
    plt.plot(dataset[0], color = 'black', linewidth=1, label = 'True value')
    plt.ylabel("T (degC)")
    plt.xlabel("Day")
    plt.title("All data")


    #Predicted data
    plt.figure()
    plt.plot(y_test_descaled, color = 'black', linewidth=1, label = 'True value')
    plt.plot(y_predicted_descaled, color = 'red',  linewidth=1, label = 'Predicted')
    plt.legend(frameon=False)
    plt.ylabel("Temperature")
    plt.xlabel("Day")
    plt.title("Predicted data")

    
    #Predicted data for 75 days
    plt.figure()
    plt.plot(y_test_descaled[0:75], 'b', linewidth=1, label = 'True value')
    plt.plot(y_predicted_descaled[0:75], '--r', label = 'Predicted')
    plt.legend(frameon=False)
    plt.ylabel("Temperature")
    plt.xlabel("Day")
    plt.title("Predicted data for first 75 days")

    
    #Training curve
    plt.figure()
    plt.plot(epochs_plot, loss, color='black')
    plt.ylabel("Loss (MSE)")
    plt.xlabel("Epoch")
    plt.title("Training curve")

    
    #Residual plot
    plt.figure()
    plt.plot(y_test_descaled-y_predicted_descaled, color='black')
    plt.ylabel("Residual")
    plt.xlabel("Day")
    plt.title("Residual plot")

    
    #Scatter plot
    plt.figure()
    plt.scatter(y_predicted_descaled, y_test_descaled, s=2, color='black')
    plt.ylabel("Y true")
    plt.xlabel("Y predicted")
    plt.title("Scatter plot")

        
    #plt.subplots_adjust(hspace = 0.5, wspace=0.3)

    #plt.show()
    
    