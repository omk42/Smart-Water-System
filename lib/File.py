#!/usr/bin/env python
import csv
from pathlib import Path

FIELD_NAMES = ["time", "hour","moisture_sensor_1", "moisture_sensor_2", "moisture_sensor_3", "moisture_sensor_4", "average_moisture",
               "resistive_moisture",
               "temperature", "humidity", "weather_code", "cloud_percent", "rain", "city",
               "last_watering_time","watered"]

class File:
    def __init__(self, path:str):
        self._file_path_str = path
        self._file_path = Path(path)

    def _open_file(self):
        #try:
        self._file_obj = open(self._file_path_str, 'a', newline = '')
        #except:
        #    print("Error opening file : ", self._file_path)

    def _close_file(self):
        try:
            self._file_obj.close()
        except:
            print("Error closing file : ", self._file_path)

    def write_header(self):
        if self._file_path.suffix == ".csv":
            self._open_file()
            writer = csv.DictWriter(self._file_obj, fieldnames=FIELD_NAMES)
            writer.writeheader()
            self._close_file()

    def write_row(self, content:dict):
        if self._file_path.suffix == ".csv":
            self._open_file()
            writer = csv.DictWriter(self._file_obj, fieldnames=FIELD_NAMES)
            writer.writerow(content)
            self._close_file()
        elif self._file_path.suffix == '.txt':
            pass
        else:
            print ("File not a csv or text")


if __name__ == "__main__":
    test = File('C:\\Users\\admin\\Desktop\\some_sample.csv')
    test.write_header()
    test.write_row({'moisture_sensor_1': '1', 'moisture_sensor_2': '2', "moisture_sensor_3": '3', 'moisture_sensor_4': '4'})
    test.write_row({'moisture_sensor_1': '11', 'moisture_sensor_2': '22', "moisture_sensor_3": '33', 'moisture_sensor_4': '44'})
    test.write_row({'moisture_sensor_1': '111', 'moisture_sensor_2': '222', "moisture_sensor_3": '333', 'moisture_sensor_4': '444'})
    test.write_row({'moisture_sensor_1': '1111', 'moisture_sensor_2': '2222', "moisture_sensor_3": '3333', 'moisture_sensor_4': '4444'})
    test.write_row({'moisture_sensor_1': '11111', 'moisture_sensor_2': '22222', "moisture_sensor_3": '33333', 'moisture_sensor_4': '44444'})
