import serial

def leer_datos_serial(puerto='COM3', baudrate=115200, num_muestras=1024, timeout=1):
    datos = []
    with serial.Serial(puerto, baudrate, timeout=timeout) as ser:
        print("Leyendo datos...")
        while len(datos) < num_muestras:
            try:
                linea = ser.readline().decode('utf-8').strip()
                if linea.isdigit():
                    datos.append(int(linea))
            except:
                continue
    return datos