from tkinter import *
from tkinter import ttk
 
window = Tk()

scale_1 = Scale(window, orient='horizontal', resolution=1, length=400, from_=0, to=30)
scale_1.pack(padx=10, pady=30, anchor='nw')

# def fontSize():
#     label_1.config(font=('Candara', int(scale_1.get())))

def slider_mod():
    current = float(scale_1.get())

    if current < 10 or current > 20:
        scale_1.config(resolution=(5))
    else:
        scale_1.config(resolution=(1))

scale_1.config(command=lambda e: slider_mod())

window.mainloop()
