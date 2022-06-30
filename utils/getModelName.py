from config.config import *

def getModelName(model):
    tab_layers = []
    for i in range(len(model.layers)):    
        tab_layers.append(model.layers[i].name.translate({ord(c):None for c in "_0123456789"}))

    tab_layers_unique = []
    for i in range(len(model.layers)):
        if not model.layers[i].name.translate({ord(c):None for c in "_0123456789"}) in tab_layers_unique:
            tab_layers_unique.append(model.layers[i].name.translate({ord(c):None for c in "_0123456789"}))

    tab_layers_count = []
    for i in range(len(tab_layers_unique)):
        tab_layers_count.append(tab_layers.count(tab_layers_unique[i]))

    units = ""
    for i in range(tab_layers_count[0]):    
        units += str(model.layers[i].units)
        units += "_"

    # print("layers                 :", tab_layers)
    # print("unique layers          :", tab_layers_unique)
    # print("unique layers count    :", tab_layers_count)
    # print("layers sequences length:", units)
    # print(units)

    name = ""

    if modify_data_EMA:
        name += "EMA_"

    name += str(tab_layers[0])
    name += str(tab_layers_count[0])
    name += "_units_"
    name += str(units)
    name += "Optimizer_"
    name += str(model.optimizer.__class__.__name__)
    name += "_Loss_"
    name += str(model.loss)
    name += "_Epochs_"
    name += str(epochs)
    #name += "_StepsPerEpoch_"
    #name += str(int(steps_per_epoch))
    name += "_BatchSize_"
    name += str(batch_size)
    #name += "_ValSteps_"
    #name += str(int(val_steps))
    return name