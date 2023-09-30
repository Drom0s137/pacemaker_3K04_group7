from tkinter import *
import customtkinter
import backend
import sys

# global login
#
# def temp_text(e, i):
#     i.delete(0, "end")
#
# def obtain_logins(ui_username, ui_pswrd):
#     username = ui_username.get()
#     password = ui_pswrd.get()
#     if backend.log_in(username, password):
#         login = True
#     else:
#         login = False
#
# def register_user(ui_username, ui_pswrd):
#     username = ui_username.get()
#     password = ui_pswrd.get()
#     if backend.register(username, password):
#         login = 1
#     else:
#         login = 0
#
#
# def test():
#     print("Asfdfds")
#
# def main():
#     welcome = Tk()
#     welcome.title("Pacemaker UI")
#     welcome.geometry("500x580")
#
#     label = Label(welcome, text="Welcome to Pacemaker Interface", font=('Arial', 14))
#     label.pack(padx=20, pady=20)
#
#     #username section
#     ui_username = Entry(welcome, bg = "white", width=20)
#     ui_username.insert(0, "Enter Username")
#     ui_username.pack(pady=2, padx=10)
#     def handler(event, i=ui_username):
#         return temp_text(event, i)
#     ui_username.bind("<FocusIn>", handler)
#
#     #password section
#     ui_pswrd = Entry(welcome, width=20)
#     ui_pswrd.insert(0, "Enter Password")
#     ui_pswrd.pack(pady=2, padx=10)
#     def handler(event, i=ui_pswrd):
#         return temp_text(event, i)
#     ui_pswrd.bind("<FocusIn>", handler)
#
#     login = Button(welcome, command = lambda: obtain_logins(ui_username, ui_pswrd), text="Login", font=('Arial', 12))
#     login.pack(padx=20, pady=10)
#
#     register = Button(welcome, command = lambda: register_user(ui_username, ui_pswrd), text="Register", font=('Arial', 12))
#     register.pack(padx=20, pady=10)
#
#     quit = Button(welcome, command = backend.exit_system, text="Quit", font=('Arial', 12))
#     quit.pack(padx=20, pady=10)
#
#     welcome.mainloop()
#
#     Modes = Tk()
#     Modes.title("Pacemaker UI")
#     Modes.geometry("500x580")
#
#     label = Label(Modes, text="Select the Pacing Mode", font=('Arial', 14))
#     label.pack(padx=20, pady=20)
#
#     AOO_btn = Button(Modes, text="AOO", font=('Arial', 12))
#     AOO_btn.pack(padx=20, pady=10)
#
#     VOO_btn = Button(Modes, text="VOO", font=('Arial', 12))
#     VOO_btn.pack(padx=20, pady=10)
#
#     AAI_btn = Button(Modes, text="AAI", font=('Arial', 12))
#     AAI_btn.pack(padx=20, pady=10)
#
#     VVI_btn = Button(Modes, text="VVI", font=('Arial', 12))
#     VVI_btn.pack(padx=20, pady=10)
#
#     Modes.mainloop()

## A00 Pacing Mode
def AOO_page():
    AOO = Tk()
    AOO.title("Pacemaker UI")
    AOO.geometry("500x580")

    label = Label(AOO, text="AOO Page", font=('Arial', 14))
    label.pack(padx=20, pady=20)

    url_label = Label(AOO, text="Input the Upper Rate Limit", font=('Arial', 12))
    url_label.pack()
    url_scale = Scale(AOO, length=400, from_=50, to=175, resolution=5, orient=HORIZONTAL)
    url_scale.pack(pady=10)

    lrl_label = Label(AOO, text="Input the Lower Rate Limit", font=('Arial', 12))
    lrl_label.pack()
    lrl_scale = Scale(AOO, length=400, from_=30, to=175, resolution=1, orient=HORIZONTAL)
    lrl_scale.pack(pady=10)

    apw_label = Label(AOO, text="Atrial Pulse Width", font=('Arial', 12))
    apw_label.pack()
    apw_scale = Scale(AOO, length=400, from_=0.05, to=1.9, resolution=0.01, orient=HORIZONTAL)
    apw_scale.pack(pady=10)

    aa_label = Label(AOO, text="Atrial Amplitude", font=('Arial', 12))
    aa_label.pack()
    aa_scale = Scale(AOO, length=400, from_=0, to=7, resolution=0.1, orient=HORIZONTAL)
    aa_scale.pack(pady=10)

    AOO_save = Button(AOO, text="SAVE", height=1, width=10, command=Save_press)
    AOO_save.pack(pady=10)

    AOO_back = Button(AOO, text="BACK", height=1, width=10, command=Back_press)
    AOO_back.pack()

    AOO.mainloop()

