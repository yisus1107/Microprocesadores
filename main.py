from adquisicion import leer_datos_serial
from transformacion import aplicar_fft
from visualizacion import graficar_senal_y_fft

PUERTO = 'COM4'
BAUDRATE = 115200
NUM_MUESTRAS = 1024
FS = 1000  # Frecuencia de muestreo

senal = leer_datos_serial(PUERTO, BAUDRATE, NUM_MUESTRAS)
frecuencias, magnitudes = aplicar_fft(senal, FS)
graficar_senal_y_fft(senal, frecuencias, magnitudes)