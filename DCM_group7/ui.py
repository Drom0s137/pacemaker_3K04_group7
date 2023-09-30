from tkinter import *
import customtkinter
import backend
import sys

global login

def temp_text(e, i):
    i.delete(0, "end")

def obtain_logins(ui_username, ui_pswrd):
    username = ui_username.get()
    password = ui_pswrd.get()
    if backend.log_in(username, password):
        login = True
    else:
        login = False

def register_user(ui_username, ui_pswrd):
    username = ui_username.get()
    password = ui_pswrd.get()
    if backend.register(username, password):
        login = 1
    else:
        login = 0

def main():
    welcome = Tk()
    welcome.title("Pacemaker UI")
    welcome.geometry("500x580")

    label = Label(welcome, text="Welcome to Pacemaker Interface", font=('Arial', 14))
    label.pack(padx=20, pady=20)

    #username section
    ui_username = Entry(welcome, bg = "white", width=20)
    ui_username.insert(0, "Enter Username")
    ui_username.pack(pady=2, padx=10)
    def handler(event, i=ui_username):   
        return temp_text(event, i)
    ui_username.bind("<FocusIn>", handler)

    #password section
    ui_pswrd = Entry(welcome, width=20)
    ui_pswrd.insert(0, "Enter Password")
    ui_pswrd.pack(pady=2, padx=10)
    def handler(event, i=ui_pswrd):   
        return temp_text(event, i)
    ui_pswrd.bind("<FocusIn>", handler)

    login = Button(welcome, command = lambda: obtain_logins(ui_username, ui_pswrd), text="Login", font=('Arial', 12))
    login.pack(padx=20, pady=10)

    register = Button(welcome, command = lambda: register_user(ui_username, ui_pswrd), text="Register", font=('Arial', 12))
    register.pack(padx=20, pady=10)

    quit = Button(welcome, command = backend.exit_system, text="Quit", font=('Arial', 12))
    quit.pack(padx=20, pady=10)

    welcome.mainloop()


if __name__ == "__main__":
    main()
