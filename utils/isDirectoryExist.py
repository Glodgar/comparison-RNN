import os
from getSpecifications import getSpecifications

def isResultsExist():
    path = "results"
    if not os.path.exists(path):
        os.mkdir(path)
        print("created dictionary:", path, "\n")

    path += "\\" 
    
    path += getSpecifications()
    if not os.path.exists(path):
        os.mkdir(path)
        print("created dictionary:", path, "\n")

    return path