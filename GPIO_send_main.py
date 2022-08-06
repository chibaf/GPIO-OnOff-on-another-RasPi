import socket
from time import sleep
from GPIO_flag_send_class import GPIO_flag_send  # send flags to RasPi via socket

host = '192.168.0.11'   # server ip address
port = 9988  #poert number

gpio_flag=GPIO_flag_send(host,port)  # establish socket connection
s = gpio_flag.Socket  # socket

num=(11,12)  # GPIO pin number
i=0;j=0
while True:   # sending flags via socket
  sleep(1)
  i=i+1;j=j+1
  k=i % 2;l=j % 2
  gpio_flag.flag_send(s,(num[k],l))  # send flags to RasPi via socket
