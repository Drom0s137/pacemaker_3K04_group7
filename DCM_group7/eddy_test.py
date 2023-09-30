# Import the required libraries
from tkinter import *
from tkinter import font

# Create an instance of tkinter frame or window
win = Tk()

# Set the size of the window
win.geometry("700x350")

# Create two frames in the window
greet = Frame(win)
order = Frame(win)

# Define a function for switching the frames
def change_to_greet():
   greet.pack(fill='both', expand=1)
   order.pack_forget()

def change_to_order():
   order.pack(fill='both', expand=1)
   greet.pack_forget()

# Create fonts for making difference in the frame
font1 = font.Font(family='Georgia', size='22', weight='bold')
font2 = font.Font(family='Aerial', size='12')

# Add a heading logo in the frames
label1 = Label(greet, text="Hey There! Welcome to TutorialsPoint.", foreground="green3", font=font1)
label1.pack(pady=20)

label2 = Label(order, text="Find all the interesting Tutorials.", foreground="blue", font=font2)
label2.pack(pady=20)

# Add a button to switch between two frames
btn1 = Button(win, text="Switch to Greet", font=font2, command=change_to_order)
btn1.pack(pady=20)

btn2 = Button(win, text="Switch to Order", font=font2, command=change_to_greet)
btn2.pack(pady=20)

win.mainloop()