from tkinter import *

root = Tk()
# gui logic here

root.geometry("644x434")        # "Width x Height"

root.minsize(300,100)           # width , height

root.maxsize(1200,988)          # width , height


shakaib = Label(text="Shakaib is a good boy and this is his GUI")
shakaib.pack()



root.mainloop()