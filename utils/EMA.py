def EMA(dataset):
    datasetEMA = dataset.ewm(2).mean()
    return datasetEMA