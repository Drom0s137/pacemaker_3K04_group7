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

# Option A Below code works
"""
Start = b'\x16'
set = b'\x55'
on = b'\x01'
off = b'\x00'
off_time = b'\x00\x00\x00\x01'   # big endian
switch_time = b'\x50\x11'        # big endian
send1 = Start + set + on + on + on + off_time + switch_time
send2 = Start + set + off + off + off + off_time + switch_time
ser.write(send1)
"""

# Option B Below code also works
"""
Start = struct.pack("b", 22)
set = struct.pack('b', 85)
on = struct.pack('b', 1)
off = struct.pack('b', 0)
off_time = struct.pack("f", 0.1)
switch_time = struct.pack('H', 4)

send1 = Start + set + on + off + off + off_time + switch_time
# send2 = Start + set + off + off + off + off_time + switch_time
print(send1)
ser.write(send1)
"""

ser.close()