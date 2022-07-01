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
    │   ├── ...
    │   ├── time.csv
    │   └── averageDistance.csv
    │
    ├── specifications_2
    │   ├── ...
    │   └── ...
    ├── ...
    └── ...
```

## Models
| Optimizers | SimpleRNN             | LSTM             | GRU             |
|:----------:|:---------------------:|:----------------:|:---------------:|
|            | SimpleRNN(None,32)    | LSTM(None,32)    | GRU(None,32)    |
|            | Dense(None,1)         | Dense(None,1)    | Dense(None,1)   |
|            |───────────────────────|──────────────────|─────────────────|
|            | SimpleRNN(None,10,32) | LSTM(None,10,32) | GRU(None,10,32) |
|            | SimpleRNN(None,10,32) | LSTM(None,10,32) | GRU(None,10,32) |
|            | SimpleRNN(None,32)    | LSTM(None,32)    | GRU(None,32)    |
|            | Dense(None,1)         | Dense(None,1)    | Dense(None,1)   |
|            |───────────────────────|──────────────────|─────────────────|
| RMSprop    | SimpleRNN(None,10,64) | LSTM(None,10,64) | GRU(None,10,64) |
|            | SimpleRNN(None,10,32) | LSTM(None,10,32) | GRU(None,10,32) |
|            | SimpleRNN(None,16)    | LSTM(None,16)    | GRU(None,16)    |
|            | Dense(None,1)         | Dense(None,1)    | Dense(None,1)   |
|            |───────────────────────|──────────────────|─────────────────|
|            | SimpleRNN(None,10,64) | LSTM(None,10,64) | GRU(None,10,64) |
|            | SimpleRNN(None,10,32) | LSTM(None,10,32) | GRU(None,10,32) |
|            | SimpleRNN(None,16)    | LSTM(None,16)    | GRU(None,16)    |
|            | Dense(None,1)         | Dense(None,1)    | Dense(None,1)   |
|────────────|───────────────────────|──────────────────|─────────────────|
|            | SimpleRNN(None,32)    | LSTM(None,32)    | GRU(None,32)    |
|            | Dense(None,1)         | Dense(None,1)    | Dense(None,1)   |
|            |───────────────────────|──────────────────|─────────────────|
|            | SimpleRNN(None,10,32) | LSTM(None,10,32) | GRU(None,10,32) |
|            | SimpleRNN(None,10,32) | LSTM(None,10,32) | GRU(None,10,32) |
|            | SimpleRNN(None,32)    | LSTM(None,32)    | GRU(None,32)    |
|            | Dense(None,1)         | Dense(None,1)    | Dense(None,1)   |
|            |───────────────────────|──────────────────|─────────────────|
| SGD        | SimpleRNN(None,10,64) | LSTM(None,10,64) | GRU(None,10,64) |
|            | SimpleRNN(None,10,32) | LSTM(None,10,32) | GRU(None,10,32) |
|            | SimpleRNN(None,16)    | LSTM(None,16)    | GRU(None,16)    |
|            | Dense(None,1)         | Dense(None,1)    | Dense(None,1)   |
|            |───────────────────────|──────────────────|─────────────────|
|            | SimpleRNN(None,10,64) | LSTM(None,10,64) | GRU(None,10,64) |
|            | SimpleRNN(None,10,32) | LSTM(None,10,32) | GRU(None,10,32) |
|            | SimpleRNN(None,16)    | LSTM(None,16)    | GRU(None,16)    |
|            | Dense(None,1)         | Dense(None,1)    | Dense(None,1)   |

<!-- ├ ┬ ┼  ┤ -->

## Average distance for T
|          |model                      |averageDistance   |
|:--------:|:-------------------------:|:----------------:|
|32        |simplernn1_32_RMSprop      |2.6451327808128315|
|RMSprop   |lstm1_32_RMSprop           |2.6347318419766586|
|          |gru1_32_RMSprop            |2.6331591564837304|
|──────────|───────────────────────────|──────────────────|
|32        |simplernn1_32_SGD          |2.618292828682733 |
|SGD       |lstm1_32_SGD               |2.8037038837881125|
|          |gru1_32_SGD                |2.62076415815729  |
|──────────|───────────────────────────|──────────────────|
|32_32_32  |simplernn3_32_32_32_RMSprop|2.865973051694582 |
|RMSprop   |lstm3_32_32_32_RMSprop     |2.729212822038299 |
|          |gru3_32_32_32_RMSprop      |2.745191264720594 |
|──────────|───────────────────────────|──────────────────|
|32_32_32  |simplernn3_32_32_32_SGD    |2.6650527978019385|
|SGD       |lstm3_32_32_32_SGD         |3.445523014778766 |
|          |gru3_32_32_32_SGD          |2.9858316431687197|
|──────────|───────────────────────────|──────────────────|
|16_32_64  |simplernn3_16_32_64_RMSprop|2.7898178471202146|
|RMSprop   |lstm3_16_32_64_RMSprop     |2.782277435279318 |
|          |gru3_16_32_64_RMSprop      |2.7250013006201805|
|──────────|───────────────────────────|──────────────────|
|16_32_64  |simplernn3_16_32_64_SGD    |2.75758577485546  |
|RMSprop   |lstm3_16_32_64_SGD         |3.4385166828121463|
|          |gru3_16_32_64_SGD          |3.0341526444499607|
|──────────|───────────────────────────|──────────────────|
|64_32_16  |simplernn3_64_32_16_RMSprop|3.079921303027137 |
|RMSprop   |lstm3_64_32_16_RMSprop     |2.700237106817222 |
|          |gru3_64_32_16_RMSprop      |2.7347319761429514|
|──────────|───────────────────────────|──────────────────|
|64_32_16  |simplernn3_64_32_16_SGD    |2.840829965699388 |
|SGD       |lstm3_64_32_16_SGD         |3.4263785342488977|
|          |gru3_64_32_16_SGD          |2.994584340730189 |