import os
import matplotlib.pyplot as plt
from utils.getModelName import getModelName
from utils.isDirectoryExist import isDirectoryExist

from config.config import *

def savePlots(model, plt_title):
    path = isDirectoryExist(model)
    #..\results\spec\
    path += "\\charts\\"
    if not os.path.exists(path):
        os.mkdir(path)
        print("created dictionary:", path, "\n")
    #path += "\\"        
    path += getModelName(model)
    path += "_"        
    path += plt_title.title().replace(" ", "")
    plt.savefig(path, dpi=300)
    print("plot saved as:", path, "\n")