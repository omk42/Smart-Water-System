#!/usr/bin/env python
import RPi.GPIO as GPIO
import sys
import time

from lib.Led import Led

class Switch:
    def __init__(self, water_system, input_pin:int):
        self._input_pin = input_pin
        self._water_system_obj = water_system

        self._setup()

    def _setup(self):
        GPIO.setup(self._input_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def switch_callback(self, value):
        if self.led_obj.is_on:
            self.led_obj.turn_off()
            self.led_obj.is_on = False
            self._water_system_obj.last_water_end_time = time.time()
            self._water_system_obj.status = 0
        else:
            self.led_obj.turn_on()
            self.led_obj.is_on = True
            self._water_system_obj.status = 1
            self._water_system_obj.last_water_end_time = 0
            self._water_system_obj.write_data(self._water_system_obj.lock)

    def run(self, LED_output_pin:int):
        self.led_obj = Led(LED_output_pin)
        GPIO.add_event_detect(self._input_pin, GPIO.FALLING, callback = self.switch_callback,  bouncetime = 200)

    def is_active(self):
        return self.led_obj.is_on

if __name__ == "__main__":
    try:
        GPIO.cleanup()
        GPIO.setmode(GPIO.BOARD)
        s = Switch(7)
        s.run(11)
        while True:
            print (s.is_active())
    except KeyboardInterrupt:
        GPIO.cleanup()
        sys.exit()
