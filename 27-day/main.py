# Day 27 - Mile to KM Coverter
# A Python GUI Project

from tkinter import *

def calculate():
    miles = float(miles_input.get())
    km = miles * 1.6
    km_num_label.config(text=f"{km:.2f}")

window = Tk()
window.title("My First GUI Program")
window.config(padx=20, pady=20)

miles_input = Entry(width=10)
miles_input.grid(row=0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

equal_label = Label(text="is equal to")
equal_label.grid(row=1, column=0)

km_num_label = Label(text="0")
km_num_label.grid(row=1, column=1)

km_label = Label(text="km")
km_label.grid(row=1, column=2)

calc = Button(text="Calculate", command=calculate)
calc.grid(row=2, column=1)

window.mainloop()
