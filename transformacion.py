import cmath
import math

def fft(x):
    N = len(x)
    if N <= 1:
        return x
    even = fft(x[0::2])
    odd = fft(x[1::2])
    T = [cmath.exp(-2j * math.pi * k / N) * odd[k] for k in range(N // 2)]
    return [even[k] + T[k] for k in range(N // 2)] + \
           [even[k] - T[k] for k in range(N // 2)]

def aplicar_fft(senal, fs):
    N = len(senal)
    espectro = fft([complex(val, 0) for val in senal])
    magnitudes = [abs(c) for c in espectro[:N // 2]]
    frecuencias = [fs * k / N for k in range(N // 2)]
    return frecuencias, magnitudes