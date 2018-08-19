import RPIO
import time
from Led import Led


class Switch:
    def __init__(self, input_pin:int):
        self._input_pin = input_pin
        self._setup()

    def _setup(self):
        RPIO.setup(self._input_pin, RPIO.IN, pull_up_down=RPIO.PUD_UP)

    def switch_callback(self, gpio_id, value):
        if self.led_obj.is_on:
            self.led_obj.turn_off()
            self.led_obj.is_on = False
        else:
            self.led_obj.turn_off()

    def run(self, LED_output_pin:int):
        #Led_blink = True
        self.led_obj = Led(LED_output_pin)
        RPIO.add_interrupt_callback(self._input_pin, callback = self.switch_callback, edge = 'falling',  threaded_callback = True)
        RPIO.wait_for_interrupts()

        # while True:
        #     button_state = RPIO.input(self._input_pin)
        #     if not button_state:
        #         if Led_blink:
        #             led_obj.start_blink()
        #         else:
        #             led_obj.stop_blink()
        #         Led_blink = not Led_blink


if __name__ == "__main__":
    #RPIO.setmode(RPIO.BOARD)
    Switch(4).run(17)
    RPIO.cleanup()