## V00 Pacing Mode
def VOO_page():
    VOO = Tk()
    VOO.title("Pacemaker UI")
    VOO.geometry("500x580")

    label = Label(VOO, text="VOO Page", font=('Arial', 14))
    label.pack(padx=20, pady=20)

    url_label = Label(VOO, text="Input the Upper Rate Limit", font=('Arial', 12))
    url_label.pack(padx=20, pady=2)
    url_scale = Scale(VOO, length=400, from_=50, to=175, resolution=5, orient=HORIZONTAL)
    url_scale.pack(pady=10)

    lrl_label = Label(VOO, text="Input the Lower Rate Limit", font=('Arial', 12))
    lrl_label.pack(padx=20, pady=2)
    lrl_scale = Scale(VOO, length=400, from_=30, to=175, resolution=1, orient=HORIZONTAL)
    lrl_scale.pack(pady=10)

    vpw_label = Label(VOO, text="Ventricular Pulse Width", font=('Arial', 12))
    vpw_label.pack(padx=20, pady=2)
    vpw_scale = Scale(VOO, length=400, from_=0.05, to=1.9, resolution=0.01, orient=HORIZONTAL)
    vpw_scale.pack(pady=10)

    va_label = Label(VOO, text="Ventricular Amplitude", font=('Arial', 12))
    va_label.pack(padx=20, pady=2)
    va_scale = Scale(VOO, length=400, from_=0, to=7, resolution=0.1, orient=HORIZONTAL)
    va_scale.pack(pady=10)

    VOO_save = Button(VOO, text="SAVE", height=1, width=10, command=Save_press)
    VOO_save.pack(pady=10)

    VOO_back = Button(VOO, text="BACK", height=1, width=10, command=Back_press)
    VOO_back.pack()

    VOO.mainloop()

## AAI Pacing Mode
def AAI_page():
    AAI = Tk()
    AAI.title("Pacemaker UI")
    AAI.geometry("500x780")

    label = Label(AAI, text="AAI Page", font=('Arial', 14))
    label.pack(padx=20, pady=5)

    url_label = Label(AAI, text="Input the Upper Rate Limit", font=('Arial', 12))
    url_label.pack(padx=20, pady=2)
    url_scale = Scale(AAI, length=400, from_=50, to=175, resolution=5, orient=HORIZONTAL)
    url_scale.pack()

    lrl_label = Label(AAI, text="Input the Lower Rate Limit", font=('Arial', 12))
    lrl_label.pack(padx=20, pady=2)
    lrl_scale = Scale(AAI, length=400, from_=30, to=175, resolution=1, orient=HORIZONTAL)
    lrl_scale.pack()

    apw_label = Label(AAI, text="Atrial Pulse Width", font=('Arial', 12))
    apw_label.pack(padx=20, pady=2)
    apw_scale = Scale(AAI, length=400, from_=0.05, to=1.9, resolution=0.01, orient=HORIZONTAL)
    apw_scale.pack()

    aa_label = Label(AAI, text="Atrial Amplitude", font=('Arial', 12))
    aa_label.pack(padx=20, pady=2)
    aa_scale = Scale(AAI, length=400, from_=0, to=7, resolution=0.1, orient=HORIZONTAL)
    aa_scale.pack()

    rs_label = Label(AAI, text="Rate Smoothing", font=('Arial', 12))
    rs_label.pack(padx=20, pady=2)
    rs_scale = Scale(AAI, length=400, from_=0, to=25, resolution=1, orient=HORIZONTAL)
    rs_scale.pack()

    hys_label = Label(AAI, text="Hysteresis", font=('Arial', 12))
    hys_label.pack(padx=20, pady=2)
    hys_input = Checkbutton(AAI, text='Off unchecked, Same as LRL Checked', height=2, width=50)
    hys_input.pack()

    as_label = Label(AAI, text="Atrial Sensitivity", font=('Arial', 12))
    as_label.pack(padx=20, pady=2)
    as_input = Scale(AAI, length=400, from_=0, to=10, resolution=0.05, orient=HORIZONTAL)
    as_input.pack()

    arp_label = Label(AAI, text="Atrial Refractory Period", font=('Arial', 12))
    arp_label.pack(padx=20, pady=2)
    arp_input = Scale(AAI, length=400, from_=150, to=500, resolution=10, orient=HORIZONTAL)
    arp_input.pack()

    pvarp_label = Label(AAI, text="PVARP", font=('Arial', 12))
    pvarp_label.pack(padx=20, pady=2)
    pvarp_input = Scale(AAI, length=400, from_=150, to=500, resolution=10, orient=HORIZONTAL)
    pvarp_input.pack()

    AAI_save = Button(AAI, text="SAVE", height=1, width=10, command=Save_press)
    AAI_save.pack(pady=7)

    AAI_back = Button(AAI, text="BACK", height=1, width=10, command=Back_press)
    AAI_back.pack()

    AAI.mainloop()

