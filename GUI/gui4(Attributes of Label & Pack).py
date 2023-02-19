from tkinter import *


root = Tk()
# gui logic here

root.geometry("1244x833")
root.title("My GUI With Harry")
root.iconbitmap("GUI/python.png")


textTkinter = """\n
Qus. What is Tkinter and why is it used?\n
Ans. Tkinter is the de facto way in Python to create Graphical User interfaces (GUIs)\n
     and is included in all standard Python Distributions. In fact, it's the only\n
     framework built into the Python standard library.
"""


# Important Label Options
"""
text = adds the text
bd = background
fg = foreground
font = sets the font
    1. font = ("comicsansms",24,"bold")
    2. font = ("comicsansms 24 bold")

padx = x padding
pady = y padding

relief = border styling - SUNKEN, RAISED, GROOVE, RIDGE
"""
paragraph = Label(text=textTkinter,bg="blue",fg="white",padx=113,pady=100,font=("comicsansms",24,"bold"))


# Important Pack Options
"""
anchor = nw - (north west)
side = top, bottom, left, right
fill
padx
pady
"""

# title_label.pack(side=BOTTOM, anchor ="sw", fill=X)
paragraph.pack(anchor="nw",side="top",fill=X)




root.mainloop()