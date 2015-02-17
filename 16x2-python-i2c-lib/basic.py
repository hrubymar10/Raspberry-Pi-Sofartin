import lcddriver
import socket
from time import *
lcd = lcddriver.lcd()
pihostname = socket.gethostname()
def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('google.com', 0))
    ipaddr=s.getsockname()[0]
    return ipaddr

lcd.lcd_clear()
lcd.lcd_display_string("16X2 I2C Display", 1)
lcd.lcd_display_string("  Just works!!!", 2)
sleep(3)
lcd.lcd_clear()
lcd.lcd_display_string("System name:", 1)
lcd.lcd_display_string(pihostname, 2)
sleep(3)
lcd.lcd_clear()
lcd.lcd_display_string("System Address:", 1)
lcd.lcd_display_string(get_ip_address(), 2)
sleep(3)
