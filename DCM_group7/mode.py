from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
import customtkinter

## A00 Pacing Mode

def AOO_page(AOO):
    #AOO = ThemedTk(theme="arc")
    label = Label(AOO, text="AOO Page", font=('Arial', 14))
    label.grid(row=0, column=1)

    url_label = Label(AOO, text="Input the Upper Rate Limit [ppm]", font=('Arial', 12))
    url_label.grid(row=1, column=1)
    url_scale = Scale(AOO, length=400, from_=50, to=175, resolution=5, orient=HORIZONTAL)
    url_scale.grid(row=2, column=1)

    global lrl_scale_aoo
    lrl_label = Label(AOO, text="Input the Lower Rate Limit [ppm]", font=('Arial', 12))
    lrl_label.grid(row=3, column=1)
    lrl_scale_aoo = Scale(AOO, length=400, from_=30, to=175, resolution=1, orient=HORIZONTAL)
    lrl_scale_aoo.grid(row=4, column=1)

    global aa_scale_aoo
    aa_label = Label(AOO, text="Atrial Amplitude [V]", font=('Arial', 12))
    aa_label.grid(row=5, column=1)
    aa_scale_aoo = Scale(AOO, length=400, from_=0, to=5, resolution=0.1, orient=HORIZONTAL)
    aa_scale_aoo.grid(row=6, column=1)

    global current_index_aoo
    current_index_aoo = 0  # Initialize the index to 0

    apw_label = Label(AOO, text="Atrial Pulse Width [ms]", font=('Arial', 12))
    apw_label.grid(row=7, column=1)
    global value_label_aoo
    value_label_aoo = Label(AOO, text=str(scale_incs[current_index_aoo]))
    value_label_aoo.grid(row=8, column=1)

    # Create a increment/decrement button
    decrement_button = Button(AOO, text="<", command=lambda: update_value_aoo(False))
    decrement_button.grid(row=8, column=0)
    increment_button = Button(AOO, text=">", command=lambda: update_value_aoo(True))
    increment_button.grid(row=8, column=2)

    AOO_save = ttk.Button(AOO, text="SAVE",width=10, command=Save_press)
    AOO_save.grid(row=9, column=1)

    AOO_back = ttk.Button(AOO, text="BACK", width=10, command=Back_press)
    AOO_back.grid(row=10, column=1)

    aa_scale_aoo.config(command=lambda e: aa_slider_mod(aa_scale_aoo)) # Dynamically updates the slider resolution
    lrl_scale_aoo.config(command=lambda e: lrl_slider_mod(lrl_scale_aoo)) # Dynamically updates the slider resolution


## V00 Pacing Mode
def VOO_page(VOO):
    label = Label(VOO, text="VOO Page", font=('Arial', 14))
    label.grid(row=0, column=1)

    url_label = Label(VOO, text="Input the Upper Rate Limit [ppm]", font=('Arial', 12))
    url_label.grid(row=2, column=1)
    url_scale = Scale(VOO, length=400, from_=50, to=175, resolution=5, orient=HORIZONTAL)
    url_scale.grid(row=3, column=1)

    global lrl_scale_voo
    lrl_label = Label(VOO, text="Input the Lower Rate Limit [ppm]", font=('Arial', 12))
    lrl_label.grid(row=6, column=1)
    lrl_scale_voo = Scale(VOO, length=400, from_=30, to=175, resolution=1, orient=HORIZONTAL)
    lrl_scale_voo.grid(row=7, column=1)

    global va_scale_voo
    va_label = Label(VOO, text="Ventricular Amplitude [V]", font=('Arial', 12))
    va_label.grid(row=10, column=1)
    va_scale_voo = Scale(VOO, length=400, from_=0, to=5, resolution=0.1, orient=HORIZONTAL)
    va_scale_voo.grid(row=11, column=1)

    global current_index_voo
    current_index_voo = 0  # Initialize the index to 0

    vpw_label = Label(VOO, text="Ventricular Pulse Width [ms]", font=('Arial', 12))
    vpw_label.grid(row=14, column=1)
    global value_label_voo
    value_label_voo = Label(VOO, text=str(scale_incs[current_index_voo]))
    value_label_voo.grid(row=15, column=1)

    # Create a increment/decrement button
    decrement_button = Button(VOO, text="<", command=lambda: update_value_voo(False))
    decrement_button.grid(row=15, column=0)
    increment_button = Button(VOO, text=">", command=lambda: update_value_voo(True))
    increment_button.grid(row=15, column=2)

    VOO_save = ttk.Button(VOO, text="SAVE", width=10, command=Save_press)
    VOO_save.grid(row=18, column=1)
    VOO_back = ttk.Button(VOO, text="BACK", width=10, command=Back_press)
    VOO_back.grid(row=25, column=1)

    va_scale_voo.config(command=lambda e: va_slider_mod(va_scale_voo)) # Dynamically updates the slider resolution
    lrl_scale_voo.config(command=lambda e: lrl_slider_mod(lrl_scale_voo)) # Dynamically updates the slider resolution

