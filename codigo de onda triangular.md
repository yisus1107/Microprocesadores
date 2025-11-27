codigo onda triangular
'''
from machine import Pin, PWM
import utime
# Configurar PWM en GPIO15
pwm = PWM(Pin(15))
pwm.freq(1000) #Frecuencia fija

#Parametros de la onda
steps = 50 #Numero de niveles por subida/bajada
delay = 50 #tiempo entre pasos (ms)
max_duty = 65535 #Maximo valor de duty cicle

#Entrada Analogica
adc = ADC (Pin(26))
#Funcion para convetir duty a float
def duty_to_float (duty)
    return duty / max_duty
def duty_to_voltaje(duty):
    return (duty / max_duty)
           
#Generador de onda triangular discreta
def triangular_wave():
    while True:
        #subida
        for i in range (steps):
            duty = int ((i / steps) * max_duty)
            pwm.duty_u16(duty)
            utime.sleep_ms(delay)
        #Bajada
        for i in range (steps, -1, -1):
            duty = int ((i / steps) * max_duty)
            pwm.duty_u16(duty)
            utime.sleep_ms(delay)
            
#Ejecutar
triangular_wave()
'''