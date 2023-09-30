from tkinter import *


welcome = Tk()
welcome.title("Pacemaker UI")
welcome.geometry("500x580")

label = Label(welcome, text="Welcome to Pacemaker Interface", font=('Arial', 14))
label.pack(padx=20, pady=20)

username = Entry(welcome, width=20)
username.insert(0, "Enter Username")
username.pack(pady=2, padx=10)
# self.username.bind("<FocusIn>", DCM.clr_text)

password = Entry(welcome, width=20)
password.insert(0, "Enter Password")
password.pack(pady=2, padx=10)
# password.bind("<FocusIn>", DCM.clr_text(self, self.password))

login = Button(welcome, text="Login", font=('Arial', 12))
login.pack(padx=20, pady=10)

register = Button(welcome, text="Register", font=('Arial', 12))
register.pack(padx=20, pady=10)

quit = Button(welcome, text="Quit", font=('Arial', 12))
quit.pack(padx=20, pady=10)

welcome.mainloop()

    # def clr_text(self):
<<<<<<< HEAD
<<<<<<< HEAD
    #     self.delete(0, "end")
=======
    #     self.delete(0, "end")
>>>>>>> parent of 8509ee4 (Adding UI updates)
=======
    #     self.delete(0, "end")
>>>>>>> parent of 8509ee4 (Adding UI updates)