## AAI Pacing Mode
def AAI_page(AAI):

    label = Label(AAI, text="AAI Page", font=('Arial', 14))
    label.grid(row=0, column=1)

    url_label = Label(AAI, text="Input the Upper Rate Limit [ppm]", font=('Arial', 12))
    url_label.grid(row=1, column=1)
    url_scale = Scale(AAI, length=400, from_=50, to=175, resolution=5, orient=HORIZONTAL)
    url_scale.grid(row=2, column=1)

    global lrl_scale_aai
    lrl_label = Label(AAI, text="Input the Lower Rate Limit [ppm]", font=('Arial', 12))
    lrl_label.grid(row=3, column=1)
    lrl_scale_aai = Scale(AAI, length=400, from_=30, to=175, resolution=1, orient=HORIZONTAL)
    lrl_scale_aai.grid(row=4, column=1)

    global aa_scale_aii
    aa_label = Label(AAI, text="Atrial Amplitude [V]", font=('Arial', 12))
    aa_label.grid(row=7, column=1)
    aa_scale_aii = Scale(AAI, length=400, from_=0, to=5, resolution=0.1, orient=HORIZONTAL)
    aa_scale_aii.grid(row=8, column=1)

    arp_label = Label(AAI, text="Atrial Refractory Period [ms]", font=('Arial', 12))
    arp_label.grid(row=9, column=1)
    arp_input = Scale(AAI, length=400, from_=150, to=500, resolution=10, orient=HORIZONTAL)
    arp_input.grid(row=10, column=1)

    global current_index_aai
    current_index_aai = 0  # Initialize the index to 0

    apw_label = Label(AAI, text="Atrial Pulse Width [ms]", font=('Arial', 12))
    apw_label.grid(row=11, column=1)
    global value_label_aai
    value_label_aai = Label(AAI, text=str(scale_incs[current_index_aai]))
    value_label_aai.grid(row=12, column=1)

    # Create a increment/decrement button
    decrement_button = Button(AAI, text="<", command=lambda: update_value_aai(False))
    decrement_button.grid(row=12, column=0)
    increment_button = Button(AAI, text=">", command=lambda: update_value_aai(True))
    increment_button.grid(row=12, column=2)

    AAI_save = ttk.Button(AAI, text="SAVE", width=10, command=Save_press)
    AAI_save.grid(row=13, column=1)

    AAI_back = ttk.Button(AAI, text="BACK", width=10, command=Back_press)
    AAI_back.grid(row=14, column=1)

    aa_scale_aii.config(command=lambda e: aa_slider_mod(aa_scale_aii)) # Dynamically updates the slider resolution
    lrl_scale_aai.config(command=lambda e: lrl_slider_mod(lrl_scale_aai)) # Dynamically updates the slider resolution


