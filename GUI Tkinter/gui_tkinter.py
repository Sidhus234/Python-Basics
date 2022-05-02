# https://docs.python.org/3/library/tk.html
from tkinter import *

# Tkinter program is made of two main things - window and widgets
# widgets are created between initiating window and between window.mainloop
# create an empty window
window = Tk()


def km_to_miles():

    miles = float(e1_value.get()) / 1.6
    t1.insert(END, miles)
    return


b1 = Button(window, text="Execute", command=km_to_miles)
# b1.pack() # method to add button on window (alternate method is grid)
# rowspan to tell if it spans over more than 1 row
b1.grid(row=0, column=0, rowspan=2)

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1, rowspan=1)

t1 = Text(window, height=1, width=20)
t1.grid(row=0, column=2)

window.mainloop()
