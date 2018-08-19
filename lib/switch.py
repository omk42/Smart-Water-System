#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
from Led import Led
import sys


class Switch:
    def __init__(self, input_pin:int):
        self._input_pin = input_pin
        self._setup()

    def _setup(self):
        GPIO.setup(self._input_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def switch_callback(self, gpio_id, value):
        if self.led_obj.is_on:
            self.led_obj.turn_off()
            self.led_obj.is_on = False
        else:
            self.led_obj.turn_on()
            self.led_obj.is_on = True

    def run(self, LED_output_pin:int):
        #Led_blink = True
        self.led_obj = Led(LED_output_pin)
        GPIO.add_event_detect(self._input_pin, GPIO.FALLING, callback = self.switch_callback,  bouncetime = 200)

        # while True:
        #     button_state = RPIO.input(self._input_pin)
        #     if not button_state:
        #         if Led_blink:
        #             led_obj.start_blink()
        #         else:
        #             led_obj.stop_blink()
        #         Led_blink = not Led_blink


if __name__ == "__main__":
    try:
        GPIO.setmode(GPIO.BOARD)
        Switch(7).run(11)
        GPIO.cleanup()
    except KeyboardInterrupt:
        sys.exit()