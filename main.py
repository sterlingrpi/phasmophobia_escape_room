import threading
import queue
import time
import random
from object_detection import Camera
from tkinter import Tk, mainloop, HORIZONTAL, Text, Canvas
from PIL import Image, ImageTk
from tkinter.ttk import Progressbar, Button

from cv2 import VideoCapture, cvtColor, COLOR_BGR2RGB

#initialize parameters
hunting = True

#initialize queues
image_queue = queue.Queue()
text_queue = queue.Queue()

#initialize camera
camera = Camera()

#define threads
def video_thread():
    while True:
        if image_queue.empty():
            camera.capture_image()
            if hunting:
                camera.run_detector()
            image = camera.get_image()
            image_queue.put(image)
        else:
            time.sleep(1)

def voice_thread():
    while True:
        if text_queue.empty():
            text = 'text ' + str(random.randint(0, 10))
            text_queue.put(text)
        else:
            time.sleep(10)

#start threads
threading.Thread(target=video_thread, daemon=True).start()
threading.Thread(target=voice_thread, daemon=True).start()
time.sleep(1)


# creating GUI
root = Tk()
root.geometry('800x600')
ghost_canvas = Canvas(root, width=800, height=800)  # Create 200x200 Canvas widget

# initializing image
image = ImageTk.PhotoImage(Image.open("cam.jpg"))
image_canvas = ghost_canvas.create_image(20,
                                        20,
                                        anchor='nw',
                                        image=image,
                                        )
ghost_canvas.pack()

def update_image(event):
    if image_queue.empty() and text_queue.empty():
        print('all queues empty zzz...')
        time.sleep(0.5)
    else:
        if not image_queue.empty():
            global ghost_canvas
            global image_canvas
            global image

            image = image_queue.get()

            image = cvtColor(image, COLOR_BGR2RGB)  # to RGB
            image = Image.fromarray(image)  # to PIL format
            image = ImageTk.PhotoImage(image)  # to ImageTk format

            ghost_canvas.itemconfig(image_canvas, image=image)  # change the displayed picture
            ghost_canvas.pack()

            print('updating image')
        if not text_queue.empty():
            text = text_queue.get()
            print(text)

root.bind('<Right>', update_image) # on right arrow key display random note
ghost_canvas.mainloop()