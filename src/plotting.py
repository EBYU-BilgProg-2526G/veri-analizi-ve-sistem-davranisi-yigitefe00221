import matplotlib.pyplot as plt

def plot_time(t, x_raw, x_filt, save_path):
    
    plt.figure()
    plt.plot(t, x_raw, label="Ham Sinyal")
    plt.plot(t, x_filt, label="Filtrelenmiş Sinyal")

    plt.xlabel("Zaman (s)")
    plt.ylabel("Genlik")
    plt.title("Zaman Domeninde Sinyal")
    plt.legend()
    plt.grid()

    plt.savefig(save_path)
    plt.show()
