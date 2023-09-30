from tkinter import *
import customtkinter
import backend
import sys

def temp_text(e, i):
    i.delete(0, "end")

def obtain_logins(ui_username, ui_pswrd):
    username = ui_username.get()
    password = ui_pswrd.get()
    if backend.log_in(username, password):
        print("chaging to mode view")
        mode.pack(fill='both', expand=1)
        welcome.pack_forget()

def register_user(ui_username, ui_pswrd):
    username = ui_username.get()
    password = ui_pswrd.get()
    backend.register(username, password)


def welcome_page(welcome):
    #welcome = Modes_page(mode)

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



def Modes_page(Modes):

    label = Label(Modes, text="Select the Pacing Mode", font=('Arial', 14))
    label.pack(padx=20, pady=20)

    AOO_btn = Button(Modes, text="AOO", font=('Arial', 12))
    AOO_btn.pack(padx=20, pady=10)

    VOO_btn = Button(Modes, text="VOO", font=('Arial', 12))
    VOO_btn.pack(padx=20, pady=10)

    AAI_btn = Button(Modes, text="AAI", font=('Arial', 12))
    AAI_btn.pack(padx=20, pady=10)

    VVI_btn = Button(Modes, text="VVI", font=('Arial', 12))
    VVI_btn.pack(padx=20, pady=10)

    

if __name__ == "__main__":
    
    win = Tk()
    win.title("Pacemaker UI")
    win.geometry("500x580")
    mode = Frame(win)
    welcome = Frame(win)
    welcome_page(welcome)
    Modes_page(mode)
    welcome.pack(fill='both', expand=1)
    win.mainloop()


