from numpy import array

def dataSplit(sequence, lookback):
    x = []
    y = []
    for i in range(len(sequence)):
        end_ix = i + lookback
        if end_ix > len(sequence)-1:
            break
        seq_x, seq_y = sequence[i:end_ix], sequence[end_ix, 0:1]
        x.append(seq_x)
        y.append(seq_y)
    return array(x), array(y)