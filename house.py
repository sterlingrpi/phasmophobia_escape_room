import serial
import time
from pygame import mixer  # Load the popular external library
import random
import threading

class House:
    def __init__(self):
        self.mixer = mixer
        # 'Headphones (Realtek(R) Audio)', 'Speakers (Realtek(R) Audio)', 'ASUS VA24E (NVIDIA High Definition Audio)', 'Speakers (Jabra EVOLVE LINK)'
        self.mixer_speaker = 'Headphones (Realtek(R) Audio)'
        self.mixer_sb7 = 'Headphones (Realtek(R) Audio)'

        self.serialPort = serial.Serial(port="COM3",
                                        baudrate=9600,
                                        bytesize=8,
                                        timeout=2,
                                        stopbits=serial.STOPBITS_ONE,
                                        )
        print('initializing serial...')
        time.sleep(2)
        self.serialPort.write(b'3')

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

        self.lamps = [self.outlet_1, self.outlet_2, self.outlet_9]
        self.book_outlet = self.outlet_4
        self.emf_outlet = self.outlet_5
        self.throw_outlet = self.outlet_6
        self.fan_outlet = self.outlet_7
        self.fingies_outout = self.outlet_8
        self.hunt_outlets = [self.outlet_1,
                             self.outlet_2,
                             self.outlet_3,
                             self.outlet_4,
                             self.outlet_5,
                             self.outlet_7,
                             self.outlet_8]

        self.ghost_chars = [b'k', b'l']

        for outlet in self.lamps:
            self.on(outlet)

    def on(self, char):
        self.serialPort.write(char[0])

    def off(self, char):
        self.serialPort.write(char[1])

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

    def emf(self):
        threading.Thread(target=self.interaction_thread,
                         args=(self.emf_outlet, 10),
                         daemon=True).start()

    def fingies(self):
        threading.Thread(target=self.interaction_thread,
                         args=(self.fingies_outout, 20),
                         daemon=True).start()

    def fan(self):
        threading.Thread(target=self.interaction_thread,
                         args=(self.fan_outlet, 10),
                         daemon=True).start()

    def throw(self):
        threading.Thread(target=self.interaction_thread,
                         args=(self.throw_outlet, 2),
                         daemon=True).start()

    def play_sound(self, file):
        mixer.init(devicename=self.mixer_speaker)
        mixer.music.load(file)
        mixer.music.play()
        while mixer.music.get_busy():
            time.sleep(0.1)
        mixer.quit()

    def sb7_sound(self, file):
        mixer.init(devicename=self.mixer_sb7)
        mixer.music.load(file)
        mixer.music.play()
        while mixer.music.get_busy():
            time.sleep(0.1)
        mixer.quit()

    def sound_thread(self, file, stop):
        mixer.init(devicename=self.mixer_speaker)
        mixer.music.load(file)
        while True:
            if not self.mixer.music.get_busy():
                mixer.music.play()
            else:
                time.sleep(0.1)
            if stop():
                break

    def hunt_sequence(self, duration):
        hunt_end = time.time() + duration
        stop = False
        gurgle_tread = threading.Thread(target=self.sound_thread,
                                        daemon=True,
                                        args=('sounds/gurgle.mp3', lambda: stop,))
        gurgle_tread.start()
        self.on(self.ghost_chars)
        while hunt_end > time.time():
            for outlet in self.hunt_outlets:
                if random.choice(['on', 'off']) == 'on':
                    self.on(outlet)
                else:
                    self.off(outlet)
            time.sleep(1)
        stop = True
        gurgle_tread.join()
        for outlet in self.hunt_outlets:
            self.off(outlet)
        self.off(self.ghost_chars)


if __name__ == '__main__':
    house = House()
    print('turn light off')
    house.blink()