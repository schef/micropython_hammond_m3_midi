import time
from machine import Pin

LED = 25
led = None

def init():
    global led
    print("init")
    led = Pin(LED, Pin.OUT)

def run():
    pass
