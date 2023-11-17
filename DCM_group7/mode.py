from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
import ui
import backend


def Save_press(frame, AURL=-1, VURL=-1, ALRL=-1, VLRL = -1, \
               APW=-1, AA=-1, ARP=-1, VPW=-1, VA=-1, VRP=-1,\
                AMSR=-1, VMSR=-1, AREACT=-1, VREACT=-1, ARF=-1, VRF=-1,\
                    ARECOVER=-1, VRECOVER=-1, AAT=-1, VAT=-1):
    print("Save Pressed")
    settings = {
        "AURL": AURL,
        "VURL": VURL,
        "ALRL": ALRL,
        "VLRL": VLRL,
        "APW": APW,
        "AA": AA,
        "ARP": ARP,
        "VPW": VPW,
        "VA": VA,
        "VRP": VRP,
        "AMSR": AMSR,
        "VMSR": VMSR,
        "AREACT":AREACT,
        "VREACT":VREACT,
        "ARF": ARF,
        "VRF": VRF,
        "ARECOVER": ARECOVER,
        "VRECOVER": VRECOVER,
        "AAT": AAT,
        "VAT": AAT
    }
    temp = backend.verifyInput(settings)
    if temp[0]:
        ui.display_msg("\t\tSUCCESS\t\t", frame, 2)
        return 1
    else:
        ui.display_msg(temp[1], frame, 2)
        return 0


def Back_press(modes, current):
    print("Back Pressed")
    ui.switch_frame(modes, current)


def update_values():
    global url_aoo, url_aai, url_voo, url_vvi, lrl_aoo, lrl_voo, lrl_aai, lrl_vvi
    global aa_aai, aa_aoo, arp_aai, va_voo, va_vvi, vrp_vvi#, apw, vpw
    #global amsr, vmsr, areact, vreact, arf, vrf, arecover, vrecover, aat, vat
    url_aoo.set(backend.USERSETTINGS[0])
    url_aai.set(backend.USERSETTINGS[0])
    url_voo.set(backend.USERSETTINGS[1])
    url_vvi.set(backend.USERSETTINGS[1])

    lrl_aoo.set(backend.USERSETTINGS[2])
    lrl_aai.set(backend.USERSETTINGS[2])
    lrl_voo.set(backend.USERSETTINGS[3])
    lrl_vvi.set(backend.USERSETTINGS[3])
    
    aa_aoo.set(backend.USERSETTINGS[4])
    aa_aai.set(backend.USERSETTINGS[4])

    va_voo.set(backend.USERSETTINGS[5])
    va_vvi.set(backend.USERSETTINGS[5])

    arp_aai.set(backend.USERSETTINGS[6])
    vrp_vvi.set(backend.USERSETTINGS[7])
    '''amsr.set(backend.USERSETTINGS[10])
    vmsr.set(backend.USERSETTINGS[11])
    areact.set(backend.USERSETTINGS[12])
    vreact.set(backend.USERSETTINGS[13])
    arf.set(backend.USERSETTINGS[14])
    vrf.set(backend.USERSETTINGS[15])
    arecover.set(backend.USERSETTINGS[16])
    vrecover.set(backend.USERSETTINGS[17])
    aat.set(backend.USERSETTINGS[18])
    vat.set(backend.USERSETTINGS[19])'''

