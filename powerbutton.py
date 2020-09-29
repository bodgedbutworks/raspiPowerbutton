#!/usr/bin/python3

# Start using non-sudo "crontab -e":
#	"@reboot python3 /home/pi/powerbutton/powerbutton.py"

# Uses lowermost two pins (near Ethernet port) on RasPi 3B header
# 	Bottom left = Pin 39 = GND
#	Bottom Right = Pin 40 = GPIO29

import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def shutdown(someArgument):
	os.system("wall \"Power button pressed, shutting down now.\"")
	os.system("sudo poweroff")

GPIO.add_event_detect(21, GPIO.FALLING, callback=shutdown, bouncetime=2000)	# bouncetime is in ms

print("Powerbutton python script active!")

while(True):
	time.sleep(1)
