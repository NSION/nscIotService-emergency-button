#! /usr/bin/env python
import RPi.GPIO as GPIO
import time
import requests

BtnPin1 = 4    # pin4 --- button1

def setup():
    GPIO.setmode(GPIO.BCM)       # GPIO Layoyt BCM
    GPIO.setup(BtnPin1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)    # Set BtnPin's mode is input, and pull down to low level(0V)
    GPIO.setwarnings(False)

def switch(ev=None):
    print('Broadcasting on\r')
    requests.post('http://localhost:8091/nscIotService/media/live/start')
        
def loop():
    GPIO.add_event_detect(BtnPin1, GPIO.RISING, callback=switch, bouncetime=250)    
    if GPIO.add_event_detect(BtnPin1, GPIO.FALLING): 
        print('Broadcasting off\r')
        requests.post('http://localhost:8091/nscIotService/media/live/end')    
    while True:
        pass   

def destroy():
        GPIO.cleanup() 

if __name__ == '__main__':     # Program start from here
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()
