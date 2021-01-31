#! /usr/bin/env python3
import RPi.GPIO as GPIO
import time
import requests

BtnPin1 = 23    # pin23 --- button1

def setup():
    GPIO.setmode(GPIO.BCM)       # GPIO Layoyt BCM
    GPIO.setup(BtnPin1, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Set BtnPin's mode is input, and pull up to high level(3.3V)
    GPIO.setwarnings(False)

def switchon(ev=None):
    if GPIO.input(BtnPin1):     # if port BtnPin1 == 1  
        print('Broadcasting off\r')
        requests.post('http://localhost:8091/nscIotService/media/live/end')  
    else: 
        print('Broadcasting on\r')
        requests.post('http://localhost:8091/nscIotService/media/live/start')

def loop():
    GPIO.add_event_detect(BtnPin1, GPIO.FALLING, callback=switchon, bouncetime=300)
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
