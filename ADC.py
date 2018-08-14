#######################################
#
# Smart Water System
#
# File Name      :  sensor_reading.py
#
# Author         :  Omkar Pathak
# Contact email  :  opathak@uci.edu
# Faculty Mentor :
#
# Description    : Adafruit MCP3008 analog to 
#                  digital converter code
#
# Created on     : 4/28/2018
#
########################################

import time
import Adafruit_MCP3008
import RPi.GPIO as GPIO

# Software SPI configuration:
CLK  = 18
MISO = 23
MOSI = 24
CS   = 25
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

#List that stores all the names of sensors.
sensor_lst = ["C1(0)", "C2(1)", "C3(2)", "R1(3)"]
#sensor_lst = ["c1(0)"]

#Counter for writing
counter = 0
MAXCOUNT = 10

def open_file (file_path:str) -> 'File':
    #try:
    #print (file_path)
    file = open(file_path, "a")
    #except:
       # print ("Error opening file  :  ", file_path)
       # return None
    return file

def close_file (file):
    file.close()

def write_line (file, text:str):
    file.write (text + '\n')
    file.flush()

def write_header (file):
    write_line (file, "#######################################")
    write_line (file, "#" )
    write_line (file, "# Smart Water System")
    write_line (file, "#")
    write_line (file, "# File Name      :  sensor_reading.txt")
    write_line (file, "#" )
    write_line (file, "# Author         :  Omkar Pathak" )
    write_line (file, "#" )
    write_line (file, "# Contact email  :  opathak@uci.edu" )
    write_line (file, "#" )
    write_line (file, "# Faculty Mentor :  " )
    write_line (file, "#" )
    write_line (file, "# Description    : " )
    write_line (file, "#" )
    write_line (file, "# Created on     :  4/28/2018 " )
    write_line (file, "#" )
    write_line (file, "# Abbrevations   :  R1- Resistive 1" )
    write_line (file, "#" )
    write_line (file, "#######################################")

def write_time (file):
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    write_line (file, "Reading at " + current_time)

def make_table (file, sensor_lst: list):
    write_line (file, '-' * 9* len(sensor_lst))
    content = ""
    for i in sensor_lst:
        content += "{0:>6}".format (i) + "  |"
    write_line (file, content)

def write_sensor_data (file_txt, file_csv, sensor_lst: list):
    global counter
    counter += 1
    if counter < MAXCOUNT:
        return
    write_line (file_txt, '-' * 9* len(sensor_lst))
    values = []
    for i in range (len(sensor_lst)):
        values.append (mcp.read_adc(i))

    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    values_txt_str = current_time
    values_csv_str = current_time

    for value in values:
        values_txt_str += "{0:>6}".format (value) + "  |"
        values_csv_str +=  "," + str (value)
    write_line (file_txt, values_txt_str)
    write_line (file_csv, values_csv_str)
    print (values_csv_str)
    counter = 0

def button_pressed ():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    input_state = GPIO.input(2)
    return not (input_state)

def write_watered(file, sensor_lst):
    write_line (file, '-'*9*len(sensor_lst))
    write_line (file, "Plant Watered!")
    write_time (file)
    write_line (file, "Quantity  :   ")


if __name__ == "__main__":

    file_path_txt = "./Desktop/Smart-Water-System/data/sensor_reading.txt"
    file_path_csv = "./Desktop/Smart-Water-System/data/sensor_reading.csv"
    
    #file_path_txt = "sensor_reading.txt"
    #file_path_csv = "sensor_reading.csv"
 

    file_txt = open_file(file_path_txt)
    file_csv = open_file(file_path_csv)

    #Only uncomment when writing to a file for the first time
    # write_header (file)
    # close_file (file)

    write_line (file_txt,"")
    write_time (file_txt)
    make_table (file_txt, sensor_lst) 
    close_file (file_txt) 
    close_file (file_csv)

    while True:
        file_txt = open_file (file_path_txt)
        file_csv = open_file (file_path_csv)
        write_sensor_data(file_txt, file_csv, sensor_lst)
        if button_pressed ():
            print("entered")
            write_line (file_txt, "")
            write_watered(file_txt, sensor_lst)
            make_table (file_txt, sensor_lst)
        close_file(file_txt)
        close_file (file_csv)
        time.sleep (.1)
        print("Successful transferred code on Github!!")
