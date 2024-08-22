import time
from machine import Pin

LED = 25
TMUX = 28
BUTTON = 22
led = None
tmux = None
button = None
button_last_state = None
is_init = False

def init():
    global led, tmux, button, is_init, button_last_state
    if is_init:
        return
    is_init = True
    print("init")
    led = Pin(LED, Pin.OUT)
    tmux = Pin(TMUX, Pin.OUT)
    button = Pin(BUTTON, Pin.IN, Pin.PULL_UP)

def run():
    global button_last_state
    init()
    while True:
        button_state = button.value()
        if button_last_state is None or button_state != button_last_state:
            button_last_state = button_state
            led.value(int(not button_state))
            tmux.value(int(not button_state))
