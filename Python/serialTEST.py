import serial
import threading
from random import randint

s = serial.Serial('/dev/cu.usbmodem1411', 9600)
print(s.readline())

def hello_world():
  threading.Timer(5.0, hello_world).start() # called every minute
  onoff = randint(0,1)
  data = str(onoff)
  # data = bytes(data)
  print(data)
  # ser.write(b"{}".format(str(onoff)))
  s.write(data.encode())

hello_world()

# while True:
#     ser.write(b'5')
