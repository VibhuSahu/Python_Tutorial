from tkinter import *
from PIL import Image,ImageTk

root = Tk()
# gui logic here

root.geometry("740x410")                    # Default size of the window


photo = PhotoImage(file="photo1.png")       # The first way to put image in window only for png
photoLable = Label(image=photo)
photoLable.pack()

image = Image.open("bussiness-man.jpg")     # This will put image in window for any image formate
passport = ImageTk.PhotoImage(image)
passportLable = Label(image=passport)
passportLable.pack()


root.mainloop()