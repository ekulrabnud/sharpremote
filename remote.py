import serial
import time

cmd = dict()

cmd['PORT']="COM5"

cmd['OFF']="POWR0"
cmd['ON']="POWR1"
cmd['UP']="CHUP1"
cmd['DOWN']="CHDW"
cmd['DIGITAL']="DC2U"


class Remote():

	def __init__(self):
		self.ser = serial.Serial(cmd['PORT'])

	def reply(self):
		time.sleep(1)
		print self.ser.read(self.ser.inWaiting())

	def fix_command(self,cmd):
		self.ser.write(cmd + "   \r")
		self.reply

	def var_command(self,cmd):
		length = len(cmd)
		space =" "
		spaces = 8 - length
		self.ser.write(cmd + (space*spaces) + "\r")
		self.reply()

	def on(self):
		self.fix_command(cmd["ON"])
		self.reply()

	def off(self):
		self.fix_command(cmd["OFF"])
		self.reply()

	def digital(self,ch):
		self.var_command(cmd['DIGITAL'] + str(ch))

