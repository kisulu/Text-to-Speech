import tkinter as tk
from tkinter import *
try:
    import pyttsx3
    pyttsx3_availabe = True
except ImportError:
    pyttsx3_availabe = False


Engine = pyttsx3.init()

def speak():
    Engine.say(text_voice.get())
    Engine.runAndWait()
    Engine.stop()


root = Tk()

text_voice = StringVar()

obj = LabelFrame(root, text="Text to Speech", font=20, bd=1)
obj.pack(fill="both", expand=1, padx=10, pady=10)

label = Label(obj, text="Text", font=30)
label.pack(side=tk.LEFT, padx=5)

text = Entry(obj, textvariable=text_voice, font=30, width=25, bd=5)
text.pack(side=tk.LEFT, padx=10)

button = Button(obj, text="Speak", font=20, bg="black", fg="white", command=speak)
button.pack(side=tk.LEFT, padx=10)

root.title("Text to Speech")
root.geometry("400x200")
root.resizable(False, False)

root.mainloop()

