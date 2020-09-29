import serial
serialport = serial.Serial("/dev/ttyUSB0", 9600, timeout=20)
from firebase import firebase
FBConn=firebase.FirebaseApplication("https://sensor-readings-142b2.firebaseio.com/")


while True:
    command = serialport.readline()
    command=command[3:5]
    FBConn.put('https://sensor-readings-142b2.firebaseio.com',"Ph",command)
    print("pH "+command)
  