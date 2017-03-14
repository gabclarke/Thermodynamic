import serial
import threading

ser = serial.Serial('/dev/cu.usbmodem1411', 9600)
print(ser.readline())

def hello_world():
  threading.Timer(5.0, hello_world).start() # called every minute
  ser.write(b"abc")

hello_world()

# while True:
#     ser.write(b'5')
