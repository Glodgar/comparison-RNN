import os
from utils.getModelName import getModelName
from utils.getSpecifications import getSpecifications
import pandas as pd

def saveTime(model, end_time):
    name = getModelName(model)
    time_df = pd.DataFrame({'model': [name], 'time': [end_time]})

    #..\
    path = "results"
    if not os.path.exists(path):
        os.mkdir(path)
        print("created directory:", path, "\n")
    #..\results

    path += "\\" 
    
    #..\results\\
    path += getSpecifications()
    if not os.path.exists(path):
        os.mkdir(path)
        print("created directory:", path, "\n")
    #..\results\\T_p_H2OC_maxWv

    path += "\\"
    path += "time_"
    path += getSpecifications()
    path += ".csv"

    if not os.path.isfile(path):
        time_df.to_csv(path, index=False, header='column_names')
    else:
        time_df.to_csv(path, mode='a', index=False, header=False)
    print("models time saved as:", path, "\n")
