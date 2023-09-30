from tkinter import *
import customtkinter

## Welcome Screen
# welcome = Tk()
# welcome.title("Pacemaker UI")
# welcome.geometry("500x580")
#
# label = Label(welcome, text="Welcome to Pacemaker Interface", font=('Arial', 14))
# label.pack(padx=20, pady=20)
#
# username = Entry(welcome, width=20)
# username.insert(0, "Enter Username")
# username.pack(pady=2, padx=10)
# # self.username.bind("<FocusIn>", DCM.clr_text)
#
# password = Entry(welcome, width=20)
# password.insert(0, "Enter Password")
# password.pack(pady=2, padx=10)
# # password.bind("<FocusIn>", DCM.clr_text(self, self.password))
#
# login = Button(welcome, text="Login", font=('Arial', 12))
# login.pack(padx=20, pady=10)
#
# register = Button(welcome, text="Register", font=('Arial', 12))
# register.pack(padx=20, pady=10)
#
# quit = Button(welcome, text="Quit", font=('Arial', 12))
# quit.pack(padx=20, pady=10)
#
# welcome.mainloop()

# def clr_text(self):
#     self.delete(0, "end")

## Pacing Modes
Modes = Tk()
Modes.title("Pacemaker UI")
Modes.geometry("500x580")

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

Modes.mainloop()

## A00 Pacing Mode
def AOO_page():
    AOO = Tk()
    AOO.title("Pacemaker UI")
    AOO.geometry("500x580")

    label = Label(AOO, text="AOO Page", font=('Arial', 14))
    label.pack(padx=20, pady=20)

    url_label = Label(AOO, text="Input the Upper Rate Limit", font=('Arial', 12))
    url_label.pack(padx=20, pady=2)
    url_input = customtkinter.CTkEntry(AOO, placeholder_text = "120ppm")
    url_input.pack(pady=8, padx=10)

    lrl_label = Label(AOO, text="Input the Lower Rate Limit", font=('Arial', 12))
    lrl_label.pack(padx=20, pady=2)
    lrl_input = customtkinter.CTkEntry(AOO, placeholder_text = "60ppm")
    lrl_input.pack(pady=8, padx=10)

    apw_label = Label(AOO, text="Atrial Pulse Width", font=('Arial', 12))
    apw_label.pack(padx=20, pady=2)
    apw_input = customtkinter.CTkEntry(AOO, placeholder_text = "---")
    apw_input.pack(pady=8, padx=10)

    aa_label = Label(AOO, text="Atrial Amplitude", font=('Arial', 12))
    aa_label.pack(padx=20, pady=2)
    AA_input = customtkinter.CTkEntry(AOO, placeholder_text = "---")
    AA_input.pack(pady=8, padx=10)

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
    url_input = customtkinter.CTkEntry(VOO, placeholder_text = "120ppm")
    url_input.pack(pady=8, padx=10)

    lrl_label = Label(VOO, text="Input the Lower Rate Limit", font=('Arial', 12))
    lrl_label.pack(padx=20, pady=2)
    lrl_input = customtkinter.CTkEntry(VOO, placeholder_text = "60ppm")
    lrl_input.pack(pady=8, padx=10)

    vpw_label = Label(VOO, text="Ventricular Pulse Width", font=('Arial', 12))
    vpw_label.pack(padx=20, pady=2)
    vpw_input = customtkinter.CTkEntry(VOO, placeholder_text = "---")
    vpw_input.pack(pady=8, padx=10)

    va_label = Label(VOO, text="Ventricular Amplitude", font=('Arial', 12))
    va_label.pack(padx=20, pady=2)
    va_input = customtkinter.CTkEntry(VOO, placeholder_text = "---")
    va_input.pack(pady=8, padx=10)

    VOO.mainloop()

