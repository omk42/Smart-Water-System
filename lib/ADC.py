#!/usr/bin/env python
import Adafruit_MCP3008
from Adafruit_GPIO import RPiGPIOAdapter
import RPi.GPIO

from statistics import mean
import time

class ADC:
    # Software SPI configuration:
    CLK = 12
    MISO = 16
    MOSI = 18
    CS = 22
    GPIO = RPiGPIOAdapter(RPi.GPIO, RPi.GPIO.BOARD)

    #Moisture value bounds
    CAPACITIVE_LOWER = 400
    CAPACITIVE_UPPER = 900
    RESISTIVE_LOWER = 400
    RESISTIVE_UPPER = 1024

    def __init__(self):
        pass

    @staticmethod
    def sensor_val(type:str, pin:int):
        assert (pin in [0,1,2,3,4,5,6,7])
        mcp = Adafruit_MCP3008.MCP3008(clk=ADC.CLK, cs=ADC.CS, miso=ADC.MISO, mosi=ADC.MOSI, gpio=ADC.GPIO)
        reading = mcp.read_adc(pin)

        #Error checking-
        if type == "capacitive":
            if ADC.CAPACITIVE_LOWER < reading < ADC.CAPACITIVE_UPPER:
                return reading
            return 0
        elif type == "resistive":
            if ADC.RESISTIVE_LOWER < reading < ADC.RESISTIVE_UPPER:
                return reading
            return 0

    @staticmethod
    def average_moisture(values:list):
        filtered_lst = [value for value in values if value != 0]
        if len(filtered_lst) != 0:
            return mean (filtered_lst)
        else:
            return 0

if __name__ == "__main__":

    print ("Initial testing")

    print (ADC.average_moisture([1,2,3,4,5]))
    print (ADC.average_moisture([]))

    val1 = ADC.sensor_val("capacitive", 0)
    val2 = ADC.sensor_val("capacitive", 1)
    val3 = ADC.sensor_val("capacitive", 2)
    val4 = ADC.sensor_val("capacitive", 3)
    val5 = ADC.sensor_val("resistive", 4)

    print("sensor moisture 1: ", val1)
    print("sensor moisture 2: ", val2)
    print("sensor moisture 3: ", val3)
    print("sensor moisture 4: ", val4)
    print("sensor moisture 4: ", val5)

    print ("Average moisture value: ", ADC.average_moisture([val1, val2, val3, val4]))

    try:
        print (ADC.sensor_val("capacitive",99))
    except AssertionError:
        print ("correct")
        pass

    print ("\n\n\nLoop testing\n")
    while True:
        val_1 = ADC.sensor_val ("capacitive", 0)
        val_2 = ADC.sensor_val ("capacitive", 1)
        val_3 = ADC.sensor_val ("capacitive", 2)
        val_4 = ADC.sensor_val ("capacitive", 3)
        val_5 = ADC.sensor_val("resistive", 4)

        avg = ADC.average_moisture([val_1, val_2, val_3, val_4])
        print (val_1, val_2, val_3, val_4, val_5, avg, sep = "  ")
        time.sleep(1)
