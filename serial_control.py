import serial
import time
from tkinter import Tk, Button, mainloop

serialPort = serial.Serial(port="COM3",
                           baudrate=9600,
                           bytesize=8,
                           timeout=2,
                           stopbits=serial.STOPBITS_ONE
                           )

print('initializing...')
time.sleep(2)

def ch1_off():
    print('ch1 off')
    serialPort.write(b'0')
def ch1_on():
    print('ch1 on')
    serialPort.write(b'1')
def ch2_off():
    print('ch2 off')
    serialPort.write(b'2')
def ch2_on():
    print('ch2 on')
    serialPort.write(b'3')
def ch3_off():
    print('ch3 off')
    serialPort.write(b'4')
def ch3_on():
    print('ch3 on')
    serialPort.write(b'5')
def ch4_off():
    print('ch4 off')
    serialPort.write(b'6')
def ch4_on():
    print('ch4 on')
    serialPort.write(b'7')
def ch5_off():
    print('ch5 off')
    serialPort.write(b'8')
def ch5_on():
    print('ch5 on')
    serialPort.write(b'9')
def ch6_off():
    print('ch6 off')
    serialPort.write(b'a')
def ch6_on():
    print('ch6 on')
    serialPort.write(b'b')
def ch7_off():
    print('ch7 off')
    serialPort.write(b'c')
def ch7_on():
    print('ch7 on')
    serialPort.write(b'd')

root = Tk()
Button(root, text='ch1 off', command=ch1_off).pack(pady=10)
Button(root, text='ch1 on', command=ch1_on).pack(pady=10)
Button(root, text='ch2 off', command=ch2_off).pack(pady=10)
Button(root, text='ch2 on', command=ch2_on).pack(pady=10)
Button(root, text='ch3 off', command=ch3_off).pack(pady=10)
Button(root, text='ch3 on', command=ch3_on).pack(pady=10)
Button(root, text='ch4 off', command=ch4_off).pack(pady=10)
Button(root, text='ch4 on', command=ch4_on).pack(pady=10)
Button(root, text='ch5 off', command=ch5_off).pack(pady=10)
Button(root, text='ch5 on', command=ch5_on).pack(pady=10)
Button(root, text='ch6 off', command=ch6_off).pack(pady=10)
Button(root, text='ch6 on', command=ch6_on).pack(pady=10)
Button(root, text='ch7 off', command=ch7_off).pack(pady=10)
Button(root, text='ch7 on', command=ch7_on).pack(pady=10)
mainloop()

serialPort.close()