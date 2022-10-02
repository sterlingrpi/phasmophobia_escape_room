import threading
import time
from tkinter import Tk, mainloop, HORIZONTAL, Text, Canvas, Label, Frame
from tkinter.ttk import Progressbar, Button
from PIL import Image, ImageTk
from pygame import mixer
from cv2 import VideoCapture, cvtColor, COLOR_BGR2RGB
from object_detection import Camera
from voice_recognition import Voice
from house import House

#initialize parameters
hunting = True
text = ''

#initialize objects
camera = Camera()
voice = Voice()
house = House()
mixer.init()

# creating GUI
ghost_window = Tk()
ghost_window.geometry('800x600')

# initializing image
ghost_frame = Frame(ghost_window, width=1600, height=900)
ghost_frame.grid(row=0, column=0, padx=10, pady=2)
image_label = Label(ghost_frame)
image_label.grid(row=0, column=0)

# define threads
def update_image():
    #https://stackoverflow.com/questions/32342935/using-opencv-with-tkinter
    camera.capture_image()
    camera.run_detector()
    image = camera.get_image()

    imgtk = ImageTk.PhotoImage(Image.fromarray(cvtColor(image, COLOR_BGR2RGB)))

    image_label.imgtk = imgtk
    image_label.configure(image=imgtk)
    image_label.after(10, update_image)

def voice_thread():
    global text
    # initializing text label
    text_label = Label(ghost_window, text="")
    text_label.place(x=70, y=90)
    while True:
        text = voice.get_text()
        if text:
            text_label.configure(text=text)

def sound_thread(file, seconds):
    time_end = time.time() + seconds
    while time_end > time.time():
        print('playing sound')
        mixer.music.load(file)
        mixer.music.play()

def interatction_thread():
    global text
    while True:
        try:
            if 'show' in text or 'sign' in text:
                house.blink()
                text = ''
            if 'fan' in text:
                house.fan()
                text = ''
            if 'book' in text:
                house.book()
                text = ''
            if 'where' in text:
                text = ''
                if camera.are_you_near():
                    mixer.music.load('sounds/behind.mp3')
                    mixer.music.play()
                else:
                    mixer.music.load('sounds/away.mp3')
                    mixer.music.play()
            if 'old' in text:
                mixer.music.load('sounds/adult.mp3')
                mixer.music.play()
                text = ''
            if 'hide and seek' in text:
                hunt_seconds = 15
                # threading.Thread(target=sound_thread,
                #                  args=('sounds/gurgle.mp3', hunt_seconds),
                #                  daemon=True).start()
                mixer.music.load('sounds/gurgle.mp3')
                mixer.music.play(-1)
                house.hunt_sequence(hunt_seconds)
        except:
            pass
        time.sleep(0.1)

def sanity_thread():
    # initializing sanity meter
    sanity_label = Label(ghost_window, text="sanity")
    sanity_label.grid(row=1, column=0)
    sanity_bar = Progressbar(ghost_window,
                             orient=HORIZONTAL,
                             length=500,
                             mode='determinate', )
    sanity_bar['value'] = 100
    sanity_bar.grid(row=2, column=0)
    while True:
        time.sleep(3)
        sanity_bar['value'] = sanity_bar['value'] -1
        if sanity_bar['value'] <= 0:
            print('start hunt sequence')
            sanity_bar['value'] = 100

# start threads
update_image()
threading.Thread(target=voice_thread, daemon=True).start()
threading.Thread(target=interatction_thread, daemon=True).start()
threading.Thread(target=sanity_thread, daemon=True).start()
ghost_window.mainloop()