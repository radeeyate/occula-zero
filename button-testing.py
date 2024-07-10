from gpiozero import Button, LED
from picamera2 import Picamera2
from datetime import datetime
from signal import pause
import time

button = Button(17, pull_up=False)
green = LED(23)
picam2 = Picamera2()
capture_config = picam2.create_still_configuration()
picam2.start()
green.off()


def blinkLED():
    green.on()
    time.sleep(0.05)
    green.off()
    time.sleep(0.05)

def startBlink():
    while button.is_pressed:
        blinkLED()

def focus():
    picam2.autofocus_cycle()

def capture():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    green.on()
    focus()
    picam2.switch_mode_and_capture_file(capture_config, f"pic_{timestamp}.jpg")
    green.off()
    time.sleep(0.1)
    for _ in range(2):
        blinkLED()
    print("took pic")
    time.sleep(0.5)

#button.when_pressed = startBlink
#button.when_pressed = focus
button.when_pressed = lambda:[startBlink(), focus()]
button.when_released = capture

pause()
