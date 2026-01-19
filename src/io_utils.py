
import csv
import numpy as np

def load_signal_csv(path):
    CSV formatı:
    t,x
    0.0, 1.23
    0.01, 1.10
    
    t = []
    x = []

    with open(path, "r") as file:
        reader = csv.reader(file)
        next(reader)  # başlık satırını atla (t,x)

        for row in reader:
            t.append(float(row[0]))
            x.append(float(row[1]))

    t = np.array(t)
    x = np.array(x)

    return t, x
