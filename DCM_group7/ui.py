from tkinter import *


class DCM:

    def __init__(self):
        self.welcome = Tk()
        self.welcome.title("Pacemaker UI")
        self.welcome.geometry("500x580")

        self.label = Label(self.welcome, text="Welcome to Pacemaker Interface", font=('Arial', 14))
        self.label.pack(padx=20, pady=20)

        self.username = Entry(self.welcome, width=20)
        self.username.insert(0, "Enter Username")
        self.username.pack(pady=2, padx=10)
        # self.username.bind("<FocusIn>", DCM.clr_text)

        self.password = Entry(self.welcome, width=20)
        self.password.insert(0, "Enter Password")
        self.password.pack(pady=2, padx=10)
        # self.password.bind("<FocusIn>", DCM.clr_text(self, self.password))

        self.login = Button(self.welcome, text="Login", font=('Arial', 12))
        self.login.pack(padx=20, pady=10)

        self.register = Button(self.welcome, text="Register", font=('Arial', 12))
        self.register.pack(padx=20, pady=10)

        self.quit = Button(self.welcome, text="Quit", font=('Arial', 12))
        self.quit.pack(padx=20, pady=10)

        self.welcome.mainloop()

    # def clr_text(self):
    #     self.delete(0, "end")

DCM()
