# importing tkinter module
from tkinter import Tk, mainloop, HORIZONTAL, Text, Canvas
from tkinter.ttk import Progressbar, Button
import time

# creating tkinter window
root = Tk()
root.geometry('800x600')

# Progress bar widget
progress = Progressbar(root, orient=HORIZONTAL,
                       length=100, mode='determinate')
progress['value'] = 100

ghost_canvas = Canvas(root, width=200, height=200)  # Create 200x200 Canvas widget
ghost_canvas.pack()

lamp = ghost_canvas.create_oval(50, 50, 100, 100, fill='yellow')  # Create a circle on the Canvas

def blink():
    for _ in range(2):
        ghost_canvas.itemconfig(lamp, fill='gray')
        root.update_idletasks()
        time.sleep(0.5)
        ghost_canvas.itemconfig(lamp, fill='yellow')
        root.update_idletasks()
        time.sleep(0.5)

def spirit_box_loop():
    import speech_recognition as sr
    r = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            print("Talk")
            audio_text = r.listen(source)
            print("Time over, thanks")
        try:
            text = r.recognize_google(audio_text)
            print(text)
            if 'sign' in text:
                blink()
        except:
            print("Sorry, I did not get that")

def update_sanity():
    sanity_values = [100, 80, 60,40, 20, 0]
    for sanity_value in sanity_values:
        progress['value'] = sanity_value
        root.update_idletasks()
        time.sleep(1)

progress.pack(pady=10)

# This button will initialize
# the progress bar
Button(root, text='Sanity drain', command=update_sanity).pack(pady=10)
Button(root, text='Spirit box on', command=spirit_box_loop).pack(pady=10)

# infinite loop
mainloop()