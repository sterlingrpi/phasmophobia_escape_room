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

def ch1_on():
    print('ch1 on')
    serialPort.write(b'0')
def ch1_off():
    print('ch1 off')
    serialPort.write(b'1')
def ch2_on():
    print('ch2 on')
    serialPort.write(b'2')
def ch2_off():
    print('ch2 off')
    serialPort.write(b'3')
def ch3_on():
    print('ch3 on')
    serialPort.write(b'4')
def ch3_off():
    print('ch3 off')
    serialPort.write(b'5')
def ch4_on():
    print('ch4 on')
    serialPort.write(b'6')
def ch4_off():
    print('ch4 off')
    serialPort.write(b'7')
def ch5_on():
    print('ch5 on')
    serialPort.write(b'8')
def ch5_off():
    print('ch5 off')
    serialPort.write(b'9')
def ch6_on():
    print('ch6 on')
    serialPort.write(b'a')
def ch6_off():
    print('ch6 off')
    serialPort.write(b'b')
def ch7_on():
    print('ch7 on')
    serialPort.write(b'c')
def ch7_off():
    print('ch7 off')
    serialPort.write(b'd')
def ch8_on():
    print('ch8 on')
    serialPort.write(b'e')
def ch8_off():
    print('ch8 off')
    serialPort.write(b'f')
def ch9_on():
    print('ch9 on')
    serialPort.write(b'g')
def ch9_off():
    print('ch9 off')
    serialPort.write(b'h')
def ch10_on():
    print('ch10 on')
    serialPort.write(b'i')
def ch10_off():
    print('ch10 off')
    serialPort.write(b'j')

root = Tk()
padx = 10
pady =10
Button(root, text='ch1 on', command=ch1_on).grid(row=1, column=1, padx=padx, pady=pady)
Button(root, text='ch1 off', command=ch1_off).grid(row=1, column=2, padx=padx, pady=pady)
Button(root, text='ch2 on', command=ch2_on).grid(row=2, column=1, padx=padx, pady=pady)
Button(root, text='ch2 off', command=ch2_off).grid(row=2, column=2, padx=padx, pady=pady)
Button(root, text='ch3 on', command=ch3_on).grid(row=3, column=1, padx=padx, pady=pady)
Button(root, text='ch3 off', command=ch3_off).grid(row=3, column=2, padx=padx, pady=pady)
Button(root, text='ch4 on', command=ch4_on).grid(row=4, column=1, padx=padx, pady=pady)
Button(root, text='ch4 off', command=ch4_off).grid(row=4, column=2, padx=padx, pady=pady)
Button(root, text='ch5 on', command=ch5_on).grid(row=5, column=1, padx=padx, pady=pady)
Button(root, text='ch5 off', command=ch5_off).grid(row=5, column=2, padx=padx, pady=pady)
Button(root, text='ch6 on', command=ch6_on).grid(row=6, column=1, padx=padx, pady=pady)
Button(root, text='ch6 off', command=ch6_off).grid(row=6, column=2, padx=padx, pady=pady)
Button(root, text='ch7 on', command=ch7_on).grid(row=7, column=1, padx=padx, pady=pady)
Button(root, text='ch7 off', command=ch7_off).grid(row=7, column=2, padx=padx, pady=pady)
Button(root, text='ch8 on', command=ch8_on).grid(row=8, column=1, padx=padx, pady=pady)
Button(root, text='ch8 off', command=ch8_off).grid(row=8, column=2, padx=padx, pady=pady)
Button(root, text='ch9 on', command=ch9_on).grid(row=9, column=1, padx=padx, pady=pady)
Button(root, text='ch9 off', command=ch9_off).grid(row=9, column=2, padx=padx, pady=pady)
Button(root, text='ch10 on', command=ch10_on).grid(row=10, column=1, padx=padx, pady=pady)
Button(root, text='ch10 off', command=ch10_off).grid(row=10, column=2, padx=padx, pady=pady)
mainloop()

serialPort.close()