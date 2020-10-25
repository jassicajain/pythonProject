from tkinter import *

root = Tk()

root.geometry("500x400")

root.title("Ready")

title_label = Label(text='''Ready''', bg="green", fg="white", padx=10, pady=10, font="verdana 24 bold",

                    borderwidth=3, relief=SUNKEN)

title_label.pack(side="bottom", fill="x")

root.mainloop()


