from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
import customtkinter

## A00 Pacing Mode

def AOO_page(AOO):
    #AOO = ThemedTk(theme="arc")
    label = Label(AOO, text="AOO Page", font=('Arial', 14))
    label.pack(padx=20, pady=20)

    url_label = Label(AOO, text="Input the Upper Rate Limit", font=('Arial', 12))
    url_label.pack()
    url_scale = Scale(AOO, length=400, from_=50, to=175, resolution=5, orient=HORIZONTAL)
    url_scale.pack(pady=10)

    global lrl_scale_aoo
    lrl_label = Label(AOO, text="Input the Lower Rate Limit", font=('Arial', 12))
    lrl_label.pack()
    lrl_scale_aoo = Scale(AOO, length=400, from_=30, to=175, resolution=1, orient=HORIZONTAL)
    lrl_scale_aoo.pack(pady=10)

    apw_label = Label(AOO, text="Atrial Pulse Width", font=('Arial', 12))
    apw_label.pack()
    apw_scale = Scale(AOO, length=400, from_=0.05, to=1.9, resolution=0.01, orient=HORIZONTAL)
    apw_scale.pack(pady=10)

    global aa_scale_aoo
    aa_label = Label(AOO, text="Atrial Amplitude", font=('Arial', 12))
    aa_label.pack()
    aa_scale_aoo = Scale(AOO, length=400, from_=0, to=5, resolution=0.1, orient=HORIZONTAL)
    aa_scale_aoo.pack(pady=10)

    AOO_save = ttk.Button(AOO, text="SAVE",width=10, command=Save_press)
    AOO_save.pack(pady=10)

    AOO_back = ttk.Button(AOO, text="BACK", width=10, command=Back_press)
    AOO_back.pack()

    aa_scale_aoo.config(command=lambda e: aa_slider_mod(aa_scale_aoo)) # Dynamically updates the slider resolution
    lrl_scale_aoo.config(command=lambda e: lrl_slider_mod(lrl_scale_aoo)) # Dynamically updates the slider resolution


## V00 Pacing Mode
def VOO_page(VOO):
    label = Label(VOO, text="VOO Page", font=('Arial', 14))
    label.pack(padx=20, pady=20)

    url_label = Label(VOO, text="Input the Upper Rate Limit", font=('Arial', 12))
    url_label.pack(padx=20, pady=2)
    url_scale = Scale(VOO, length=400, from_=50, to=175, resolution=5, orient=HORIZONTAL)
    url_scale.pack(pady=10)

    global lrl_scale_voo
    lrl_label = Label(VOO, text="Input the Lower Rate Limit", font=('Arial', 12))
    lrl_label.pack(padx=20, pady=2)
    lrl_scale_voo = Scale(VOO, length=400, from_=30, to=175, resolution=1, orient=HORIZONTAL)
    lrl_scale_voo.pack(pady=10)

    global vpw_scale_voo
    vpw_label = Label(VOO, text="Ventricular Pulse Width", font=('Arial', 12))
    vpw_label.pack(padx=20, pady=2)
    vpw_scale_voo = Scale(VOO, length=400, from_=0.05, to=1.9, resolution=0.01, orient=HORIZONTAL)
    vpw_scale_voo.pack(pady=10)

    global va_scale_voo
    va_label = Label(VOO, text="Ventricular Amplitude", font=('Arial', 12))
    va_label.pack(padx=20, pady=2)
    va_scale_voo = Scale(VOO, length=400, from_=0, to=5, resolution=0.1, orient=HORIZONTAL)
    va_scale_voo.pack(pady=10)

    VOO_save = ttk.Button(VOO, text="SAVE", width=10, command=Save_press)
    VOO_save.pack(pady=10)

    VOO_back = ttk.Button(VOO, text="BACK", width=10, command=Back_press)
    VOO_back.pack()

    vpw_scale_voo.config(command=lambda e: vpw_slider_mod(vpw_scale_voo)) # Dynamically updates the slider resolution
    va_scale_voo.config(command=lambda e: va_slider_mod(va_scale_voo)) # Dynamically updates the slider resolution
    lrl_scale_voo.config(command=lambda e: lrl_slider_mod(lrl_scale_voo)) # Dynamically updates the slider resolution