## AAI Pacing Mode
def AAI_page():
    AAI = Tk()
    AAI.title("Pacemaker UI")
    AAI.geometry("500x750")

    label = Label(AAI, text="AAI Page", font=('Arial', 14))
    label.pack(padx=20, pady=20)

    url_label = Label(AAI, text="Input the Upper Rate Limit", font=('Arial', 12))
    url_label.pack(padx=20, pady=2)
    url_input = customtkinter.CTkEntry(AAI, placeholder_text = "120ppm")
    url_input.pack(pady=8, padx=10)

    lrl_label = Label(AAI, text="Input the Lower Rate Limit", font=('Arial', 12))
    lrl_label.pack(padx=20, pady=2)
    lrl_input = customtkinter.CTkEntry(AAI, placeholder_text = "60ppm")
    lrl_input.pack(pady=8, padx=10)

    apw_label = Label(AAI, text="Atrial Pulse Width", font=('Arial', 12))
    apw_label.pack(padx=20, pady=2)
    apw_input = customtkinter.CTkEntry(AAI, placeholder_text = "---")
    apw_input.pack(pady=8, padx=10)

    aa_label = Label(AAI, text="Atrial Amplitude", font=('Arial', 12))
    aa_label.pack(padx=20, pady=2)
    aa_input = customtkinter.CTkEntry(AAI, placeholder_text = "---")
    aa_input.pack(pady=8, padx=10)

    rs_label = Label(AAI, text="Rate Smoothing", font=('Arial', 12))
    rs_label.pack(padx=20, pady=2)
    rs_input = customtkinter.CTkEntry(AAI, placeholder_text = "---")
    rs_input.pack(pady=8, padx=10)

    hys_label = Label(AAI, text="Hysteresis", font=('Arial', 12))
    hys_label.pack(padx=20, pady=2)
    hys_input = customtkinter.CTkEntry(AAI, placeholder_text = "---")
    hys_input.pack(pady=8, padx=10)

    as_label = Label(AAI, text="Atrial Sensitivity", font=('Arial', 12))
    as_label.pack(padx=20, pady=2)
    as_input = customtkinter.CTkEntry(AAI, placeholder_text = "---")
    as_input.pack(pady=8, padx=10)

    arp_label = Label(AAI, text="ARP", font=('Arial', 12))
    arp_label.pack(padx=20, pady=2)
    arp_input = customtkinter.CTkEntry(AAI, placeholder_text = "---")
    arp_input.pack(pady=8, padx=10)

    pvarp_label = Label(AAI, text="PVARP", font=('Arial', 12))
    pvarp_label.pack(padx=20, pady=2)
    pvarp_input = customtkinter.CTkEntry(AAI, placeholder_text = "---")
    pvarp_input.pack(pady=8, padx=10)

    AAI.mainloop()

## VVI Pacing Mode
def VVI_page():
    VVI = Tk()
    VVI.title("Pacemaker UI")
    VVI.geometry("500x700")

    label = Label(VVI, text="VVI Page", font=('Arial', 14))
    label.pack(padx=20, pady=20)

    url_label = Label(VVI, text="Input the Upper Rate Limit", font=('Arial', 12))
    url_label.pack(padx=20, pady=2)
    url_input = customtkinter.CTkEntry(VVI, placeholder_text = "120ppm")
    url_input.pack(pady=8, padx=10)

    lrl_label = Label(VVI, text="Input the Lower Rate Limit", font=('Arial', 12))
    lrl_label.pack(padx=20, pady=2)
    lrl_input = customtkinter.CTkEntry(VVI, placeholder_text = "60ppm")
    lrl_input.pack(pady=8, padx=10)

    vpw_label = Label(VVI, text="Ventricular Pulse Width", font=('Arial', 12))
    vpw_label.pack(padx=20, pady=2)
    vpw_input = customtkinter.CTkEntry(VVI, placeholder_text = "---")
    vpw_input.pack(pady=8, padx=10)

    va_label = Label(VVI, text="Ventricular Amplitude", font=('Arial', 12))
    va_label.pack(padx=20, pady=2)
    va_input = customtkinter.CTkEntry(VVI, placeholder_text = "---")
    va_input.pack(pady=8, padx=10)

    rs_label = Label(VVI, text="Rate Smoothing", font=('Arial', 12))
    rs_label.pack(padx=20, pady=2)
    rs_input = customtkinter.CTkEntry(VVI, placeholder_text = "---")
    rs_input.pack(pady=8, padx=10)

    hys_label = Label(VVI, text="Hysteresis", font=('Arial', 12))
    hys_label.pack(padx=20, pady=2)
    hys_input = customtkinter.CTkEntry(VVI, placeholder_text = "---")
    hys_input.pack(pady=8, padx=10)

    as_label = Label(VVI, text="Ventricular Sensitivity ", font=('Arial', 12))
    as_label.pack(padx=20, pady=2)
    as_input = customtkinter.CTkEntry(VVI, placeholder_text = "---")
    as_input.pack(pady=8, padx=10)

    arp_label = Label(VVI, text="VRP", font=('Arial', 12))
    arp_label.pack(padx=20, pady=2)
    arp_input = customtkinter.CTkEntry(VVI, placeholder_text = "---")
    arp_input.pack(pady=8, padx=10)

    VVI.mainloop()