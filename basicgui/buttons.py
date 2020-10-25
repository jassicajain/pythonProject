
from tkinter import *

root =Tk()
root.geometry("655x333")

def hello():
    print("Hello tkinter Buttons")

def name():
    print("Name is jassica")

def jassica():
    print("surname=jain")

def college():
    print("gtbit")

frame = Frame(root, borderwidth=6, bg="grey", relief=SUNKEN)
frame.pack(side=LEFT, anchor="nw")

b1 = Button(frame, fg="red", text="Print now", command=hello)
b1.pack(side=LEFT, padx=23)

b2 = Button(frame, fg="red", text="Tell me name now", command=name)
b2.pack(side=LEFT, padx=23)

b3 = Button(frame, fg="red", text="Print now",command=jassica)
b3.pack(side=LEFT, padx=23)

b4 = Button(frame, fg="red", text="Print now",command=college)
b4.pack(side=LEFT, padx=23)
root.mainloop()
