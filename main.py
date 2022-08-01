import tkinter
from tkinter import *
from PIL import ImageTk,Image
from tkinter.filedialog import *
from tkinter import filedialog
from matplotlib.offsetbox import TextArea
import os

def AIMouse():
    from AImouse import ai_Mouse
def AIKeyboard():
    from AIKeyboard import ai_Keyboard
def AIPainter():
    from VirtualPainter import virtual_Painter

root = Tk()
root.geometry('620x450')
root.title("Main Window")
f1 = Frame(root, bg="white",borderwidth=20)
f1.pack(side=TOP)
l = Label(f1, text="!! WELCOME !!", bg ="white", fg ="red", font="ariel 20 italic")
l.pack()

for i in range(3):
    root.columnconfigure(i, weight=1, minsize=75)
    root.rowconfigure(i, weight=1, minsize=50)

top_frame = tkinter.Frame(root).pack()

b1 = Button(top_frame, fg="red", font="Calibri 15 italic", text = " AI Virtual Mouse ", command = AIMouse)
b1.pack(side=TOP, padx=23, pady=23)

b2 = Button(top_frame, fg="red", font="Calibri 15 italic", text = " AI Virtual Keyboard ", command= AIKeyboard)
b2.pack(side=TOP, padx=23, pady=23)

b3 = Button(top_frame, fg="red", font="Calibri 15 italic", text = " AI Virtual Painter ", command= AIPainter)
b3.pack(side=TOP, padx=23, pady=23)

b4 = Button(top_frame, fg="red", font="Calibri 15 italic", text = " Exit program ", command=root.quit)
b4.pack(side=TOP, padx=23, pady=23)



root.mainloop()