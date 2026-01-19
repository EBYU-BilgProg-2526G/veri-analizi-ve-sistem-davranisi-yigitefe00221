import numpy as np

def sampling_rate(t):

    dt = t[1] - t[0]

    fs = 1 / dt
    return fs


def basic_stats(x):  
    stats = {}
    stats["mean"] = np.mean(x)
    stats["std"] = np.std(x)
    stats["rms"] = np.sqrt(np.mean(x ** 2))
    stats["min"] = np.min(x)
    stats["max"] = np.max(x)

    return stats
