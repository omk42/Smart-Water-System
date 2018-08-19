#!/usr/bin/env python
import RPi.GPIO as GPIO
import sys

class Led:
    def __init__(self, output_pin:int):
        self._output_pin = output_pin
        self.is_on = False
        self._setup()

    def _setup(self):
        GPIO.setup(self._output_pin, GPIO.OUT, initial= GPIO.LOW)

    def start_blink(self):
        counter = 0
        while True:
            self.turn_on()
            counter += 1
            if counter == 100:
                self.turn_off()
                counter = 0

    def stop_blink(self):
        self.turn_off()

    def turn_on(self):
        GPIO.output(self._output_pin, GPIO.HIGH)

    def turn_off(self):
        GPIO.output(self._output_pin, GPIO.LOW)


if __name__ == "__main__":
    try:
        Led_obj = Led(11)
        Led_obj.turn_on()
        GPIO.cleanup()
    except KeyboardInterrupt:
        sys.exit()