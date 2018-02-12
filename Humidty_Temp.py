#!/usr/bin/python
# Example using a character LCD connected to a Raspberry Pi
import datetime
import Adafruit_CharLCD as LCD
import sys
import Adafruit_DHT
from astral import Astral


# Raspberry Pi pin setup
lcd_rs = 25
lcd_en = 24
lcd_d4 = 23
lcd_d5 = 17
lcd_d6 = 18
lcd_d7 = 22
lcd_backlight = 0

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows = 4

lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)

lcd.message('Getting\nReadings')
# Wait 5 seconds
i=0

city_name = 'Buffalo'
a = Astral()
a.solar_depression = 'civil'
city = a[city_name]
try:
    while True:
    #for x in range(2):
    humidity, temperature = Adafruit_DHT.read_retry(11, 2)
    t=(temperature * 9/5) + 32
    lcd.clear()
    i+=1
    sun = city.sun(date=datetime.datetime.today(), local=True)
    lcd.set_cursor(0, 0)
    lcd.message("Temp: "+str(t)+"F")
    lcd.set_cursor(0, 1)
    lcd.message("Humidity: "+str(humidity))
    lcd.set_cursor(-4, 2)
    lcd.message("Sunrise: "+str(sun['sunrise'].hour)+":"+str(sun['sunrise'].minute))
    lcd.set_cursor(-4, 3)
    lcd.message("Sunset   "+str(sun['sunset'].hour)+":"+str(sun['sunset'].minute))

finally:                   # this block will run no matter how the try block exits
    GPIO.cleanup()         # clean up after yourself
