from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
# Entry

mile = Entry(width=10)
mile.config(text="Miles")
mile.grid(column=1, row=0)

# Mile Label
mile_label = Label(text="Miles")
mile_label.grid(column=2, row=0)

# is equal to Label
equal_to_label = Label(text="is equal to")
equal_to_label.grid(column=0, row=1)

# Converted Km Label


def converter():
    ans = float(mile.get())
    result = round(ans*1.609)
    num.config(text=result)


num = Label(text=0)
num.grid(column=1, row=1)

# Km Label
km = Label(text="Km")
km.grid(column=2, row=1)

# Calculate Button
button = Button(text="Calculate", command=converter)
button.grid(column=1, row=2)
window.mainloop()
