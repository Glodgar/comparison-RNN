import os
from utils.getSpecifications import getSpecifications
from utils.getModelName import getModelName
from config.config import *

def isDirectoryExist(model):
    #..\
    path = "results"
    if not os.path.exists(path):
        os.mkdir(path)
        print("created directory:", path, "\n")

    path += "\\" 

    if modify_data_EMA:
        path += "EMA_"
    
    #..\results
    path += getSpecifications()
    if not os.path.exists(path):
        os.mkdir(path)
        print("created directory:", path, "\n")

    path += "\\" 

    #..\results\T\
    path += getModelName(model)
    if not os.path.exists(path):
        os.mkdir(path)
        print("created directory:", path, "\n")

    #..\results\T\simplernn_32_....
    return path