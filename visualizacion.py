import matplotlib.pyplot as plt

def graficar_senal_y_fft(senal, frecuencias, magnitudes):
    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.plot(senal)
    plt.title("Señal original")
    plt.xlabel("Muestra")
    plt.ylabel("Valor ADC")

    plt.subplot(1, 2, 2)
    plt.plot(frecuencias, magnitudes)
    plt.title("Espectro de Frecuencia (FFT)")
    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("Magnitud")

    plt.tight_layout()
    plt.show()