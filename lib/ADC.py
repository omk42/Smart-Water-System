#!/usr/bin/env python
import Adafruit_MCP3008
from statistics import mean

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
    def capacitance_sensor_val(pin):
        assert (pin in [1,2,3,4])
        mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)
        reading = mcp.read_adc(pin)

        #Error checking-
        if ADC.LOWER < reading < ADC.UPPER:
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

    print (ADC.average_moisture([1,2,3,4,5]))
    print (ADC.average_moisture([]))

    val1 = ADC.capacitance_sensor_val(1)
    val2 = ADC.capacitance_sensor_val(2)
    val3 = ADC.capacitance_sensor_val(3)
    val4 = ADC.capacitance_sensor_val(4)

    print("sensor moisture 1: ", val1)
    print("sensor moisture 2: ", val2)
    print("sensor moisture 3: ", val3)
    print("sensor moisture 4: ", val4)

    print ("Average moisture value: ", ADC.average_moisture([val1, val2, val3]))

    try:
        print (ADC.capacitance_sensor_val(5))
    except AssertionError:
        pass
