from tkinter import *
from PIL  import Image,ImageTk

root = Tk()

root.geometry("1255x944")
#photo = PhotoImage(file="Snapchat-18663821.jpg")

image = Image.open("Snapchat-18663821.jpg")
photo = ImageTk.PhotoImage(image)

label1 = Label(image=photo)
label1.pack()

root.mainloop()