## VVI Pacing Mode
def VVI_page():
    VVI = Tk()
    VVI.title("Pacemaker UI")
    VVI.geometry("500x780")

    label = Label(VVI, text="VVI Page", font=('Arial', 14))
    label.pack(padx=20, pady=5)

    url_label = Label(VVI, text="Input the Upper Rate Limit", font=('Arial', 12))
    url_label.pack(padx=20, pady=2)
    url_scale = Scale(VVI, length=400, from_=50, to=175, resolution=5, orient=HORIZONTAL)
    url_scale.pack()

    lrl_label = Label(VVI, text="Input the Lower Rate Limit", font=('Arial', 12))
    lrl_label.pack(padx=20, pady=2)
    lrl_scale = Scale(VVI, length=400, from_=30, to=175, resolution=1, orient=HORIZONTAL)
    lrl_scale.pack()

    vpw_label = Label(VVI, text="Ventricular Pulse Width", font=('Arial', 12))
    vpw_label.pack(padx=20, pady=2)
    vpw_scale = Scale(VVI, length=400, from_=0.05, to=1.9, resolution=0.01, orient=HORIZONTAL)
    vpw_scale.pack()

    va_label = Label(VVI, text="Ventricular Amplitude", font=('Arial', 12))
    va_label.pack(padx=20, pady=2)
    va_scale = Scale(VVI, length=400, from_=0, to=7, resolution=0.1, orient=HORIZONTAL)
    va_scale.pack()

    rs_label = Label(VVI, text="Rate Smoothing", font=('Arial', 12))
    rs_label.pack(padx=20, pady=2)
    rs_scale = Scale(VVI, length=400, from_=0, to=25, resolution=1, orient=HORIZONTAL)
    rs_scale.pack()

    hys_label = Label(VVI, text="Hysteresis", font=('Arial', 12))
    hys_label.pack(padx=20, pady=2)
    hys_input = Checkbutton(VVI, text='Off unchecked, Same as LRL Checked', height=2, width=50)
    hys_input.pack()

    vs_label = Label(VVI, text="Ventricular Sensitivity ", font=('Arial', 12))
    vs_label.pack(padx=20, pady=2)
    vs_input = Scale(VVI, length=400, from_=0, to=10, resolution=0.05, orient=HORIZONTAL)
    vs_input.pack()

    vrp_label = Label(VVI, text="VRP", font=('Arial', 12))
    vrp_label.pack(padx=20, pady=2)
    vrp_input = Scale(VVI, length=400, from_=150, to=500, resolution=10, orient=HORIZONTAL)
    vrp_input.pack()

    VVI_save = Button(VVI, text="SAVE", height=1, width=10, command=Save_press)
    VVI_save.pack()

    VVI_back = Button(VVI, text="BACK", height=1, width=10, command=Back_press)
    VVI_back.pack()

    VVI.mainloop()

# if __name__ == "__main__":
#     main()

def Save_press():
    print("Save Pressed")
    return True

def Back_press():
    print("Back Pressed")
    return True

# Calling the AOO for testing Slider
AOO_page()
VOO_page()
VVI_page()
AAI_page()