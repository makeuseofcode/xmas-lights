import random
from machine import Pin, ADC
from time import sleep
# import RPi.GPIO from GPIO

#map each relay to the Pico GPIO Pin 
relay1 = Pin(6, Pin.OUT) #GP6
relay2 = Pin(5, Pin.OUT) #GP5
relay3 = Pin(14, Pin.OUT) #GP14

#add the relay modules to a list
lights_list = [relay1, relay2, relay3]


#try:
#set a count to loop through x times
for i in range(200):
    # randomly pick a relay from the assigned list
    lights = random.choice(lights_list)
    # output for diagnosis 
    print(lights)
    # turn light on (relay at open)
    lights.value(1)
    # pause / sleep
    sleep(0.5)
    # turn light off (relay at closed state)
    lights.value(0)
#finally:
    #GPIO.cleanup()