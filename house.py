import serial
import time
from pygame import mixer  # Load the popular external library
import random
import threading

class House:
    def __init__(self):
        self.serialPort = serial.Serial(port="COM3",
                                        baudrate=9600,
                                        bytesize=8,
                                        timeout=2,
                                        stopbits=serial.STOPBITS_ONE,
                                        )
        print('initializing serial...')
        time.sleep(2)
        self.serialPort.write(b'3')

        self.mixer = mixer.init()
        self.outlet_1 = [b'0', b'1']
        self.outlet_2 = [b'2', b'3']
        self.outlet_3 = [b'4', b'5']
        self.outlet_4 = [b'6', b'7']
        self.outlet_5 = [b'8', b'9']
        self.lamps = [self.outlet_1, self.outlet_2]

    def off(self, outlet):
        self.serialPort.write(outlet[0])

    def on(self, outlet):
        self.serialPort.write(outlet[1])

    def blink(self):
        print('do the blink')
        outlet = random.choice(self.lamps)
        for _ in range(2):
            self.off(outlet)
            time.sleep(0.5)
            self.on(outlet)
            time.sleep(0.5)

    def fan_thread(self):
        self.on(self.outlet_5)
        time.sleep(10)
        self.off(self.outlet_5)

    def fan(self):
        threading.Thread(target=self.fan_thread, daemon=True).start()

    def book_thread(self):
        self.on(self.outlet_4)
        time.sleep(20)
        self.off(self.outlet_4)

    def book(self):
        threading.Thread(target=self.book_thread, daemon=True).start()

    def old(self):
        self.mixer.music.load('sounds/adult.mp3')
        self.mixer.music.play()


if __name__ == '__main__':
    house = House()
    print('turn light off')
    house.off()
    house.old()