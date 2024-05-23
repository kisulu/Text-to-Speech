import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
from tkinter import messagebox
import os

try:
    import pyttsx3
    pyttsx3_availabe = True
except ImportError:
    pyttsx3_availabe = False


Engine = pyttsx3.init()

def speak():
    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = Engine.getProperty('voices')

    def setvoice():
        if (gender == 'Male'):
            Engine.setProperty('voice', voices[0].id)
            Engine.say(text)
            Engine.runAndWait()
            #Engine.stop()
        else:
            Engine.setProperty('voice', voices[1].id)
            Engine.say(text)
            Engine.runAndWait()
            #Engine.stop()

    if(text):
        if  (speed == 'Fast'):
            Engine.setProperty('rate', 200)
            setvoice()

        elif (speed == 'Normal'):
            Engine.setProperty('rate', 150)
            setvoice()

        else:
            Engine.setProperty('rate', 60)
            setvoice()

            

def download():
    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = Engine.getProperty('voices')

    def setvoice():
        if (gender == 'Male'):
            Engine.setProperty('voice', voices[0].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            Engine.save_to_file(text, 'test.mp3')
            Engine.runAndWait()
            #Engine.stop()
        else:
            Engine.setProperty('voice', voices[1].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            Engine.save_to_file(text, 'test.mp3')
            Engine.runAndWait()
            #Engine.stop()

    if(text):
        if  (speed == 'Fast'):
            Engine.setProperty('rate', 200)
            setvoice()

        elif (speed == 'Normal'):
            Engine.setProperty('rate', 150)
            setvoice()

        else:
            Engine.setProperty('rate', 60)
            setvoice()

    # Engine.save_to_file('Hello World', 'test.mp3')
    # Engine.runAndWait()
    # messagebox.showinfo("Saved", "Successfully saved") since we are asking directory we dont need messagebox

root = Tk()
root.config(bg="#305065")

##### icon
image_icon = PhotoImage(file="speak.png")
root.iconphoto(False, image_icon)

#### top frame
top_frame = Frame(root, bg="white", width=900, height=100)
top_frame.place(x=0, y=0)

logo = PhotoImage(file="logo.png")
label = Label(top_frame, image=logo, bg="white")
label.place(x=10, y=5)

Label(top_frame, text="TEXT TO SPEECH", font="arial 20", bg="white", fg="black").place(x=100,y=30)

text_area= Text(root, font="Robote 20", bg="white", fg="black", relief=GROOVE, wrap=WORD)
text_area.place(x=10,y=150, width=500, height=250)


Label(root, text="VOICE", font="arial 15 bold", bg="#305065", fg="WHITE").place(x=580,y=160)
Label(root, text="SPEED", font="arial 15 bold", bg="#305065", fg="white").place(x=760,y=160)

gender_combobox= Combobox(root, values=['Male','Female'],font="arial 14", state='r',width=10)
gender_combobox.place(x=550,y=200)
gender_combobox.set("Male")

speed_combobox= Combobox(root, values=['Fast','Normal', 'Slow'],font="arial 14", state='r',width=10)
speed_combobox.place(x=730,y=200)
speed_combobox.set("Normal")

imageicon=PhotoImage(file="speaker.png")
btn = Button(root, text="Speak", compound=LEFT, image=imageicon, width=130, font="arial 14 bold", command=speak)
btn.place(x=550, y=280)

imageicon2=PhotoImage(file="download.png")
save = Button(root, text="Save", compound=LEFT, image=imageicon2,bg="#39c790", width=130, font="arial 14 bold", command=download)
save.place(x=730, y=280)

root.title("Text to Speech")
root.geometry("900x450")
root.resizable(False, False)

root.mainloop()