## A00 Pacing Mode

    
def AOO_page(AOO, modes):
    l0 = Label(AOO, width=37, height=3) # This is blank space just to help center the layout 
    l0.grid(column=0, row=0, rowspan=10)

    plot = Label(AOO, width=50, height=10, bg = "dark green") # This is the temporary graph holder 
    plot.grid(column=1, row = 9, columnspan=3, pady=5)

    label = Label(AOO, text="AOO Page", font=('Arial', 14))
    label.grid(row=0, column=2)

    global url_aoo
    url_aoo = StringVar()
    url_label = Label(AOO, text="Input the Upper Rate Limit [ppm]", font=('Arial', 12))
    url_label.grid(row=1, column=2)
    aurl_scale = Scale(AOO, variable=url_aoo, length=400, from_=50, to=175, resolution=5, orient=HORIZONTAL)
    aurl_scale.grid(row=2, column=2)
    aurl_scale.set(120)

    global alrl_scale, lrl_aoo
    lrl_aoo = StringVar()
    lrl_label = Label(AOO, text="Input the Lower Rate Limit [ppm]", font=('Arial', 12))
    lrl_label.grid(row=3, column=2)
    alrl_scale = Scale(AOO, variable=lrl_aoo, length=400, from_=30, to=175, resolution=1, orient=HORIZONTAL)
    alrl_scale.grid(row=4, column=2)
    alrl_scale.set(60)

    global aa_scale, aa_aoo
    aa_aoo = StringVar()
    aa_label = Label(AOO, text="Atrial Amplitude [V]", font=('Arial', 12))
    aa_label.grid(row=5, column=2)
    aa_scale = Scale(AOO, variable=aa_aoo, length=400, from_=0, to=5, resolution=0.1, orient=HORIZONTAL)
    aa_scale.grid(row=6, column=2)
    aa_scale.set(3.5)

    global current_index_aoo
    current_index_aoo = 4  # Initialize the index to 0

    apw_label = Label(AOO, text="Atrial Pulse Width [ms]", font=('Arial', 12))
    apw_label.grid(row=7, column=2)
    global value_label_aoo
    value_label_aoo = Label(AOO, text=str(scale_incs[current_index_aoo]))
    value_label_aoo.grid(row=8, column=2)

    # Create a increment/decrement button
    decrement_button = Button(AOO, text="<", command=lambda: update_value_aoo(False))
    decrement_button.grid(row=8, column=1)
    increment_button = Button(AOO, text=">", command=lambda: update_value_aoo(True))
    increment_button.grid(row=8, column=3)

    AOO_save = ttk.Button(AOO, text="SAVE", width=10,
                          command=lambda: Save_press(AURL=url_aoo.get(), ALRL=lrl_aoo.get(), APW=scale_incs[current_index_aoo],
                                                     AA=aa_aoo.get(), frame=AOO))
    AOO_save.grid(row=10, column=2)

    AOO_back = ttk.Button(AOO, text="BACK", width=10, command=lambda: Back_press(modes, AOO))
    AOO_back.grid(row=11, column=2)

    aa_scale.config(command=lambda e: aa_slider_mod(aa_scale))  # Dynamically updates the slider resolution
    alrl_scale.config(command=lambda e: lrl_slider_mod(alrl_scale))  # Dynamically updates the slider resolution


## V00 Pacing Mode
def VOO_page(VOO, modes):
        
    l0 = Label(VOO, width=37, height=3) # This is blank space just to help center the layout 
    l0.grid(column=0, row=0, rowspan=10)

    plot = Label(VOO, width=50, height=10, bg = "dark green") # This is the temporary graph holder 
    plot.grid(column=1, row = 16, columnspan=3, pady=5)

    label = Label(VOO, text="VOO Page", font=('Arial', 14))
    label.grid(row=0, column=2)

    global url_voo
    url_voo = StringVar()
    url_label = Label(VOO, text="Input the Upper Rate Limit [ppm]", font=('Arial', 12))
    url_label.grid(row=2, column=2)
    vurl_scale = Scale(VOO, variable=url_voo, length=400, from_=50, to=175, resolution=5, orient=HORIZONTAL)
    vurl_scale.grid(row=3, column=2)
    vurl_scale.set(120)

    global vlrl_scale, lrl_voo
    lrl_voo = StringVar()
    lrl_label = Label(VOO, text="Input the Lower Rate Limit [ppm]", font=('Arial', 12))
    lrl_label.grid(row=6, column=2)
    vlrl_scale = Scale(VOO, variable=lrl_voo, length=400, from_=30, to=175, resolution=1, orient=HORIZONTAL)
    vlrl_scale.grid(row=7, column=2)
    vlrl_scale.set(60)

    global va_scale, va_voo
    va_voo = StringVar()
    va_label = Label(VOO, text="Ventricular Amplitude [V]", font=('Arial', 12))
    va_label.grid(row=10, column=2)
    va_scale = Scale(VOO, variable=va_voo, length=400, from_=0, to=5, resolution=0.1, orient=HORIZONTAL)
    va_scale.grid(row=11, column=2)
    va_scale.set(3.5)

    global current_index_voo
    current_index_voo = 4  # Initialize the index to 0

    vpw_label = Label(VOO, text="Ventricular Pulse Width [ms]", font=('Arial', 12))
    vpw_label.grid(row=14, column=2)
    global value_label_voo
    value_label_voo = Label(VOO, text=str(scale_incs[current_index_voo]))
    value_label_voo.grid(row=15, column=2)

    # Create a increment/decrement button
    decrement_button = Button(VOO, text="<", command=lambda: update_value_voo(False))
    decrement_button.grid(row=15, column=1)
    increment_button = Button(VOO, text=">", command=lambda: update_value_voo(True))
    increment_button.grid(row=15, column=3)

    VOO_save = ttk.Button(VOO, text="SAVE", width=10,
                          command=lambda: Save_press(VURL=url_voo.get(), VLRL=lrl_voo.get(), VPW=scale_incs[current_index_voo],
                                                     VA=va_voo.get(), frame=VOO))
    VOO_save.grid(row=18, column=2)
    VOO_back = ttk.Button(VOO, text="BACK", width=10, command=lambda: Back_press(modes, VOO))
    VOO_back.grid(row=25, column=2)

    va_scale.config(command=lambda e: va_slider_mod(va_scale))  # Dynamically updates the slider resolution
    vlrl_scale.config(command=lambda e: lrl_slider_mod(vlrl_scale))  # Dynamically updates the slider resolution