## AAI Pacing Mode

def AAI_page(AAI):

    label = Label(AAI, text="AAI Page", font=('Arial', 14))
    label.pack(padx=20, pady=5)

    url_label = Label(AAI, text="Input the Upper Rate Limit", font=('Arial', 12))
    url_label.pack(padx=20, pady=2)
    url_scale = Scale(AAI, length=400, from_=50, to=175, resolution=5, orient=HORIZONTAL)
    url_scale.pack()

    global lrl_scale_aai
    lrl_label = Label(AAI, text="Input the Lower Rate Limit", font=('Arial', 12))
    lrl_label.pack(padx=20, pady=2)
    lrl_scale_aai = Scale(AAI, length=400, from_=30, to=175, resolution=1, orient=HORIZONTAL)
    lrl_scale_aai.pack()

    apw_label = Label(AAI, text="Atrial Pulse Width", font=('Arial', 12))
    apw_label.pack(padx=20, pady=2)
    apw_scale = Scale(AAI, length=400, from_=0.05, to=1.9, resolution=0.01, orient=HORIZONTAL)
    apw_scale.pack()

    global aa_scale_aii
    aa_label = Label(AAI, text="Atrial Amplitude", font=('Arial', 12))
    aa_label.pack(padx=20, pady=2)
    aa_scale_aii = Scale(AAI, length=400, from_=0, to=5, resolution=0.1, orient=HORIZONTAL)
    aa_scale_aii.pack()

    # rs_label = Label(AAI, text="Rate Smoothing", font=('Arial', 12))
    # rs_label.pack(padx=20, pady=2)
    # rs_scale = Scale(AAI, length=400, from_=0, to=25, resolution=1, orient=HORIZONTAL)
    # rs_scale.pack()

    # hys_label = Label(AAI, text="Hysteresis", font=('Arial', 12))
    # hys_label.pack(padx=20, pady=2)
    # hys_input = Checkbutton(AAI, text='Off unchecked, Same as LRL Checked', height=2, width=50)
    # hys_input.pack()

    # as_label = Label(AAI, text="Atrial Sensitivity", font=('Arial', 12))
    # as_label.pack(padx=20, pady=2)
    # as_input = Scale(AAI, length=400, from_=0, to=10, resolution=0.05, orient=HORIZONTAL)
    # as_input.pack()

    arp_label = Label(AAI, text="Atrial Refractory Period", font=('Arial', 12))
    arp_label.pack(padx=20, pady=2)
    arp_input = Scale(AAI, length=400, from_=150, to=500, resolution=10, orient=HORIZONTAL)
    arp_input.pack()

    # pvarp_label = Label(AAI, text="PVARP", font=('Arial', 12))
    # pvarp_label.pack(padx=20, pady=2)
    # pvarp_input = Scale(AAI, length=400, from_=150, to=500, resolution=10, orient=HORIZONTAL)
    # pvarp_input.pack()

    AAI_save = ttk.Button(AAI, text="SAVE", width=10, command=Save_press)
    AAI_save.pack(pady=7)

    AAI_back = ttk.Button(AAI, text="BACK", width=10, command=Back_press)
    AAI_back.pack()

    aa_scale_aii.config(command=lambda e: aa_slider_mod(aa_scale_aii)) # Dynamically updates the slider resolution
    lrl_scale_aai.config(command=lambda e: lrl_slider_mod(lrl_scale_aai)) # Dynamically updates the slider resolution


## VVI Pacing Mode

