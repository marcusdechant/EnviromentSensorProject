#RadioProject
#Remote Sensor Data Logger

#verbose
script='main.py'
v='v1.2.0'
author='Marcus Dechant (c) 2023'
verbose=('\n'+script+' - ('+v+') - '+author+'\n')
print(verbose)

#Sensors [Position 1 & 2]
from sht1 import t1
from sht1 import h1
from sht2 import t2
from sht2 import h2

#import list
import lib.RFM.adafruit_rfm9x as RFM
import digitalio as DIO
import board as bo
import busio as bu
import time as ti
import microcontroller as mc

#local variables
#Constructors
sl=ti.sleep
dio=DIO.DigitalInOut
rfm=RFM.RFM9x

#SPI Object
spi=bu.SPI(bo.GP10, MOSI=bo.GP11, MISO=bo.GP12)
cs=dio(bo.GP13)
rst=dio(bo.GP15)

#RF Frequency (MHz)
rf=915.0

#High Power Level (max=19dB, min=5dB, +19dB cause board crashes)
#For 2 Sensors max=16dB
pwr=16
spf=11

#Radio Object
radio=rfm(spi, cs, rst, rf, high_power=True)

#Board Led
led=dio(bo.LED)
led.direction=DIO.Direction.OUTPUT
led.value=True #On when Pico is powered and running

#common variables
lid=0
delay=10
ledel=0.5

#Delimiter
c=','

#functions
def mct(): #board temp function
    bt=('{0:0.2f}'.format(mc.cpu.temperature))
    return(bt)

while(True): #Main Loop
    lid+=1 #Loop Local Variables
    temp_a=float(t1())
    humi_a=float(h1())
    temp_b=float(t2())
    humi_b=float(h2())
    bt=float(mct())
    
    #If Sen1 is returning None.
    #TO-DO: Copy for Sen2
    if(temp_a is None)or(humi_a is None):
        nid=1
        #attempt 30 times
        while(nid==30):
            nid+=1
            temp_a=t1()
            humi_a=h1()
            if(temp_a is not None)and(humi_a is not None):
                break
        while(True): #After 30 tries led will blink indicating an error
            led.value=False
            sl(ledel)
            led.value=True
            sl(ledel)
    
    else: #Sensor Returns a Value
        data=(str(lid)+c+str(delay)+c+"Good"+c+str(temp_a)+c+str(humi_a)+c+str(temp_b)+c+str(humi_b)+c+str(bt))
    
    data=data+c+str(pwr)
    radio.tx_power=pwr
    #Send Data to RXRadio
    radio.send(data)
    #print data to user
    print(data)
    #can be in function
    #Led Indicates Data is Sent
    led.value=False
    sl(ledel)
    led.value=True
    #reading delay
    sl(delay)
#led off before exit
led.value=False
exit(0)