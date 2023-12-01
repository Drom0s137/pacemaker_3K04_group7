import time
import struct
import serial


# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
    port = "COM8",
    baudrate=115200,
    #parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_ONE,
    bytesize= 8,
    timeout = 1

)
# ser.open()
ser.isOpen()

print ("Enter your commands below.\r\nInsert exit to leave the application.")
Start = b'\x16'

i = 0
while 1:
    x = ser.read(16)
    ser.write(Start)

    if i != 0:
        atr_sig = struct.unpack("d", x[0:8])[0]
        vent_sig = struct.unpack("d", x[8:16])[0]
        a = 1
        print(f"atr_signal: {atr_sig}")
        print(f"vent_sig: {vent_sig}")

    i = 1
    # print(x)

ser.close()