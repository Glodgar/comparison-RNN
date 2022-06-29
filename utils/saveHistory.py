import os
import pandas as pd
from utils.getModelName import getModelName
from utils.isDirectoryExist import isDirectoryExist

from config.config import *

def saveHistory(model, history):
    path = isDirectoryExist(model)
    #..\results\spec\
    path += "\\history\\"
    if not os.path.exists(path):
        os.mkdir(path)
        print('created dictionary:', path, "\n")
        
    path += getModelName(model)
    path += ".csv"
    hist_df = pd.DataFrame(history.history)
    with open(path, mode='w') as f:
        hist_df.to_csv(f)
    print("history saved as:", path, "\n")