## VVI Pacing Mode
def VVI_page(VVI):

    label = Label(VVI, text="VVI Page", font=('Arial', 14))
    label.grid(row=0, column=1)

    url_label = Label(VVI, text="Input the Upper Rate Limit [ppm]", font=('Arial', 12))
    url_label.grid(row=1, column=1)
    url_scale = Scale(VVI, length=400, from_=50, to=175, resolution=5, orient=HORIZONTAL)
    url_scale.grid(row=2, column=1)

    global lrl_scale_vvi
    lrl_label = Label(VVI, text="Input the Lower Rate Limit [ppm]", font=('Arial', 12))
    lrl_label.grid(row=3, column=1)
    lrl_scale_vvi = Scale(VVI, length=400, from_=30, to=175, resolution=1, orient=HORIZONTAL)
    lrl_scale_vvi.grid(row=4, column=1)

    global va_scale_vvi
    va_label = Label(VVI, text="Ventricular Amplitude [V]", font=('Arial', 12))
    va_label.grid(row=5, column=1)
    va_scale_vvi = Scale(VVI, length=400, from_=0, to=5, resolution=0.1, orient=HORIZONTAL)
    va_scale_vvi.grid(row=6, column=1)

    vrp_label = Label(VVI, text="Ventrical Refractory Period [ms]", font=('Arial', 12))
    vrp_label.grid(row=7, column=1)
    vrp_input = Scale(VVI, length=400, from_=150, to=500, resolution=10, orient=HORIZONTAL)
    vrp_input.grid(row=8, column=1)

    global current_index_vvi
    current_index_vvi = 0  # Initialize the index to 0

    vpw_label = Label(VVI, text="Ventricular Pulse Width [ms]", font=('Arial', 12))
    vpw_label.grid(row=9, column=1)
    global value_label_vvi
    value_label_vvi = Label(VVI, text=str(scale_incs[current_index_vvi]))
    value_label_vvi.grid(row=10, column=1)

    # Create a increment/decrement button
    decrement_button = Button(VVI, text="<", command=lambda: update_value_vvi(False))
    decrement_button.grid(row=10, column=0)
    increment_button = Button(VVI, text=">", command=lambda: update_value_vvi(True))
    increment_button.grid(row=10, column=2)

    VVI_save = ttk.Button(VVI, text="SAVE", width=10, command=Save_press)
    VVI_save.grid(row=11, column=1)

    VVI_back = ttk.Button(VVI, text="BACK", width=10, command=Back_press)
    VVI_back.grid(row=12, column=1)

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

global scale_incs
scale_incs = [0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9]

def update_value_voo(increment):
    global current_index_voo
    if increment:
        current_index_voo = (current_index_voo + 1) % len(scale_incs)
    else:
        current_index_voo = (current_index_voo - 1) % len(scale_incs)
    value_label_voo.config(text=str(scale_incs[current_index_voo]))

def update_value_vvi(increment):
    global current_index_vvi
    if increment:
        current_index_vvi = (current_index_vvi + 1) % len(scale_incs)
    else:
        current_index_vvi = (current_index_vvi - 1) % len(scale_incs)
    value_label_vvi.config(text=str(scale_incs[current_index_vvi]))

def update_value_aoo(increment):
    global current_index_aoo
    if increment:
        current_index_aoo = (current_index_aoo + 1) % len(scale_incs)
    else:
        current_index_aoo = (current_index_aoo - 1) % len(scale_incs)
    value_label_aoo.config(text=str(scale_incs[current_index_aoo]))

def update_value_aai(increment):
    global current_index_aai
    if increment:
        current_index_aai = (current_index_aai + 1) % len(scale_incs)
    else:
        current_index_aai = (current_index_aai - 1) % len(scale_incs)
    value_label_aai.config(text=str(scale_incs[current_index_aai]))