def VVI_page(VVI):

    label = Label(VVI, text="VVI Page", font=('Arial', 14))
    label.pack(padx=20, pady=5)

    url_label = Label(VVI, text="Input the Upper Rate Limit", font=('Arial', 12))
    url_label.pack(padx=20, pady=2)
    url_scale = Scale(VVI, length=400, from_=50, to=175, resolution=5, orient=HORIZONTAL)
    url_scale.pack()

    global lrl_scale_vvi
    lrl_label = Label(VVI, text="Input the Lower Rate Limit", font=('Arial', 12))
    lrl_label.pack(padx=20, pady=2)
    lrl_scale_vvi = Scale(VVI, length=400, from_=30, to=175, resolution=1, orient=HORIZONTAL)
    lrl_scale_vvi.pack()

    global vpw_scale_vvi
    vpw_label = Label(VVI, text="Ventricular Pulse Width", font=('Arial', 12))
    vpw_label.pack(padx=20, pady=2)
    vpw_scale_vvi = Scale(VVI, length=400, from_=0.05, to=1.9, resolution=0.01, orient=HORIZONTAL)
    vpw_scale_vvi.pack()

    global va_scale_vvi
    va_label = Label(VVI, text="Ventricular Amplitude", font=('Arial', 12))
    va_label.pack(padx=20, pady=2)
    va_scale_vvi = Scale(VVI, length=400, from_=0, to=5, resolution=0.1, orient=HORIZONTAL)
    va_scale_vvi.pack()

    # rs_label = Label(VVI, text="Rate Smoothing", font=('Arial', 12))
    # rs_label.pack(padx=20, pady=2)
    # rs_scale = Scale(VVI, length=400, from_=0, to=25, resolution=1, orient=HORIZONTAL)
    # rs_scale.pack()

    # hys_label = Label(VVI, text="Hysteresis", font=('Arial', 12))
    # hys_label.pack(padx=20, pady=2)
    # hys_input = Checkbutton(VVI, text='Off unchecked, Same as LRL Checked', height=2, width=50)
    # hys_input.pack()

    # vs_label = Label(VVI, text="Ventricular Sensitivity ", font=('Arial', 12))
    # vs_label.pack(padx=20, pady=2)
    # vs_input = Scale(VVI, length=400, from_=0, to=10, resolution=0.05, orient=HORIZONTAL)
    # vs_input.pack()

    vrp_label = Label(VVI, text="VRP", font=('Arial', 12))
    vrp_label.pack(padx=20, pady=2)
    vrp_input = Scale(VVI, length=400, from_=150, to=500, resolution=10, orient=HORIZONTAL)
    vrp_input.pack()

    VVI_save = ttk.Button(VVI, text="SAVE", width=10, command=Save_press)
    VVI_save.pack()

    VVI_back = ttk.Button(VVI, text="BACK", width=10, command=Back_press)
    VVI_back.pack()

    vpw_scale_vvi.config(command=lambda e: vpw_slider_mod(vpw_scale_vvi)) # Dynamically updates the slider resolution
    va_scale_vvi.config(command=lambda e: va_slider_mod(va_scale_vvi)) # Dynamically updates the slider resolution
    lrl_scale_vvi.config(command=lambda e: lrl_slider_mod(lrl_scale_vvi)) # Dynamically updates the slider resolution

def Save_press():
    print("Save Pressed")
    return True

def Back_press():
    print("Back Pressed")
    return True

def lrl_slider_mod(scale):
    current = float(scale.get())
    if current < 50 or current > 90:
        scale.config(resolution=(5))
    else:
        scale.config(resolution=(1))

def va_slider_mod(scale):
    current = float(scale.get())
    if current < 0.5 or current > 2.5:
        scale.config(resolution=(0.5))
    else:
        scale.config(resolution=(0.1))

def aa_slider_mod(scale):
    current = float(scale.get())
    if current < 0.5 or current > 2.5:
        scale.config(resolution=(0.5))
    else:
        scale.config(resolution=(0.1))

def vpw_slider_mod(scale):
    current = float(scale.get())
    if current < 1/10:
        scale.config(length=400, from_=0.05, to=1.9, resolution=(0.05))
        print(current)
    else:
        scale.config(length=400, from_=0.05, to=1.9, resolution=(0.1))
        print(current)
