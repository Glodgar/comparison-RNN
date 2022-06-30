# Comparison efficency of SimpleRNN, LSTM and GRU

## Development Environment
* CPU: Intel(R) Core(TM) i5-7600K CPU @ 380GHz 3.79 GHz
* Ram: 16.0 GB 
* Python: 3.9.10
* Keras: 2.10.0
* NumPy: 1.22.1
* SciPy: 1.7.3
* Scikit-learn: 1.0.2
* Pandas: 1.4.0
* Matplotlib: 3.5.1
* TensorFlow: 2.10.0

## Dataset
![Ilustration of data](https://raw.githubusercontent.com/Glodgar/comparison-RNN/master/img/data.png)

## Folders structure
<p align="center">
<!--   ![Folders structure](https://raw.githubusercontent.com/Glodgar/comparison-RNN/master/img/files_tree.png) -->
  <img src="https://raw.githubusercontent.com/Glodgar/comparison-RNN/master/img/files_tree.png" title="Files tree" alt="Files tree">
</p>

```
└── results 
    ├── specifications_1
    │   ├── model_1
    │   │   ├── charts
    │   │   │   ├── AllData.png
    │   │   │   ├── PredictedData.png
    │   │   │   ├── PredictedDataForFirst75Days.png
    │   │   │   ├── ResidualPlot.png
    │   │   │   ├── ScatterPlot.png
    │   │   │   ├── Train&ValidationLoss.png
    │   │   │   └── TrainingCurve.png
    │   │   ├── history
    │   │   │   └── history.csv
    │   │   └── weights
    │   │       └── weights.HDF5
    │   │
    │   ├── model_2
    │   ├── ...
    │   └── ...
    │
    ├── specifications_2
    │   ├── ...
    │   └── ...
    ├── ...
    └── ...
```

## Models
| Optimizers    | SimpleRNN             | LSTM             | GRU              |
| ------------- |:---------------------:|:----------------:| ----------------:|
|               | SimpleRNN(None,32)    | LSTM(None,32)    | GRU(None,32)     |
|               | Dense(None,1)         | Dense(None,1)    | Dense(None,1)    |
| ------------- |:---------------------:|:----------------:| ----------------:|
|               | SimpleRNN(None,10,32) | LSTM(None,10,32) | GRU(None,10,32)  |
|               | SimpleRNN(None,10,32) | LSTM(None,10,32) | GRU(None,10,32)  |
|               | SimpleRNN(None,32)    | LSTM(None,32)    | GRU(None,32)     |
|               | Dense(None,1)         | Dense(None,1)    | Dense(None,1)    |
| ------------- |:---------------------:|:----------------:| ----------------:|
|    RMSprop    | SimpleRNN(None,10,64) | LSTM(None,10,64) | GRU(None,10,64)  |
|               | SimpleRNN(None,10,32) | LSTM(None,10,32) | GRU(None,10,32)  |
|               | SimpleRNN(None,16)    | LSTM(None,16)    | GRU(None,16)     |
|               | Dense(None,1)         | Dense(None,1)    | Dense(None,1)    |
| ------------- |:---------------------:|:----------------:| ----------------:|
|               | SimpleRNN(None,10,64) | LSTM(None,10,64) | GRU(None,10,64)  |
|               | SimpleRNN(None,10,32) | LSTM(None,10,32) | GRU(None,10,32)  |
|               | SimpleRNN(None,16)    | LSTM(None,16)    | GRU(None,16)     |
|               | Dense(None,1)         | Dense(None,1)    | Dense(None,1)    |
| ------------- |:---------------------:|:----------------:| ----------------:|
|               | SimpleRNN(None,32)    | LSTM(None,32)    | GRU(None,32)     |
|               | Dense(None,1)         | Dense(None,1)    | Dense(None,1)    |
| ------------- |:---------------------:|:----------------:| ----------------:|
|               | SimpleRNN(None,10,32) | LSTM(None,10,32) | GRU(None,10,32)  |
|               | SimpleRNN(None,10,32) | LSTM(None,10,32) | GRU(None,10,32)  |
|               | SimpleRNN(None,32)    | LSTM(None,32)    | GRU(None,32)     |
|               | Dense(None,1)         | Dense(None,1)    | Dense(None,1)    |
| ------------- |:---------------------:|:----------------:| ----------------:|
|      SGD      | SimpleRNN(None,10,64) | LSTM(None,10,64) | GRU(None,10,64)  |
|               | SimpleRNN(None,10,32) | LSTM(None,10,32) | GRU(None,10,32)  |
|               | SimpleRNN(None,16)    | LSTM(None,16)    | GRU(None,16)     |
|               | Dense(None,1)         | Dense(None,1)    | Dense(None,1)    |
| ------------- |:---------------------:|:----------------:| ----------------:|
|               | SimpleRNN(None,10,64) | LSTM(None,10,64) | GRU(None,10,64)  |
|               | SimpleRNN(None,10,32) | LSTM(None,10,32) | GRU(None,10,32)  |
|               | SimpleRNN(None,16)    | LSTM(None,16)    | GRU(None,16)     |
|               | Dense(None,1)         | Dense(None,1)    | Dense(None,1)    |
| ------------- |:---------------------:|:----------------:| ----------------:|