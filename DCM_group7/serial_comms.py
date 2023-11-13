import time
import serial

# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
    port='/dev/ttyUSB1',
    baudrate=9600,
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.SEVENBITS
)

ser.isOpen()

print ("Enter your commands below.\r\nInsert exit to leave the application.")

input=1
while 1 :
    # get keyboard input
    input = input(">> ")
        # Python 3 users
        # input = input(">> ")
    if input == 'exit':
        ser.close()
        exit()