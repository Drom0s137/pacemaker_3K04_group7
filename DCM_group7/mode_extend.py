from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
import ui
import backend
import mode

def AOOR_page(AOOR, modes):
    label = Label(AOOR, text="AOOR Page", font=('Arial', 14))
    label.grid(row=0, column=1)

    url = StringVar()
    url_label = Label(AOOR, text="Input the Upper Rate Limit [ppm]", font=('Arial', 12))
    url_label.grid(row=1, column=1)
    url_scale = Scale(AOOR, variable=url, length=400, from_=50, to=175, resolution=5, orient=HORIZONTAL)
    url_scale.grid(row=2, column=1)
    url_scale.set(120)

    global lrl_scale_aoor
    lrl = StringVar()
    lrl_label = Label(AOOR, text="Input the Lower Rate Limit [ppm]", font=('Arial', 12))
    lrl_label.grid(row=3, column=1)
    lrl_scale_aoor = Scale(AOOR, variable=lrl, length=400, from_=30, to=175, resolution=1, orient=HORIZONTAL)
    lrl_scale_aoor.grid(row=4, column=1)
    lrl_scale_aoor.set(60)

    global aa_scale_aoor
    aa = StringVar()
    aa_label = Label(AOOR, text="Atrial Amplitude [V]", font=('Arial', 12))
    aa_label.grid(row=5, column=1)
    aa_scale_aoor = Scale(AOOR, variable=aa, length=400, from_=0, to=5, resolution=0.1, orient=HORIZONTAL)
    aa_scale_aoor.grid(row=6, column=1)
    aa_scale_aoor.set(3.5)

    global current_index_aoor
    current_index_aoor = 4  # Initialize the index to 0

    apw_label = Label(AOOR, text="Atrial Pulse Width [ms]", font=('Arial', 12))
    apw_label.grid(row=7, column=1)
    global value_label_aoor
    value_label_aoor = Label(AOOR, text=str(mode.scale_incs[current_index_aoor]))
    value_label_aoor.grid(row=8, column=1)

    # Create a increment/decrement button
    decrement_button = Button(AOOR, text="<", command=lambda: update_value_aoor(False))
    decrement_button.grid(row=8, column=0)
    increment_button = Button(AOOR, text=">", command=lambda: update_value_aoor(True))
    increment_button.grid(row=8, column=2)

    AOO_save = ttk.Button(AOOR, text="SAVE", width=10,
                          command=lambda: mode.Save_press(url.get(), lrl.get(), APW=mode.scale_incs[current_index_aoor],
                                                     AA=aa.get(), frame=AOOR))
    AOO_save.grid(row=9, column=1)

    AOO_back = ttk.Button(AOOR, text="BACK", width=10, command=lambda: mode.Back_press(modes, AOOR))
    AOO_back.grid(row=10, column=1)

    aa_scale_aoor.config(command=lambda e: mode.aa_slider_mod(aa_scale_aoor))  # Dynamically updates the slider resolution
    lrl_scale_aoor.config(command=lambda e: mode.lrl_slider_mod(lrl_scale_aoor))  # Dynamically updates the slider resolution

def VOOR_page(VOOR, modes):
    label = Label(VOOR, text="VOOR Page", font=('Arial', 14))
    label.grid(row=0, column=1)

    label = Label(VOOR, text="VOOR Page", font=('Arial', 14))
    label.grid(row=0, column=1)

    url = StringVar()
    url_label = Label(VOOR, text="Input the Upper Rate Limit [ppm]", font=('Arial', 12))
    url_label.grid(row=2, column=1)
    url_scale = Scale(VOOR, variable=url, length=400, from_=50, to=175, resolution=5, orient=HORIZONTAL)
    url_scale.grid(row=3, column=1)
    url_scale.set(120)

    global lrl_scale_voo
    lrl = StringVar()
    lrl_label = Label(VOOR, text="Input the Lower Rate Limit [ppm]", font=('Arial', 12))
    lrl_label.grid(row=6, column=1)
    lrl_scale_voo = Scale(VOOR, variable=lrl, length=400, from_=30, to=175, resolution=1, orient=HORIZONTAL)
    lrl_scale_voo.grid(row=7, column=1)
    lrl_scale_voo.set(60)

    global va_scale_voo
    va = StringVar()
    va_label = Label(VOOR, text="Ventricular Amplitude [V]", font=('Arial', 12))
    va_label.grid(row=10, column=1)
    va_scale_voo = Scale(VOOR, variable=va, length=400, from_=0, to=5, resolution=0.1, orient=HORIZONTAL)
    va_scale_voo.grid(row=11, column=1)
    va_scale_voo.set(3.5)

    global current_index_voor
    current_index_voor = 4  # Initialize the index to 0

    vpw_label = Label(VOOR, text="Ventricular Pulse Width [ms]", font=('Arial', 12))
    vpw_label.grid(row=14, column=1)
    global value_label_voor
    value_label_voor = Label(VOOR, text=str(mode.scale_incs[current_index_voor]))
    value_label_voor.grid(row=15, column=1)

    # Create a increment/decrement button
    decrement_button = Button(VOOR, text="<", command=lambda: update_value_voor(False))
    decrement_button.grid(row=15, column=0)
    increment_button = Button(VOOR, text=">", command=lambda: update_value_voor(True))
    increment_button.grid(row=15, column=2)

    VOO_save = ttk.Button(VOOR, text="SAVE", width=10,
                          command=lambda: mode.Save_press(url.get(), lrl.get(), VPW=mode.scale_incs[current_index_voor],
                                                     VA=va.get(), frame=VOOR))
    VOO_save.grid(row=18, column=1)
    VOO_back = ttk.Button(VOOR, text="BACK", width=10, command=lambda: mode.Back_press(modes, VOOR))
    VOO_back.grid(row=25, column=1)

    va_scale_voo.config(command=lambda e: mode.va_slider_mod(va_scale_voo))  # Dynamically updates the slider resolution
    lrl_scale_voo.config(command=lambda e: mode.lrl_slider_mod(lrl_scale_voo))  # Dynamically updates the slider resolution

