#sht2.py
#Temperature and Humidity Sensor Position 2

import lib.SHT31D.adafruit_sht31d as SHT
import busio as BU
import board as BO

ICC=BU.I2C(scl=BO.GP17, sda=BO.GP16, frequency=200000)
sht30=SHT.SHT31D(ICC)

def t2():
    TEMP=sht30.temperature
    temp=('{0:0.2f}'.format(TEMP))
    return(temp)

def h2():
    HUMI=sht30.relative_humidity
    humi=('{0:0.2f}'.format(HUMI))
    return(humi)

#testing
#print(t2())
#print(h2())

#(c) Marcus Dechant 2023