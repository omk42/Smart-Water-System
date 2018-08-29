import RPi.GPIO as GPIO
import threading
import time

from data_generator import DataGenerator
from lib.switch import Switch
from lib.File import File


class Water_System:

    # Pins
    push_button = 7
    led = 11
    path = "./data/sensor_reading.csv"

    def __init__(self):
        self.lock = threading.Lock()
        self.data_generator = DataGenerator(self)
        self.status = 0
        self.last_water_end_time = 0

    def pi_setup(self):
        GPIO.setmode(GPIO.BOARD)

    def pi_cleanup(self):
        GPIO.cleanup()

    def write_data(self,lock):
        last_watered_time = time.time() - self.last_water_end_time
        with lock:
            File(Water_System.path).write_row(self.data_generator.collect_data(self.status, last_watered_time))

    def run(self):
        self.pi_setup()
        switch_obj = Switch(self, Water_System.push_button)
        switch_obj.run(Water_System.led)

        thread1 = threading.Thread(target=self.data_generator.monitor_data, name="thread1",
                                   args=(self.lock,), daemon=True)
        thread1.start()
        try:
            while True:
                pass
        except KeyboardInterrupt:
            return
