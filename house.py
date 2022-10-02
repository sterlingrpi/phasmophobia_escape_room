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

        self.outlet_6 = [b'a', b'b']
        self.outlet_7 = [b'c', b'd']
        self.outlet_8 = [b'e', b'f']
        self.outlet_9 = [b'g', b'h']
        self.outlet_10 = [b'i', b'j']

        self.lamps = [self.outlet_1, self.outlet_2]
        self.book_outlet = self.outlet_4
        self.fan_outlet = self.outlet_5
        self.emf_outlet = self.outlet_6
        self.fingies_outout = self.outlet_7
        self.solenoid_outlet = self.outlet_8
        self.hunt_outlets = [self.outlet_1,
                             self.outlet_2,
                             self.outlet_3,
                             self.outlet_4,
                             self.outlet_5]
    def on(self, outlet):
        self.serialPort.write(outlet[0])

    def off(self, outlet):
        self.serialPort.write(outlet[1])

    def blink(self):
        print('do the blink')
        outlet = random.choice(self.lamps)
        for _ in range(2):
            self.off(outlet)
            time.sleep(0.5)
            self.on(outlet)
            time.sleep(0.5)

    def interaction_thread(self, outlet, seconds):
        print('outlet', outlet)
        print('seconds', seconds)
        self.on(outlet)
        time.sleep(seconds)
        self.off(outlet)

    def book(self):
        threading.Thread(target=self.interaction_thread,
                         args=(self.book_outlet, 20),
                         daemon=True).start()
    def fan(self):
        threading.Thread(target=self.interaction_thread,
                         args=(self.fan_outlet, 10),
                         daemon=True).start()

    def old(self):
        self.mixer.music.load('sounds/adult.mp3')
        self.mixer.music.play()

    def hunt_sequence(self, seconds):
        time_end = time.time() + seconds
        while time_end > time.time():
            for outlet in self.hunt_outlets:
                if random.choice(['on', 'off']) == 'on':
                    self.on(outlet)
                else:
                    self.off(outlet)
            time.sleep(1)
        for outlet in self.hunt_outlets:
            self.off(outlet)


if __name__ == '__main__':
    house = House()
    print('turn light off')
    house.blink()