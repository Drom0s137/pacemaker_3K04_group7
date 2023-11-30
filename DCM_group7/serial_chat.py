import time
import struct
import serial

# configure the serial connections (the parameters differ based on the device you are connecting to)
ser = serial.Serial(
    port="COM8",
    baudrate=115200,
    stopbits=serial.STOPBITS_ONE,
    bytesize=8,
    timeout=1
)

ser.isOpen()

print("Enter your commands below.\r\nInsert exit to leave the application.")

# Specify the expected length of the data (double in this case)
data_length = 8
end_pattern = b'\xc0'  # Adjust this based on the actual ending pattern in your data stream

while True:
    # Read data until the end pattern is detected
    buffer = bytearray()
    while True:
        byte = ser.read(1)
        buffer += byte
        if buffer[-len(end_pattern):] == end_pattern:
            # Remove the end pattern
            buffer = buffer[:-len(end_pattern)]
            # Check if the received data is of the expected length
            if len(buffer) == data_length:
                value2 = struct.unpack("d", buffer)[0]
                print(buffer)
                print(value2)
            break
