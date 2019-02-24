#! /usr/bin/python

import RPi.GPIO as GPIO
import can
import time
import os
import queue
from threading import Thread



print('\n\rCAN Rx test')
print('Bring up CAN0....')

# Bring up can0 interface at 500kbps
os.system("sudo /sbin/ip link set can0 up type can bitrate 500000")
time.sleep(0.1)	
print("Ready")

# test connection
try:
	bus = can.interface.Bus(channel='can0', bustype='socketcan_native')
except OSError:
	print("Cannot find PiCAN board.")
	
	exit()
	
	

	
def upShift (bus):

	msg = can.Message(arbitration_id=0x148,data=[0x09],extended_id=False)
	bus.send(msg)
	time.sleep(0.1)
	
	msg.data[0] = 0x05
	bus.send(msg)
	time.sleep(0.01)
	return 
	
	
	
def downShift (bus):

	msg = can.Message(arbitration_id=0x148,data=[0x0A],extended_id=False)
	bus.send(msg)
	time.sleep(0.1)
	
	msg.data[0] = 0x05
	bus.send(msg)
	time.sleep(0.01)
	return 
	
	
try:

	#sample of upshift and downshift every 2s
	upShift (bus)
	time.sleep(2)
	
	downShift (bus)
	time.sleep(2)
		
	
except KeyboardInterrupt:
	#Catch keyboard interrupt
	 
	os.system("sudo /sbin/ip link set can0 down")
	print("\n\rKeyboard interrtupt")