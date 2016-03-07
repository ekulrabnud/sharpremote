import serial
import time

ser = serial.Serial('COM5')

def command(input):
	length = len(input)
	cr ="\r"
	space =" "
	spaces = 8 - length
	return input + (space * spaces) + cr

def run():
	while True:
		input = command(raw_input("Command?...."))
		ser.write(input)
		time.sleep(1)
		reply = ser.inWaiting()
		if reply:
			print ser.read(reply)
		else:
			print "No Reply"
		
		

if __name__ == "__main__":
	run()