## AAI Pacing Mode

def AAI_page(AAI, modes):
        
    l0 = Label(AAI, width=37, height=3) # This is blank space just to help center the layout 
    l0.grid(column=0, row=0, rowspan=10)

    plot = Label(AAI, width=50, height=10, bg = "dark green") # This is the temporary graph holder 
    plot.grid(column=1, row = 13, columnspan=3, pady=5)

    label = Label(AAI, text="AAI Page", font=('Arial', 14))
    label.grid(row=0, column=2)

    global url_aai
    url_aai = StringVar()
    url_label = Label(AAI, text="Input the Upper Rate Limit [ppm]", font=('Arial', 12))
    url_label.grid(row=1, column=2)
    aurl_scale = Scale(AAI, variable=url_aai, length=400, from_=50, to=175, resolution=5, orient=HORIZONTAL)
    aurl_scale.grid(row=2, column=2)
    aurl_scale.set(120)

    global alrl_scale, lrl_aai
    lrl_aai = StringVar()
    lrl_label = Label(AAI, text="Input the Lower Rate Limit [ppm]", font=('Arial', 12))
    lrl_label.grid(row=3, column=2)
    alrl_scale = Scale(AAI, variable=lrl_aai, length=400, from_=30, to=175, resolution=1, orient=HORIZONTAL)
    alrl_scale.grid(row=4, column=2)
    alrl_scale.set(60)

    global aa_scale, aa_aai
    aa_aai = StringVar()
    aa_label = Label(AAI, text="Atrial Amplitude [V]", font=('Arial', 12))
    aa_label.grid(row=7, column=2)
    aa_scale = Scale(AAI, variable=aa_aai, length=400, from_=0, to=5, resolution=0.1, orient=HORIZONTAL)
    aa_scale.grid(row=8, column=2)
    aa_scale.set(3.5)

    global arp_aai
    arp_aai = StringVar()
    arp_label = Label(AAI, text="Atrial Refractory Period [ms]", font=('Arial', 12))
    arp_label.grid(row=9, column=2)
    arp_input = Scale(AAI, variable=arp_aai, length=400, from_=150, to=500, resolution=10, orient=HORIZONTAL)
    arp_input.grid(row=10, column=2)
    arp_input.set(250)

    global current_index_aai
    current_index_aai = 4  # Initialize the index to 0

    apw_label = Label(AAI, text="Atrial Pulse Width [ms]", font=('Arial', 12))
    apw_label.grid(row=11, column=2)
    global value_label_aai
    value_label_aai = Label(AAI, text=str(scale_incs[current_index_aai]))
    value_label_aai.grid(row=12, column=2)

    # Create a increment/decrement button
    decrement_button = Button(AAI, text="<", command=lambda: update_value_aai(False))
    decrement_button.grid(row=12, column=1)
    increment_button = Button(AAI, text=">", command=lambda: update_value_aai(True))
    increment_button.grid(row=12, column=3)

    AAI_save = ttk.Button(AAI, text="SAVE", width=10,
                          command=lambda: Save_press(AURL=url_aai.get(), ALRL=lrl_aai.get(), APW=scale_incs[current_index_aai],
                                                     AA=aa_aai.get(), ARP=arp_aai.get(), frame=AAI))
    AAI_save.grid(row=14, column=2)

    AAI_back = ttk.Button(AAI, text="BACK", width=10, command=lambda: Back_press(modes, AAI))
    AAI_back.grid(row=16, column=2)

    aa_scale.config(command=lambda e: aa_slider_mod(aa_scale))  # Dynamically updates the slider resolution
    alrl_scale.config(command=lambda e: lrl_slider_mod(alrl_scale))  # Dynamically updates the slider resolution


