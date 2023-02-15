from tkinter import *

window = Tk()
window.title("GUI Program")
window.minsize(width=500, height=400)

# Label
label = Label(text="Welcome to Tkinter")
label.grid(row=0,column=0)


def clicked():
    answer = input.get()
    label.config(text=answer)


# Button


button = Button(text="Click me", command=clicked)
button.grid(row=0,column=0)

# Input

input = Entry(width=10)
input.grid(row=9, column=10)


window.mainloop()
