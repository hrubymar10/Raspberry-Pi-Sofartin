import lcddriver
import socket
import os
import time
import commands

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

from time import *
lcd = lcddriver.lcd()
pihostname = socket.gethostname()
temp_sensor_in = '/sys/bus/w1/devices/28-000006090383/w1_slave'
temp_sensor_out = '/sys/bus/w1/devices/28-0000060a9e9d/w1_slave'
piip = commands.getoutput("/sbin/ifconfig").split("\n")[1].split()[1][5:]

def temp_raw_in():
    f = open(temp_sensor_in, 'r')
    lines_in = f.readlines()
    f.close()
    return lines_in

def temp_raw_out():
    f = open(temp_sensor_out, 'r')
    lines_out = f.readlines()
    f.close()
    return lines_out

def read_temp_in():
    lines_in = temp_raw_in()
    while lines_in[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines_in = temp_raw_in()
    temp_output_in = lines_in[1].find('t=')
    if temp_output_in != -1:
        temp_string_in = lines_in[1].strip()[temp_output_in+2:]
        temp_c_in = float(temp_string_in) / 1000.0
        return temp_c_in

def read_temp_out():
    lines_out = temp_raw_out()
    while lines_out[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines_out = temp_raw_out()
    temp_output_out = lines_out[1].find('t=')
    if temp_output_out != -1:
        temp_string_out = lines_out[1].strip()[temp_output_out+2:]
        temp_c_dd_out = float(temp_string_out) / 1000.0
        temp_c_out = temp_c_dd_out
        return temp_c_out

lcd.lcd_clear()
lcd.lcd_display_string("16X2 I2C Display", 1)
lcd.lcd_display_string("   Starting...", 2)
sleep(5)
while True:
	lcd.lcd_clear()
	lcd.lcd_display_string("System name:", 1)
	lcd.lcd_display_string(pihostname, 2)
	sleep(5)
	lcd.lcd_clear()
	lcd.lcd_display_string("System Address:", 1)
	lcd.lcd_display_string(piip, 2)
	sleep(5)
	temp_in = str(read_temp_in()) + 'C'
	lcd.lcd_clear()
	lcd.lcd_display_string("Temperature IN:", 1)
	lcd.lcd_display_string(temp_in, 2)
	sleep(5)
	temp_out = str(read_temp_out()) + 'C'
	lcd.lcd_clear()
	lcd.lcd_display_string("Temperature OUT:", 1)
	lcd.lcd_display_string(temp_out, 2)
	sleep(5)