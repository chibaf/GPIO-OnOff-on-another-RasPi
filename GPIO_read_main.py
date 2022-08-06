import socket
import time
from GPIO_flag_read_class import GPIO_flag_read  # read flags from socket
import RPi.GPIO as GPIO

host = '192.168.0.11'  # server ip address
port = 9988  #port number

GPIO.setmode(GPIO.BOARD) # GPIO set up
num=(11,12) #GPIO number
for i in range(0,len(num)):
  print(num[i])
  GPIO.setup(num[i],GPIO.OUT)

read_socket=GPIO_flag_read(host,port)  #set up socket
s=read_socket.Socket # socket

conn = read_socket.setupConnection(s)  # establish socket connection
while True:
  pin=read_socket.dataTransfer(conn)  # read flags via socket
  print(pin)
  if pin[1]==0:
    GPIO.output(pin[0], GPIO.LOW)
  else:
    GPIO.output(pin[0], GPIO.HIGH)
