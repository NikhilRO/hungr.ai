import RPi.GPIO as GPIO
import PIL
import picamera
import os
from time import sleep
import socket
port = 5000

BTN = 18
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BTN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def socket():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind(("", port))
	print "waiting on port:", port
	while 1:
	    data, addr = s.recvfrom(1024)
	    print data


class Servo():
	def __init__(self, PIN):
		GPIO.setup(PIN, GPIO.OUT)
		self.pwm = GPIO.PWM(PIN, 50)
		self.pwm.start(7.5)

	def setAngle(self, angle):
		set_angle = 0.053*angle + 2.2
		self.pwm.ChangeDutyCycle(set_angle)

	def move(self, angle):
		self.setAngle(0)
		self.setAngle(120)


def move(n):
	if(n == 1):
		servoY.move()
	else if(n == 2):
		servoB.move()
	else if(n == 3):
		servoG.move()
	else:
		servoO.move()


def loop():
	flag = True
	print("program running")
	while True:
		btnState = GPIO.input(BTN)
		if btnState == 0:
			print("button press")
			move(1)


if __name__ == '__main__':		# Program start from here
	try:
		os.system('./raspi.sh')
		servoY = Servo(17)
		servoB = Servo(27)
		servoG = Servo(22)
		servoO = Servo(23)
		loop()
	except KeyboardInterrupt:	# When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		servoY.stop()
		servoB.stop()
		servoG.stop()
		servoO.stop()
		GPIO.cleanup()