def AAIR_page(AAIR, modes):
    label = Label(AAIR, text="AAIR Page", font=('Arial', 14))
    label.grid(row=0, column=1)

    url = StringVar()
    url_label = Label(AAIR, text="Input the Upper Rate Limit [ppm]", font=('Arial', 12))
    url_label.grid(row=1, column=1)
    url_scale = Scale(AAIR, variable=url, length=400, from_=50, to=175, resolution=5, orient=HORIZONTAL)
    url_scale.grid(row=2, column=1)
    url_scale.set(120)

    global lrl_scale_aai
    lrl = StringVar()
    lrl_label = Label(AAIR, text="Input the Lower Rate Limit [ppm]", font=('Arial', 12))
    lrl_label.grid(row=3, column=1)
    lrl_scale_aai = Scale(AAIR, variable=lrl, length=400, from_=30, to=175, resolution=1, orient=HORIZONTAL)
    lrl_scale_aai.grid(row=4, column=1)
    lrl_scale_aai.set(60)

    global aa_scale_aii
    aa = StringVar()
    aa_label = Label(AAIR, text="Atrial Amplitude [V]", font=('Arial', 12))
    aa_label.grid(row=7, column=1)
    aa_scale_aii = Scale(AAIR, variable=aa, length=400, from_=0, to=5, resolution=0.1, orient=HORIZONTAL)
    aa_scale_aii.grid(row=8, column=1)
    aa_scale_aii.set(3.5)

    arp = StringVar()
    arp_label = Label(AAIR, text="Atrial Refractory Period [ms]", font=('Arial', 12))
    arp_label.grid(row=9, column=1)
    arp_input = Scale(AAIR, variable=arp, length=400, from_=150, to=500, resolution=10, orient=HORIZONTAL)
    arp_input.grid(row=10, column=1)
    arp_input.set(250)

    global current_index_aair
    current_index_aair = 4  # Initialize the index to 0

    apw_label = Label(AAIR, text="Atrial Pulse Width [ms]", font=('Arial', 12))
    apw_label.grid(row=11, column=1)
    global value_label_aair
    value_label_aair = Label(AAIR, text=str(mode.scale_incs[current_index_aair]))
    value_label_aair.grid(row=12, column=1)

    # Create a increment/decrement button
    decrement_button = Button(AAIR, text="<", command=lambda: update_value_aair(False))
    decrement_button.grid(row=12, column=0)
    increment_button = Button(AAIR, text=">", command=lambda: update_value_aair(True))
    increment_button.grid(row=12, column=2)

    AAI_save = ttk.Button(AAIR, text="SAVE", width=10,
                          command=lambda: mode.Save_press(url.get(), lrl.get(), APW=mode.scale_incs[current_index_aair],
                                                     AA=aa.get(), ARP=arp.get(), frame=AAIR))
    AAI_save.grid(row=13, column=1)

    AAI_back = ttk.Button(AAIR, text="BACK", width=10, command=lambda: mode.Back_press(modes, AAIR))
    AAI_back.grid(row=14, column=1)

    aa_scale_aii.config(command=lambda e: mode.aa_slider_mod(aa_scale_aii))  # Dynamically updates the slider resolution
    lrl_scale_aai.config(command=lambda e: mode.lrl_slider_mod(lrl_scale_aai))  # Dynamically updates the slider resolution


