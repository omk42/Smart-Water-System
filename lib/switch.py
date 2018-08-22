#!/usr/bin/env python
import RPi.GPIO as GPIO
from Led import Led
import sys

class Switch:
    def __init__(self, input_pin:int):
        self._input_pin = input_pin
        self._setup()

    def _setup(self):
        GPIO.setup(self._input_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def switch_callback(self, value):
        if self.led_obj.is_on:
            self.led_obj.turn_off()
            self.led_obj.is_on = False
        else:
            self.led_obj.turn_on()
            self.led_obj.is_on = True

    def run(self, LED_output_pin:int):
        self.led_obj = Led(LED_output_pin)
        GPIO.add_event_detect(self._input_pin, GPIO.FALLING, callback = self.switch_callback,  bouncetime = 200)
        while True:
            pass

if __name__ == "__main__":
    try:
        GPIO.cleanup()
        GPIO.setmode(GPIO.BOARD)
        Switch(7).run(11)
    except KeyboardInterrupt:
        GPIO.cleanup()
        sys.exit()
