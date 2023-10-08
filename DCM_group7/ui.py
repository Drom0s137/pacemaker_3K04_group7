from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
import customtkinter
import backend
import mode


def temp_text(e, i):
    i.delete(0, "end")

def switch_frame(new, old):
    global CURRENT_FRAME
    new.pack(fill='both', expand=1)
    old.pack_forget()
    CURRENT_FRAME = new

def obtain_logins(ui_username, ui_pswrd):
    username = ui_username.get()
    password = ui_pswrd.get()
    if backend.log_in(username, password):
        print("chaging to mode view")
        switch_frame(modes, CURRENT_FRAME)

def register_user(ui_username, ui_pswrd):
    username = ui_username.get()
    password = ui_pswrd.get()
    backend.register(username, password)


def welcome_page(welcome):
    #welcome = Modes_page(mode)

    #welcome = ThemedTk(theme="arc")

    label = ttk.Label(welcome, text="Welcome to Pacemaker Interface", font=('Arial', 14))
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

    login = ttk.Button(welcome, command = lambda: obtain_logins(ui_username, ui_pswrd), text="Login")
    login.pack(padx=20, pady=10)

    register = ttk.Button(welcome, command = lambda: register_user(ui_username, ui_pswrd), text="Register")
    register.pack(padx=20, pady=10)

    log_out = ttk.Button(welcome, text="Log Out")
    log_out.pack(padx=20, pady=10)

    quit = ttk.Button(welcome, command = backend.exit_system, text="Quit")
    quit.pack(padx=20, pady=10)

def Modes_page(Modes):

    label = ttk.Label(Modes, text="Select the Pacing Mode", font=('Arial', 14))
    label.pack(padx=20, pady=20)

    AOO_btn = ttk.Button(Modes, text="AOO", command = lambda: switch_frame(aoo, CURRENT_FRAME))
    AOO_btn.pack(padx=20, pady=10)

    VOO_btn = ttk.Button(Modes, text="VOO", command = lambda: switch_frame(voo, CURRENT_FRAME))
    VOO_btn.pack(padx=20, pady=10)

    AAI_btn = ttk.Button(Modes, text="AAI", command = lambda: switch_frame(aai, CURRENT_FRAME))
    AAI_btn.pack(padx=20, pady=10)

    VVI_btn = ttk.Button(Modes, text="VVI", command = lambda: switch_frame(vvi, CURRENT_FRAME))
    VVI_btn.pack(padx=20, pady=10)

    back = ttk.Button(Modes, text="BACK", width=10, command=mode.Back_press)
    back.pack(pady=10)

if __name__ == "__main__":
    global CURRENT_FRAME
    #win = Tk()
    win = ThemedTk(theme="radiance") # Use this instead of Tk() to have themes
    win.iconbitmap("McMaster.ico")
    win.title("Pacemaker UI")
    win.geometry("500x580")
    modes = Frame(win)
    welcome = Frame(win)
    aoo = Frame(win)
    voo = Frame(win)
    aai = Frame(win)
    vvi = Frame(win)
    welcome_page(welcome)
    Modes_page(modes)
    mode.AOO_page(aoo)
    mode.VOO_page(voo)
    mode.AAI_page(aai)
    mode.VVI_page(vvi)
    welcome.pack(fill='both', expand=1)
    CURRENT_FRAME = welcome
    win.mainloop()


