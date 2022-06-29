import os
from utils.getModelName import getModelName
from utils.isDirectoryExist import isDirectoryExist

from config.config import *

def saveWeights(model):
    path = isDirectoryExist(model)
    #..\results\spec\
    path += "\\weights\\"
    if not os.path.exists(path):
        os.mkdir(path)
        print("created dictionary:", path, "\n")
    path += getModelName(model)
    path += ".HDF5"
    model.save_weights(path)
    print("weights saved as:", path, "\n")