import os
import serial

def setAngle(number, angle):
    f = serial.Serial("/dev/ttyUSB0",115200)    #opening the serial port and setting baudrate
    f.write(f"#{number}MD{angle}\r".encode())   #writing to the file
    f.close()
    print(f"#{number}MD{angle}")    #printing the command (relative move in degrees)


setAngle(4, 123)
setAngle(1, 123)

def posInDegrees(number, angle):
    f = serial.Serial("/dev/ttyUSB0",115200)
    f.write(f"#{number}D{angle}\r".encode())
    f.close()
    print(f"#{number}D{angle}")

posInDegrees(4, 1200)
posInDegrees(3, 120)

def wheelModeDegrees(number, angle):    #sets servo to wheel mode where it rotates in that direction
    f = serial.Serial("/dev/ttyUSB0",115200)
    f.write(f"#{number}WD{angle}\r".encode())
    f.close()
    print(f"#{number}WD{angle}")

wheelModeDegrees(2, 10)

#RESET Command
def reset(number):
    f = serial.Serial("/dev/ttyUSB0",115200)    #opening the serial port and setting baudrate
    f.write(f"#{number}RESET\r".encode())   #writing to the file
    f.close()
    print(f"#{number}RESET")    #printing the command (relative move in degrees)

#Limp Command
def limp(number):
    f = serial.Serial("/dev/ttyUSB0",115200)
    f.write(f"#{number}L\r".encode())
    f.close()
    print(f"#{number}L")

