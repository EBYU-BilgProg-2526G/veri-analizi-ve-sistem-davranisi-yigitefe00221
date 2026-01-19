import numpy as np
import matplotlib.pyplot as plt

from signal_io import load_signal_csv
from signal_analysis import sampling_rate, basic_stats


def moving_average(x, N):
  
    y = np.zeros(len(x))

    for i in range(len(x)):
        if i < N:
            y[i] = np.mean(x[:i+1])
        else:
            y[i] = np.mean(x[i-N+1:i+1])

    return y


def main():
    t, x = load_signal_csv("signal.csv")

    fs = sampling_rate(t)
    print("Örnekleme frekansı (Hz):", fs)

    stats = basic_stats(x)
    print("Temel istatistikler:")
    for key in stats:
        print(key, ":", stats[key])

    N = 5
    x_filt = moving_average(x, N)

    plt.figure()
    plt.plot(t, x, label="Orijinal Sinyal")
    plt.plot(t, x_filt, label="Hareketli Ortalama")
    plt.xlabel("Zaman (s)")
    plt.ylabel("Genlik")
    plt.legend()
    plt.grid()
    plt.show()


if __name__ == "__main__":
    main()
