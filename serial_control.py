import serial
import time

serialPort = serial.Serial(port="COM3",
                           baudrate=9600,
                           bytesize=8,
                           timeout=2,
                           stopbits=serial.STOPBITS_ONE
                           )

print('initializing...')
time.sleep(3)

for i in range(5):
    print('on', i + 1)
    serialPort.write(b'1')
    time.sleep(2)

    print('off', i + 1)
    serialPort.write(b'0')
    time.sleep(2)

serialPort.close()