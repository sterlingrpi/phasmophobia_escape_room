import threading
import queue
import time
import random
from object_detection import Camera
from voice_recognition import Voice
from tkinter import Tk, mainloop, HORIZONTAL, Text, Canvas, Label, Frame
from PIL import Image, ImageTk
from tkinter.ttk import Progressbar, Button

from cv2 import VideoCapture, cvtColor, COLOR_BGR2RGB

#initialize parameters
hunting = True

#initialize objects
camera = Camera()
voice = Voice()

# creating GUI
ghost_window = Tk()
ghost_window.geometry('800x600')

# initializing image
ghost_frame = Frame(ghost_window, width=900, height=600)
ghost_frame.grid(row=0, column=0, padx=10, pady=2)
image_label = Label(ghost_frame)
image_label.grid(row=0, column=0)

# initializing text
text_label = Label(ghost_window, text="")
text_label.place(x=70, y=90)

# define threads
def update_image():
    #https://stackoverflow.com/questions/32342935/using-opencv-with-tkinter
    camera.capture_image()
    if hunting:
        camera.run_detector()
    image = camera.get_image()

    imgtk = ImageTk.PhotoImage(Image.fromarray(cvtColor(image, COLOR_BGR2RGB)))

    image_label.imgtk = imgtk
    image_label.configure(image=imgtk)
    image_label.after(10, update_image)

def voice_thread():
    while True:
        text = voice.get_text()
        if text:
            text_label.configure(text=text)

# start threads
update_image()
threading.Thread(target=voice_thread, daemon=True).start()
ghost_window.mainloop()