from machine import Pin, I2C
import time
import bme280_float

i2c = I2C(0, scl=Pin(17), sda=Pin(16))
bme = bme280_float.BME280(i2c=i2c)
rele = machine.Pin(18, machine.Pin.OUT)

while True:
    print(bme.values)
    temperatura, presion, humedad = bme.read_compensated_data()
    if (temperatura > 22):
        rele.value(1)
    else:
        rele.value(0)
    time.sleep(2)
