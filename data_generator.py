import time

from lib.weather import Weather
from lib.ADC import ADC

#For debugging
import water_system
import lib.File as File

class DataGenerator:
    def __init__(self, water_system_obj):
        self._water_system_obj = water_system_obj

    def collect_data(self, status, last_watered_time):
        weather_dict = Weather().current()
        current_time = time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime())
        sensor_dict = dict()
        val1 = sensor_dict["moisture_sensor_1"] = ADC.sensor_val("capacitive", 0)
        val2 = sensor_dict["moisture_sensor_2"] = ADC.sensor_val("capacitive", 1)
        val3 = sensor_dict["moisture_sensor_3"] = ADC.sensor_val("capacitive", 2)
        val4 = sensor_dict["moisture_sensor_4"] = ADC.sensor_val("capacitive", 3)
        sensor_dict["resistive_moisture"] = ADC.sensor_val("resistive", 4)
        sensor_dict["average_moisture"] = ADC.average_moisture([val1, val2, val3, val4])
        sensor_dict.update(weather_dict)
        sensor_dict["watered"] = status
        sensor_dict["last_watering_time"] = last_watered_time
        sensor_dict["time"] = current_time
        sensor_dict["hour"] = time.strptime(current_time,"%Y-%m-%dT%H:%M:%S")[3]


        if water_system.DEBUG:
            for field in File.FIELD_NAMES:
                print (field, " : ", sensor_dict[field], end = ", ")
            print ("\n\n")

        return sensor_dict

    def monitor_data(self, lock):
        while True:
            if self._water_system_obj.status == 1:
                delay = 300
            else:
                delay = 600

            if water_system.DEBUG:
                delay = 5

            self._water_system_obj.write_data(lock)
            time.sleep(delay)
