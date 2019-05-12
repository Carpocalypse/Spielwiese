#!/usr/bin/python
import time
import RPi.GPIO as GPIO

# VOM DAB Belegt:
# 7,8,9,10,11,18,19,20,21,23,25
# GPIO Pins festlegen (anpassen)
LED_RED = 16
LED_GREEN = 22
LED_YELLOW = 27
TASTER = 18
NPN = 26
Luefter_on = 0
def get_cpu_temp():
        tempFile = open("/sys/class/thermal/thermal_zone0/temp")
        cpu_temp = tempFile.read()
        tempFile.close()
        return float(cpu_temp)/1000

if __name__ == '__main__':
	# Init
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(LED_RED,GPIO.OUT)
	GPIO.setup(LED_GREEN,GPIO.OUT)
	GPIO.setup(LED_YELLOW,GPIO.OUT)
	GPIO.setup(NPN,GPIO.OUT)
	GPIO.setup(TASTER,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
while 1:
	if get_cpu_temp() >= 60:
		GPIO.output(LED_RED,GPIO.HIGH)
		GPIO.output(LED_GREEN, GPIO.LOW)
		GPIO.output(LED_YELLOW, GPIO.LOW)
		GPIO.output(NPN, GPIO.HIGH)
		Luefter_on = 1
#		time.sleep(120)
	elif get_cpu_temp() >= 45 and get_cpu_temp() < 60:
		if get_cpu_temp() >= 50:
			GPIO.output(LED_YELLOW, GPIO.HIGH)
			GPIO.output(LED_GREEN, GPIO.LOW)
		else:
			GPIO.output(LED_YELLOW, GPIO.LOW)
			GPIO.output(LED_GREEN, GPIO.HIGH)
		GPIO.output(LED_RED, GPIO.LOW)
		if Luefter_on == 1:
			GPIO.output(NPN, GPIO.HIGH)
		elif Luefter_on ==0:
			GPIO.output(NPN, GPIO.LOW)
	elif get_cpu_temp() <= 45.000:
		GPIO.output(LED_GREEN, GPIO.HIGH)
		GPIO.output(LED_YELLOW, GPIO.LOW)
		GPIO.output(LED_RED, GPIO.LOW)
		GPIO.output(NPN, GPIO.LOW)
		Luefter_on = 0
	else :
		print "keines von alle dem"
		GPIO.output(LED_GREEN, GPIO.HIGH)
		GPIO.output(LED_YELLOW, GPIO.HIGH)
		GPIO.output(LED_RED, GPIO.HIGH)
		GPIO.output(NPN, GPIO.HIGH)
	print get_cpu_temp()
	if GPIO.input(TASTER) == GPIO.HIGH:
		Luefter_on = 1
	time.sleep(1)