def VVI_page(VVI, modes):
        
    l0 = Label(VVI, width=37, height=3) # This is blank space just to help center the layout 
    l0.grid(column=0, row=0, rowspan=10)

    plot = Label(VVI, width=50, height=10, bg = "dark green") # This is the temporary graph holder 
    plot.grid(column=1, row = 11, columnspan=3, pady=5)

    label = Label(VVI, text="VVI Page", font=('Arial', 14))
    label.grid(row=0, column=2)

    global url_vvi
    url_vvi = StringVar()
    url_label = Label(VVI, text="Input the Upper Rate Limit [ppm]", font=('Arial', 12))
    url_label.grid(row=1, column=2)
    vurl_scale = Scale(VVI, variable=url_vvi, length=400, from_=50, to=175, resolution=5, orient=HORIZONTAL)
    vurl_scale.grid(row=2, column=2)
    vurl_scale.set(120)

    global vlrl_scale, lrl_vvi
    lrl_vvi = StringVar()
    lrl_label = Label(VVI, text="Input the Lower Rate Limit [ppm]", font=('Arial', 12))
    lrl_label.grid(row=3, column=2)
    vlrl_scale = Scale(VVI, variable=lrl_vvi, length=400, from_=30, to=175, resolution=1, orient=HORIZONTAL)
    vlrl_scale.grid(row=4, column=2)
    vlrl_scale.set(60)

    global va_scale, va_vvi
    va_vvi = StringVar()
    va_label = Label(VVI, text="Ventricular Amplitude [V]", font=('Arial', 12))
    va_label.grid(row=5, column=2)
    va_scale = Scale(VVI, variable=va_vvi, length=400, from_=0, to=5, resolution=0.1, orient=HORIZONTAL)
    va_scale.grid(row=6, column=2)
    va_scale.set(3.5)

    global vrp_vvi
    vrp_vvi = StringVar()
    vrp_label = Label(VVI, text="Ventrical Refractory Period [ms]", font=('Arial', 12))
    vrp_label.grid(row=7, column=2)
    vrp_input = Scale(VVI, variable=vrp_vvi, length=400, from_=150, to=500, resolution=10, orient=HORIZONTAL)
    vrp_input.grid(row=8, column=2)
    vrp_input.set(320)

    global current_index_vvi
    current_index_vvi = 4  # Initialize the index to 0

    vpw_label = Label(VVI, text="Ventricular Pulse Width [ms]", font=('Arial', 12))
    vpw_label.grid(row=9, column=2)
    global value_label_vvi
    value_label_vvi = Label(VVI, text=str(scale_incs[current_index_vvi]))
    value_label_vvi.grid(row=10, column=2)

    # Create a increment/decrement button
    decrement_button = Button(VVI, text="<", command=lambda: update_value_vvi(False))
    decrement_button.grid(row=10, column=1)
    increment_button = Button(VVI, text=">", command=lambda: update_value_vvi(True))
    increment_button.grid(row=10, column=3)

    VVI_save = ttk.Button(VVI, text="SAVE", width=10,
                          command=lambda: Save_press(VURL=url_vvi.get(), VLRL=lrl_vvi.get(), VPW=scale_incs[current_index_vvi],
                                                     VA=va_vvi.get(), VRP=vrp_vvi.get(), frame=VVI))
    VVI_save.grid(row=12, column=2)

    VVI_back = ttk.Button(VVI, text="BACK", width=10, command=lambda: Back_press(modes, VVI))
    VVI_back.grid(row=13, column=2)

    va_scale.config(command=lambda e: va_slider_mod(va_scale))  # Dynamically updates the slider resolution
    vlrl_scale.config(command=lambda e: lrl_slider_mod(vlrl_scale))  # Dynamically updates the slider resolution

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
