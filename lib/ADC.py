#!/usr/bin/env python
import Adafruit_MCP3008
from statistics import mean
import time

class ADC:
    # Software SPI configuration:
    CLK = 18
    MISO = 23
    MOSI = 24
    CS = 25

    #Moisture value bounds
    LOWER = 400
    UPPER = 900

    def __init__(self):
        pass

    @staticmethod
    def sensor_val(type:str, pin:int):
        assert (pin in [0,1,2,3,4,5,6,7])
        mcp = Adafruit_MCP3008.MCP3008(clk=ADC.CLK, cs=ADC.CS, miso=ADC.MISO, mosi=ADC.MOSI)
        reading = mcp.read_adc(pin)

        #Error checking-
        if type == "capacitive":
            if ADC.LOWER < reading < ADC.UPPER:
                return reading
            return 0
        elif type == "resistive":
            return reading

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
    val4 = ADC.capacitance_sensor_val("", 3)

    print("sensor moisture 1: ", val1)
    print("sensor moisture 2: ", val2)
    print("sensor moisture 3: ", val3)
    print("sensor moisture 4: ", val4)

    print ("Average moisture value: ", ADC.average_moisture([val1, val2, val3]))

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
        avg = ADC.average_moisture([val_1, val_2, val_3, val_4])
        print (val_1, val_2, val_3, val_4, avg, sep = "  ")
        time.sleep(1)