def VVIR_page(VVIR, modes):
    label = Label(VVIR, text="VVIR Page", font=('Arial', 14))
    label.grid(row=0, column=1)

    url = StringVar()
    url_label = Label(VVIR, text="Input the Upper Rate Limit [ppm]", font=('Arial', 12))
    url_label.grid(row=1, column=1)
    url_scale = Scale(VVIR, variable=url, length=400, from_=50, to=175, resolution=5, orient=HORIZONTAL)
    url_scale.grid(row=2, column=1)
    url_scale.set(120)

    global lrl_scale_vvi
    lrl = StringVar()
    lrl_label = Label(VVIR, text="Input the Lower Rate Limit [ppm]", font=('Arial', 12))
    lrl_label.grid(row=3, column=1)
    lrl_scale_vvi = Scale(VVIR, variable=lrl, length=400, from_=30, to=175, resolution=1, orient=HORIZONTAL)
    lrl_scale_vvi.grid(row=4, column=1)
    lrl_scale_vvi.set(60)

    global va_scale_vvi
    va = StringVar()
    va_label = Label(VVIR, text="Ventricular Amplitude [V]", font=('Arial', 12))
    va_label.grid(row=5, column=1)
    va_scale_vvi = Scale(VVIR, variable=va, length=400, from_=0, to=5, resolution=0.1, orient=HORIZONTAL)
    va_scale_vvi.grid(row=6, column=1)
    va_scale_vvi.set(3.5)

    vrp = StringVar()
    vrp_label = Label(VVIR, text="Ventrical Refractory Period [ms]", font=('Arial', 12))
    vrp_label.grid(row=7, column=1)
    vrp_input = Scale(VVIR, variable=vrp, length=400, from_=150, to=500, resolution=10, orient=HORIZONTAL)
    vrp_input.grid(row=8, column=1)
    vrp_input.set(320)

    global current_index_vvir
    current_index_vvir = 4  # Initialize the index to 0

    vpw_label = Label(VVIR, text="Ventricular Pulse Width [ms]", font=('Arial', 12))
    vpw_label.grid(row=9, column=1)
    global value_label_vvir
    value_label_vvir = Label(VVIR, text=str(mode.scale_incs[current_index_vvir]))
    value_label_vvir.grid(row=10, column=1)

    # Create a increment/decrement button
    decrement_button = Button(VVIR, text="<", command=lambda: update_value_vvir(False))
    decrement_button.grid(row=10, column=0)
    increment_button = Button(VVIR, text=">", command=lambda: update_value_vvir(True))
    increment_button.grid(row=10, column=2)

    VVI_save = ttk.Button(VVIR, text="SAVE", width=10,
                          command=lambda: mode.Save_press(url.get(), lrl.get(), VPW=mode.scale_incs[current_index_vvir],
                                                     VA=va.get(), VRP=vrp.get(), frame=VVIR))
    VVI_save.grid(row=11, column=1)

    VVI_back = ttk.Button(VVIR, text="BACK", width=10, command=lambda: mode.Back_press(modes, VVIR))
    VVI_back.grid(row=12, column=1)

    va_scale_vvi.config(command=lambda e: mode.va_slider_mod(va_scale_vvi))  # Dynamically updates the slider resolution
    lrl_scale_vvi.config(command=lambda e: mode.lrl_slider_mod(lrl_scale_vvi))  # Dynamically updates the slider resolution


def update_value_aair(increment):
    global current_index_aair
    if increment:
        current_index_aair = (current_index_aair + 1) % len(mode.scale_incs)
    else:
        current_index_aair = (current_index_aair - 1) % len(mode.scale_incs)
    value_label_aair.config(text=str(mode.scale_incs[current_index_aair]))

def update_value_aoor(increment):
    global current_index_aoor
    if increment:
        current_index_aoor = (current_index_aoor + 1) % len(mode.scale_incs)
    else:
        current_index_aoor = (current_index_aoor - 1) % len(mode.scale_incs)
    value_label_aoor.config(text=str(mode.scale_incs[current_index_aoor]))

def update_value_vvir(increment):
    global current_index_vvir
    if increment:
        current_index_vvir = (current_index_vvir + 1) % len(mode.scale_incs)
    else:
        current_index_vvir = (current_index_vvir - 1) % len(mode.scale_incs)
    value_label_vvir.config(text=str(mode.scale_incs[current_index_vvir]))
    
def update_value_voor(increment):
    global current_index_voor
    if increment:
        current_index_voor = (current_index_voor + 1) % len(mode.scale_incs)
    else:
        current_index_voor = (current_index_voor - 1) % len(mode.scale_incs)
    value_label_voor.config(text=str(mode.scale_incs[current_index_voor]))
