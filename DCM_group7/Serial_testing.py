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
# + struct.pack("B", 0)
i = 0
while 1:
    time.sleep(0.00001)
    x = ser.read(16)
    # x = ser.read(88)
    ser.write(Start)

    if i != 0:
        atr_sig = struct.unpack("d", x[0:8])[0]
        vent_sig = struct.unpack("d", x[8:16])[0]
        a = 1
        print(f"atr_signal: {atr_sig}")
        print(f"vent_sig: {vent_sig}")

    # value3 = struct.unpack("b", x[0:8])[0]
    i = 1
    # print(x)

ser.close()