import threading
import time
from tkinter import Tk, mainloop, HORIZONTAL, VERTICAL, Text, Canvas, Label, Frame, Button
from tkinter.ttk import Progressbar
from PIL import Image, ImageTk
from pygame import mixer
from cv2 import VideoCapture, cvtColor, COLOR_BGR2RGB
import random
from object_detection import Camera
from voice_recognition import Voice
from house import House

#initialize parameters
time_to_hunt = 60*5
hunt_duration = 30
grace_period = 15
run_threads = True
text = ''
temperature = 68

#initialize objects
camera = Camera()
voice = Voice()
house = House()
mixer.init()

# creating GUI
ghost_window = Tk()
ghost_window.geometry('900x600')

# initializing image
ghost_frame = Frame(ghost_window, width=1600, height=900)
ghost_frame.grid(row=0, column=0, padx=10, pady=2)
image_label = Label(ghost_frame)
image_label.grid(row=0, column=0)

# define hunt function
def hunt(duration, grace):
    house.hunt_sequence(duration=duration)
    hunt_end = time.time() + duration
    grace_end = time.time() + grace
    while hunt_end > time.time():
        if time.time() > grace_end:
            if camera.are_you_near():
                print('you are dead')
                house.play_sound('sounds/death.mp3')
                camera.display_image()
                break
        time.sleep(0.1)

# define threads
def update_image():
    #https://stackoverflow.com/questions/32342935/using-opencv-with-tkinter
    if run_threads:
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
    text_label.place(x=20, y=20)
    while True:
        if run_threads:
            text = voice.get_text()
            if text:
                text_label.configure(text=text)
        else:
            time.sleep(1)

def interatction_thread():
    global text
    global temperature
    while True:
        if run_threads:
            try:
                if 'show' in text or 'sign' in text:
                    text = ''
                    house.blink()
                if 'fan' in text:
                    text = ''
                    house.fan()
                if 'book' in text:
                    text = ''
                    house.book()
                if 'EMF' in text:
                    text = ''
                    house.emf()
                if 'finger' in text:
                    house.fingies()
                    text = ''
                if 'throw' in text:
                    house.throw()
                    text = ''
                if 'where' in text:
                    text = ''
                    if camera.are_you_near():
                        house.sb7_sound('sounds/behind.mp3')
                    else:
                        house.sb7_sound('sounds/away.mp3')
                if ' old ' in text:
                    text = ''
                    house.sb7_sound('sounds/adult.mp3')
                if 'cold' in text:
                    text = ''
                    temperature = 32
                if 'heat' in text:
                    text = ''
                    temperature = 68
                if 'hide and seek' in text:
                    text = ''
                    hunt(duration=hunt_duration, grace=grace_period)
            except:
                pass
            time.sleep(0.1)
        else:
            time.sleep(1)

def sanity_thread():
    # initializing sanity meter
    sanity_label = Label(ghost_window, text="sanity (%)")
    sanity_label.grid(row=1, column=0)
    sanity_bar = Progressbar(ghost_window,
                             orient=HORIZONTAL,
                             length=500,
                             mode='determinate', )
    sanity_bar.grid(row=2, column=0)
    starting_sanity = 100
    sanity_bar['value'] = starting_sanity

    while True:
        if run_threads:
            time.sleep(time_to_hunt/starting_sanity)
            sanity_bar['value'] = sanity_bar['value'] -1
            if sanity_bar['value'] <= 0:
                hunt(duration=hunt_duration, grace=grace_period)
                sanity_bar['value'] = starting_sanity
        else:
            time.sleep(1)

def thermo_thread():
    # initialize thermometer
    global temperature
    thermo_label = Label(ghost_window, text="temperature (F)")
    thermo_label.grid(row=0, column=2)
    thermo_bar = Progressbar(ghost_window,
                             orient=VERTICAL,
                             length=500,
                             mode='determinate', )
    thermo_bar.grid(row=0, column=1)
    thermo_bar['value'] = 68
    while True:
        if run_threads:
            thermo_bar['value'] = temperature + random.random()*2 -1
            time.sleep(0.5)
        else:
            time.sleep(1)

# start threads
update_image()
threading.Thread(target=voice_thread, daemon=True).start()
threading.Thread(target=interatction_thread, daemon=True).start()
threading.Thread(target=sanity_thread, daemon=True).start()
threading.Thread(target=thermo_thread, daemon=True).start()

def start_game():
    global run_threads
    run_threads = True

def stop_game():
    global run_threads
    run_threads = False

Button(ghost_window, text='start game', command=start_game).grid(row=3, column=0)
Button(ghost_window, text='stop game', command=stop_game).grid(row=3, column=1)

ghost_window.mainloop()
