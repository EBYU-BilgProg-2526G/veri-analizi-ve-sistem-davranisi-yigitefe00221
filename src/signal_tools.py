import numpy as np

def moving_average(x, window_size):

    y = []

    for i in range(len(x)):
        if i < window_size:
            ortalama = np.mean(x[:i+1])
        else:
            ortalama = np.mean(x[i-window_size+1:i+1])

        y.append(ortalama)

    return np.array(y)
