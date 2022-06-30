import os
from utils.getModelName import getModelName
from utils.getSpecifications import getSpecifications
import pandas as pd

def saveAverageDistance(model, y_predicted_descaled, y_test_descaled):
    sum_value = 0
    averageDistance = 0
    for i in range(y_predicted_descaled.shape[0]):
        value = abs(y_test_descaled[i] - y_predicted_descaled[i])
        sum_value += value[0]
    averageDistance = sum_value/y_predicted_descaled.shape[0]
    print("average:", averageDistance, "\n")
    
    name = getModelName(model)
    distance_df = pd.DataFrame({'model': [name], 'averageDistance': [averageDistance]})

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
    path += "averageDistance_"
    path += getSpecifications()
    path += ".csv"

    if not os.path.isfile(path):
        distance_df.to_csv(path, index=False, header='column_names')
    else:
        distance_df.to_csv(path, mode='a', index=False, header=False)
    print("models average distance saved as:", path, "\n")
