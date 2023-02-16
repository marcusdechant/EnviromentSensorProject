#sht1.py
#Temperature and Humidity Sensor Position 1

import lib.SHT31D.adafruit_sht31d as SHT
import busio as BU
import board as BO

ICC=BU.I2C(scl=BO.GP19, sda=BO.GP18, frequency=200000)
sht30=SHT.SHT31D(ICC)

def t1():
    TEMP=sht30.temperature
    temp=('{0:0.2f}'.format(TEMP))
    return(temp)

def h1():
    HUMI=sht30.relative_humidity
    humi=('{0:0.2f}'.format(HUMI))
    return(humi)

#testing
#print(t1())
#print(h1())

#(c) Marcus Dechant 2023