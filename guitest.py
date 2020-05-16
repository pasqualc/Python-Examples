from tkinter import *

global boo = 0
global s1 = "beep"
global s2 = "boop"
global val = ""

def swapText():
    if boo == 1:
        boo = 0
        val = s1
    else:
        boo = 1
        val = s2

root = Tk()
button = Button(root, text='Stop', width=25, command=swapText())
button.pack()
w = Label(root, text=val)
w.pack()
root.mainloop()
