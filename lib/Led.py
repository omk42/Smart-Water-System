import RPIO

class Led:
    def __init__ (self, output_pin:int):
        self._output_pin = output_pin
        self.is_on = False
        self._setup()

    def _setup(self):
        RPIO.setup(self._output_pin, RPIO.OUT, initial = RPIO.LOW)

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
        RPIO.output(self._output_pin, True)

    def turn_off(self):
        RPIO.output(self._output_pin, False)


if __name__ == "__main__":
    Led_obj = Led(17)
    print ("Hello world")