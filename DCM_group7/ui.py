from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
import backend
import mode
import mode_extend


def temp_text(e, i):
    i.delete(0, "end")

def switch_frame(new, old):
    new.pack(fill='both', expand=1)
    old.forget()

def obtain_logins(ui_username, ui_pswrd):
    username = ui_username.get()
    password = ui_pswrd.get()
    if backend.log_in(username, password) == 1:
        print("chaging to mode view")
        mode.update_values()
        switch_frame(modes, welcome)
    else:
        display_msg(backend.log_in(username, password)[1], welcome, 1)

def register_user(ui_username, ui_pswrd):
    username = ui_username.get()
    password = ui_pswrd.get()
    temp = backend.register(username, password)
    if temp[0] == 0:
        display_msg(temp[1], welcome, 1)
    else:
        display_msg("\tSUCCESS\t", welcome, 1)
    
def welcome_page(welcome):
    #welcome = Modes_page(mode)

    #welcome = ThemedTk(theme="arc")

    label = ttk.Label(welcome, text="Welcome to Pacemaker Interface", font=('Arial', 14))
    label.grid(row=0, column=1)

    l0 = Label(welcome, width=42, height=3) # This is blank space just to help center the layout 
    l0.grid(column=0, row=0, rowspan=10)

    #username section
    ui_username = Entry(welcome, bg = "white", width=20)
    ui_username.insert(0, "Enter Username")
    ui_username.grid(row=1,column=1, pady=5)
    def handler(event, i=ui_username):   
        return temp_text(event, i)
    ui_username.bind("<FocusIn>", handler)

    #password section
    ui_pswrd = Entry(welcome, width=20)
    ui_pswrd.insert(0, "Enter Password")
    ui_pswrd.grid(row=2,column=1, pady=5)
    def handler(event, i=ui_pswrd):   
        return temp_text(event, i)
    ui_pswrd.bind("<FocusIn>", handler)

    login = ttk.Button(welcome, command = lambda: obtain_logins(ui_username, ui_pswrd), text="Login")
    login.grid(row=3,column=1, pady=5)

    register = ttk.Button(welcome, command = lambda: register_user(ui_username, ui_pswrd), text="Register")
    register.grid(row=4,column=1, pady=5)

    quit = ttk.Button(welcome, command = backend.exit_system, text="Quit")
    quit.grid(row=5,column=1, pady=5)


def Modes_page(Modes, Welcome):

    label = ttk.Label(Modes, text="Select the Pacing Mode", font=('Arial', 14))
    label.grid(row=0, column=1, columnspan=3, pady=5)

    l0 = Label(Modes, width=45, height=3) # This is blank space just to help center the layout 
    l0.grid(column=0, row=0, rowspan=10)

    AOO_btn = ttk.Button(Modes, text="AOO", command = lambda: switch_frame(aoo, Modes))
    AOO_btn.grid(row=1, column=1, columnspan=1,pady=5, padx=3)

    VOO_btn = ttk.Button(Modes, text="VOO", command = lambda: switch_frame(voo, Modes))
    VOO_btn.grid(row=2, column=1, columnspan=1,pady=5, padx=3)

    AAI_btn = ttk.Button(Modes, text="AAI", command = lambda: switch_frame(aai, Modes))
    AAI_btn.grid(row=3, column=1, columnspan=1,pady=5, padx=3)

    VVI_btn = ttk.Button(Modes, text="VVI", command = lambda: switch_frame(vvi, Modes))
    VVI_btn.grid(row=4, column=1, columnspan=1,pady=5, padx=3)

    AOOR_btn = ttk.Button(Modes, text="AOOR", command = lambda: switch_frame(aoor, Modes)) #Change the page
    AOOR_btn.grid(row=1, column=3, columnspan=1,pady=5, padx=3)

    VOOR_btn = ttk.Button(Modes, text="VOOR", command = lambda: switch_frame(voor, Modes)) #Change the page
    VOOR_btn.grid(row=2, column=3, columnspan=1,pady=5, padx=3)

    AAIR_btn = ttk.Button(Modes, text="AAIR", command = lambda: switch_frame(aair, Modes)) #Change the page
    AAIR_btn.grid(row=3, column=3, columnspan=1,pady=5, padx=3)

    VVIR_btn = ttk.Button(Modes, text="VVIR", command = lambda: switch_frame(vvir, Modes)) #Change the page
    VVIR_btn.grid(row=4, column=3, columnspan=1,pady=5, padx=3)

    back = ttk.Button(Modes, text="BACK", width=10, command=lambda: switch_frame(Welcome, Modes))
    back.grid(row=5, column=1, columnspan=3)

def display_msg(msg, frame, where):
    label = ttk.Label(frame, text=msg, foreground="red", font=('Arial', 10))
    label.grid(row=50,column=where)

def display_ext_msg(msg, frame, where):
    label = ttk.Label(frame, text=msg, foreground="red", font=('Arial', 10))
    label.grid(row=50,column=where, columnspan=4)

if __name__ == "__main__":
    #win = Tk()
    win = ThemedTk(theme="radiance") # Use this instead of Tk() to have themes
    win.iconbitmap("McMaster.ico")
    win.title("Pacemaker UI")
    win.geometry("1080x650")
    modes = Frame(win)
    welcome = Frame(win)
    aoo = Frame(win)
    voo = Frame(win)
    aai = Frame(win)
    vvi = Frame(win)
    aoor = Frame(win)
    voor = Frame(win)
    aair = Frame(win)
    vvir = Frame(win)
    welcome_page(welcome)
    Modes_page(modes, welcome)
    mode.AOO_page(aoo, modes)
    mode.VOO_page(voo, modes)
    mode.AAI_page(aai, modes)
    mode.VVI_page(vvi, modes)
    mode_extend.AOOR_page(aoor, modes)
    mode_extend.VOOR_page(voor, modes)
    mode_extend.AAIR_page(aair, modes)
    mode_extend.VVIR_page(vvir, modes)
    welcome.pack(fill='both', expand=1)
    win.mainloop()


