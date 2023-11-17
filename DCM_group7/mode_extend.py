from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
import ui
import backend
import mode

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
        "VAT": VAT
    }
    temp = backend.verifyInput(settings)
    if temp[0]:
        ui.display_msg("\t\tSUCCESS\t\t", frame, 2)
        return 1
    else:
        ui.display_msg(temp[1], frame, 2)
        return 0

def update_values():
    global url_aoor, url_aair, url_voor, url_vvir, lrl_aoor, lrl_voor, lrl_aair, lrl_vvir
    global aa_aair, aa_aoor, arp_aair, va_voor, va_vvir, vrp_vvir#, apw, vpw
    global msr_aoor, msr_aair, msr_voor, msr_vvir, reactt_aoor, reactt_aair, reactt_voor, reactt_vvir
    global respfac_aoor, respfac_aair, respfac_voor, respfac_vvir, \
        recovert_aoor, recovert_aair, recovert_voor, recovert_vvir, arp_aair, vrp_vvir
    url_aoor.set(backend.USERSETTINGS[0])
    url_aair.set(backend.USERSETTINGS[0])
    url_voor.set(backend.USERSETTINGS[1])
    url_vvir.set(backend.USERSETTINGS[1])

    lrl_aoor.set(backend.USERSETTINGS[2])
    lrl_aair.set(backend.USERSETTINGS[2])
    lrl_voor.set(backend.USERSETTINGS[3])
    lrl_vvir.set(backend.USERSETTINGS[3])
    
    aa_aoor.set(backend.USERSETTINGS[4])
    aa_aair.set(backend.USERSETTINGS[4])

    va_voor.set(backend.USERSETTINGS[5])
    va_vvir.set(backend.USERSETTINGS[5])

    arp_aair.set(backend.USERSETTINGS[6])
    vrp_vvir.set(backend.USERSETTINGS[7])
    
    msr_aoor.set(backend.USERSETTINGS[10])
    msr_aair.set(backend.USERSETTINGS[10])
    msr_voor.set(backend.USERSETTINGS[11])
    msr_vvir.set(backend.USERSETTINGS[11])

    reactt_aoor.set(backend.USERSETTINGS[12])
    reactt_aair.set(backend.USERSETTINGS[12])
    reactt_voor.set(backend.USERSETTINGS[13])
    reactt_vvir.set(backend.USERSETTINGS[13])

    respfac_aoor.set(backend.USERSETTINGS[14])
    respfac_aair.set(backend.USERSETTINGS[14])
    respfac_voor.set(backend.USERSETTINGS[15])
    respfac_vvir.set(backend.USERSETTINGS[15])

    recovert_aoor.set(backend.USERSETTINGS[16])
    recovert_aair.set(backend.USERSETTINGS[16])
    recovert_voor.set(backend.USERSETTINGS[17])
    recovert_vvir.set(backend.USERSETTINGS[17])


def AOOR_page(AOOR, modes):
    label = Label(AOOR, text="AOOR Page", font=('Arial', 14))
    label.grid(row=0, column=2, columnspan=4)

    l0 = Label(AOOR, width=10, height=3) # This is blank space just to help center the layout 
    l0.grid(column=0, row=0, rowspan=10)

    plot = Label(AOOR, width=50, height=10, bg = "dark green") # This is the temporary graph holder 
    plot.grid(column=2, row=15, columnspan=4, pady=5)

    global url_aoor
    url_aoor = StringVar()
    url_label = Label(AOOR, text="Input the Upper Rate Limit [ppm]", font=('Arial', 12))
    url_label.grid(row=1, column=2)
    url_scale = Scale(AOOR, variable=url_aoor, length=400, from_=50, to=175, resolution=5, orient=HORIZONTAL)
    url_scale.grid(row=2, column=2)
    url_scale.set(120)

    global lrl_scale_aoor, lrl_aoor
    lrl_aoor = StringVar()
    lrl_label = Label(AOOR, text="Input the Lower Rate Limit [ppm]", font=('Arial', 12))
    lrl_label.grid(row=3, column=2)
    lrl_scale_aoor = Scale(AOOR, variable=lrl_aoor, length=400, from_=30, to=175, resolution=1, orient=HORIZONTAL)
    lrl_scale_aoor.grid(row=4, column=2)
    lrl_scale_aoor.set(60)

    global aa_scale_aoor, aa_aoor
    aa_aoor = StringVar()
    aa_label = Label(AOOR, text="Atrial Amplitude [V]", font=('Arial', 12))
    aa_label.grid(row=5, column=2)
    aa_scale_aoor = Scale(AOOR, variable=aa_aoor, length=400, from_=0, to=5, resolution=0.1, orient=HORIZONTAL)
    aa_scale_aoor.grid(row=6, column=2)
    aa_scale_aoor.set(3.5)

    global current_index_aoor
    current_index_aoor = 4  # Initialize the index to 0

    apw_label = Label(AOOR, text="Atrial Pulse Width [ms]", font=('Arial', 12))
    apw_label.grid(row=7, column=2)
    global value_label_aoor
    value_label_aoor = Label(AOOR, text=str(mode.scale_incs[current_index_aoor]))
    value_label_aoor.grid(row=8, column=2)

    # Create a increment/decrement button
    decrement_button = Button(AOOR, text="<", command=lambda: update_value_aoor(False))
    decrement_button.grid(row=8, column=1)
    increment_button = Button(AOOR, text=">", command=lambda: update_value_aoor(True))
    increment_button.grid(row=8, column=3)

    global msr_aoor
    msr_aoor = StringVar()
    msr_label = Label(AOOR, text="Maximum Sensor Rate [MSR]", font=('Arial', 12))
    msr_label.grid(row=1, column=5)
    msr_input = Scale(AOOR, variable=msr_aoor, length=400, from_=50, to=175, resolution=5, orient=HORIZONTAL)
    msr_input.grid(row=2, column=5)
    msr_input.set(120)

    global reactt_aoor
    reactt_aoor = StringVar()
    reactt_label = Label(AOOR, text="Reaction Time [sec]", font=('Arial', 12))
    reactt_label.grid(row=3, column=5)
    reactt_input = Scale(AOOR, variable=reactt_aoor, length=400, from_=10, to=50, resolution=10, orient=HORIZONTAL)
    reactt_input.grid(row=4, column=5)
    reactt_input.set(30)

    global respfac_aoor
    respfac_aoor = StringVar()
    respfac_label = Label(AOOR, text="Response Factor [min]", font=('Arial', 12))
    respfac_label.grid(row=5, column=5)
    respfac_input = Scale(AOOR, variable=respfac_aoor, length=400, from_=1, to=16, resolution=1, orient=HORIZONTAL)
    respfac_input.grid(row=6, column=5)
    respfac_input.set(8)

    global recovert_aoor
    recovert_aoor = StringVar()
    recovert_label = Label(AOOR, text="Recover Time [min]", font=('Arial', 12))
    recovert_label.grid(row=7, column=5)
    recovert_input = Scale(AOOR, variable=recovert_aoor, length=400, from_=2, to=16, resolution=1, orient=HORIZONTAL)
    recovert_input.grid(row=8, column=5)
    recovert_input.set(5)

    global current_activity_aoor
    current_activity_aoor = 0  # Initialize the index to 0

    actt_label = Label(AOOR, text="Activity Threshold", font=('Arial', 12))
    actt_label.grid(row=9, column=5)
    global actt_label_aoor
    actt_label_aoor = Label(AOOR, text=str(activity_list[current_activity_aoor]))
    actt_label_aoor.grid(row=10, column=5)

    # Create a increment/decrement button
    decrement_activity = Button(AOOR, text="<", command=lambda: update_activity_aoor(False))
    decrement_activity.grid(row=10, column=4)
    increment_activity = Button(AOOR, text=">", command=lambda: update_activity_aoor(True))
    increment_activity.grid(row=10, column=6)

    AOOR_save = ttk.Button(AOOR, text="SAVE", width=10,
                          command=lambda: Save_press(AURL = url_aoor.get(), ALRL = lrl_aoor.get(), APW=mode.scale_incs[current_index_aoor],
                                                     AA=aa_aoor.get(), AMSR=msr_aoor.get(), AREACT=reactt_aoor.get(), ARF=respfac_aoor.get(), 
                                                     ARECOVER=recovert_aoor.get(),  frame=AOOR))
    AOOR_save.grid(row=17, column=2, columnspan= 4)

    AOOR_back = ttk.Button(AOOR, text="BACK", width=10, command=lambda: mode.Back_press(modes, AOOR))
    AOOR_back.grid(row=18, column=2, columnspan= 4)

    aa_scale_aoor.config(command=lambda e: mode.aa_slider_mod(aa_scale_aoor))  # Dynamically updates the slider resolution
    lrl_scale_aoor.config(command=lambda e: mode.lrl_slider_mod(lrl_scale_aoor))  # Dynamically updates the slider resolution

def VOOR_page(VOOR, modes):
    label = Label(VOOR, text="VOOR Page", font=('Arial', 14))
    label.grid(row=0, column=2, columnspan=4)

    l0 = Label(VOOR, width=10, height=3) # This is blank space just to help center the layout 
    l0.grid(column=0, row=0, rowspan=10)
    
    plot = Label(VOOR, width=50, height=10, bg = "dark green") # This is the temporary graph holder 
    plot.grid(column=2, row=15, columnspan=4, pady=5)

    global url_voor
    url_voor = StringVar()
    url_label = Label(VOOR, text="Input the Upper Rate Limit [ppm]", font=('Arial', 12))
    url_label.grid(row=1, column=2)
    url_scale = Scale(VOOR, variable=url_voor, length=400, from_=50, to=175, resolution=5, orient=HORIZONTAL)
    url_scale.grid(row=2, column=2)
    url_scale.set(120)

    global lrl_scale_voo, lrl_voor
    lrl_voor = StringVar()
    lrl_label = Label(VOOR, text="Input the Lower Rate Limit [ppm]", font=('Arial', 12))
    lrl_label.grid(row=3, column=2)
    lrl_scale_voo = Scale(VOOR, variable=lrl_voor, length=400, from_=30, to=175, resolution=1, orient=HORIZONTAL)
    lrl_scale_voo.grid(row=4, column=2)
    lrl_scale_voo.set(60)

    global va_scale_voo, va_voor
    va_voor = StringVar()
    va_label = Label(VOOR, text="Ventricular Amplitude [V]", font=('Arial', 12))
    va_label.grid(row=5, column=2)
    va_scale_voo = Scale(VOOR, variable=va_voor, length=400, from_=0, to=5, resolution=0.1, orient=HORIZONTAL)
    va_scale_voo.grid(row=6, column=2)
    va_scale_voo.set(3.5)

    global current_index_voor
    current_index_voor = 4  # Initialize the index to 0

    vpw_label = Label(VOOR, text="Ventricular Pulse Width [ms]", font=('Arial', 12))
    vpw_label.grid(row=7, column=2)
    global value_label_voor
    value_label_voor = Label(VOOR, text=str(mode.scale_incs[current_index_voor]))
    value_label_voor.grid(row=8, column=2)

    # Create a increment/decrement button
    decrement_button = Button(VOOR, text="<", command=lambda: update_value_voor(False))
    decrement_button.grid(row=9, column=1)
    increment_button = Button(VOOR, text=">", command=lambda: update_value_voor(True))
    increment_button.grid(row=9, column=3)

    global msr_voor
    msr_voor = StringVar()
    msr_label = Label(VOOR, text="Maximum Sensor Rate [MSR]", font=('Arial', 12))
    msr_label.grid(row=1, column=5)
    msr_input = Scale(VOOR, variable=msr_voor, length=400, from_=50, to=175, resolution=5, orient=HORIZONTAL)
    msr_input.grid(row=2, column=5)
    msr_input.set(120)

    global reactt_voor
    reactt_voor = StringVar()
    reactt_label = Label(VOOR, text="Reaction Time [sec]", font=('Arial', 12))
    reactt_label.grid(row=3, column=5)
    reactt_input = Scale(VOOR, variable=reactt_voor, length=400, from_=10, to=50, resolution=10, orient=HORIZONTAL)
    reactt_input.grid(row=4, column=5)
    reactt_input.set(30)

    global respfac_voor
    respfac_voor = StringVar()
    respfac_label = Label(VOOR, text="Response Factor [min]", font=('Arial', 12))
    respfac_label.grid(row=5, column=5)
    respfac_input = Scale(VOOR, variable=respfac_voor, length=400, from_=1, to=16, resolution=1, orient=HORIZONTAL)
    respfac_input.grid(row=6, column=5)
    respfac_input.set(8)

    global recovert_voor
    recovert_voor = StringVar()
    recovert_label = Label(VOOR, text="Recover Time [min]", font=('Arial', 12))
    recovert_label.grid(row=7, column=5)
    recovert_input = Scale(VOOR, variable=recovert_voor, length=400, from_=2, to=16, resolution=1, orient=HORIZONTAL)
    recovert_input.grid(row=8, column=5)
    recovert_input.set(5)

    global current_activity_voor
    current_activity_voor = 0  # Initialize the index to 0

    actt_label = Label(VOOR, text="Activity Threshold", font=('Arial', 12))
    actt_label.grid(row=9, column=5)
    global actt_label_voor
    actt_label_voor = Label(VOOR, text=str(activity_list[current_activity_voor]))
    actt_label_voor.grid(row=10, column=5)

    # Create a increment/decrement button
    decrement_activity = Button(VOOR, text="<", command=lambda: update_activity_voor(False))
    decrement_activity.grid(row=10, column=4)
    increment_activity = Button(VOOR, text=">", command=lambda: update_activity_voor(True))
    increment_activity.grid(row=10, column=6)

    VOOR_save = ttk.Button(VOOR, text="SAVE", width=10,
                          command=lambda: Save_press(VURL = url_voor.get(), VLRL = lrl_voor.get(), VPW=mode.scale_incs[current_index_voor],
                                                     VA=va_voor.get(), VMSR=msr_voor.get(), VREACT=reactt_voor.get(), VRF=respfac_voor.get(), 
                                                     VRECOVER=recovert_voor.get(),  frame=VOOR))
    VOOR_save.grid(row=17, column=2, columnspan= 4)

    VOOR_back = ttk.Button(VOOR, text="BACK", width=10, command=lambda: mode.Back_press(modes, VOOR))
    VOOR_back.grid(row=18, column=2, columnspan= 4)

    va_scale_voo.config(command=lambda e: mode.va_slider_mod(va_scale_voo))  # Dynamically updates the slider resolution
    lrl_scale_voo.config(command=lambda e: mode.lrl_slider_mod(lrl_scale_voo))  # Dynamically updates the slider resolution

def AAIR_page(AAIR, modes):
    label = Label(AAIR, text="AAIR Page", font=('Arial', 14))
    label.grid(row=0, column=2, columnspan=4)

    l0 = Label(AAIR, width=10, height=3) # This is blank space just to help center the layout 
    l0.grid(column=0, row=0, rowspan=10)
    
    plot = Label(AAIR, width=50, height=10, bg = "dark green") # This is the temporary graph holder 
    plot.grid(column=2, row=15, columnspan=4, pady=5)

    global url_aair
    url_aair = StringVar()
    url_label = Label(AAIR, text="Input the Upper Rate Limit [ppm]", font=('Arial', 12))
    url_label.grid(row=1, column=2)
    url_scale = Scale(AAIR, variable=url_aair, length=400, from_=50, to=175, resolution=5, orient=HORIZONTAL)
    url_scale.grid(row=2, column=2)
    url_scale.set(120)

    global lrl_scale_aai, lrl_aair
    lrl_aair = StringVar()
    lrl_label = Label(AAIR, text="Input the Lower Rate Limit [ppm]", font=('Arial', 12))
    lrl_label.grid(row=3, column=2)
    lrl_scale_aai = Scale(AAIR, variable=lrl_aair, length=400, from_=30, to=175, resolution=1, orient=HORIZONTAL)
    lrl_scale_aai.grid(row=4, column=2)
    lrl_scale_aai.set(60)

    global aa_scale_aii, aa_aair
    aa_aair = StringVar()
    aa_label = Label(AAIR, text="Atrial Amplitude [V]", font=('Arial', 12))
    aa_label.grid(row=5, column=2)
    aa_scale_aii = Scale(AAIR, variable=aa_aair, length=400, from_=0, to=5, resolution=0.1, orient=HORIZONTAL)
    aa_scale_aii.grid(row=6, column=2)
    aa_scale_aii.set(3.5)

    global arp_aair
    arp_aair = StringVar()
    arp_label = Label(AAIR, text="Atrial Refractory Period [ms]", font=('Arial', 12))
    arp_label.grid(row=7, column=2)
    arp_input = Scale(AAIR, variable=arp_aair, length=400, from_=150, to=500, resolution=10, orient=HORIZONTAL)
    arp_input.grid(row=8, column=2)
    arp_input.set(250)

    global current_index_aair
    current_index_aair = 4  # Initialize the index to 0

    apw_label = Label(AAIR, text="Atrial Pulse Width [ms]", font=('Arial', 12))
    apw_label.grid(row=9, column=2)
    global value_label_aair
    value_label_aair = Label(AAIR, text=str(mode.scale_incs[current_index_aair]))
    value_label_aair.grid(row=10, column=2)

    # Create a increment/decrement button
    decrement_button = Button(AAIR, text="<", command=lambda: update_value_aair(False))
    decrement_button.grid(row=10, column=1)
    increment_button = Button(AAIR, text=">", command=lambda: update_value_aair(True))
    increment_button.grid(row=10, column=3)

    global msr_aair
    msr_aair = StringVar()
    msr_label = Label(AAIR, text="Maximum Sensor Rate [MSR]", font=('Arial', 12))
    msr_label.grid(row=1, column=5)
    msr_input = Scale(AAIR, variable=msr_aair, length=400, from_=50, to=175, resolution=5, orient=HORIZONTAL)
    msr_input.grid(row=2, column=5)
    msr_input.set(120)

    global reactt_aair
    reactt_aair = StringVar()
    reactt_label = Label(AAIR, text="Reaction Time [sec]", font=('Arial', 12))
    reactt_label.grid(row=3, column=5)
    reactt_input = Scale(AAIR, variable=reactt_aair, length=400, from_=10, to=50, resolution=10, orient=HORIZONTAL)
    reactt_input.grid(row=4, column=5)
    reactt_input.set(30)

    global respfac_aair
    respfac_aair = StringVar()
    respfac_label = Label(AAIR, text="Response Factor [min]", font=('Arial', 12))
    respfac_label.grid(row=5, column=5)
    respfac_input = Scale(AAIR, variable=respfac_aair, length=400, from_=1, to=16, resolution=1, orient=HORIZONTAL)
    respfac_input.grid(row=6, column=5)
    respfac_input.set(8)

    global recovert_aair
    recovert_aair = StringVar()
    recovert_label = Label(AAIR, text="Recover Time [min]", font=('Arial', 12))
    recovert_label.grid(row=7, column=5)
    recovert_input = Scale(AAIR, variable=recovert_aair, length=400, from_=2, to=16, resolution=1, orient=HORIZONTAL)
    recovert_input.grid(row=8, column=5)
    recovert_input.set(5)

    global current_activity_aair
    current_activity_aair = 0  # Initialize the index to 0

    actt_label = Label(AAIR, text="Activity Threshold", font=('Arial', 12))
    actt_label.grid(row=9, column=5)
    global actt_label_aair
    actt_label_aair = Label(AAIR, text=str(activity_list[current_activity_aair]))
    actt_label_aair.grid(row=10, column=5)

    # Create a increment/decrement button
    decrement_activity = Button(AAIR, text="<", command=lambda: update_activity_aair(False))
    decrement_activity.grid(row=10, column=4)
    increment_activity = Button(AAIR, text=">", command=lambda: update_activity_aair(True))
    increment_activity.grid(row=10, column=6)

    AAIR_save = ttk.Button(AAIR, text="SAVE", width=10,
                          command=lambda: Save_press(AURL = url_aair.get(), ALRL = lrl_aair.get(), APW=mode.scale_incs[current_index_aair],
                                                     AA=aa_aair.get(), AMSR=msr_aair.get(), AREACT=reactt_aair.get(), 
                                                     ARF=respfac_aair.get(), ARECOVER=recovert_aair.get(), ARP=arp_aair.get(), frame=AAIR))
    AAIR_save.grid(row=17, column=2, columnspan= 4)

    AAIR_back = ttk.Button(AAIR, text="BACK", width=10, command=lambda: mode.Back_press(modes, AAIR))
    AAIR_back.grid(row=18, column=2, columnspan= 4)

    aa_scale_aii.config(command=lambda e: mode.aa_slider_mod(aa_scale_aii))  # Dynamically updates the slider resolution
    lrl_scale_aai.config(command=lambda e: mode.lrl_slider_mod(lrl_scale_aai))  # Dynamically updates the slider resolution


def VVIR_page(VVIR, modes):
    label = Label(VVIR, text="VVIR Page", font=('Arial', 14))
    label.grid(row=0, column=2, columnspan=4)
    
    l0 = Label(VVIR, width=10, height=3) # This is blank space just to help center the layout 
    l0.grid(column=0, row=0, rowspan=10)
    
    plot = Label(VVIR, width=50, height=10, bg = "dark green") # This is the temporary graph holder 
    plot.grid(column=2, row=15, columnspan=4, pady=5)

    global url_vvir
    url_vvir = StringVar()
    url_label = Label(VVIR, text="Input the Upper Rate Limit [ppm]", font=('Arial', 12))
    url_label.grid(row=1, column=2)
    url_scale = Scale(VVIR, variable=url_vvir, length=400, from_=50, to=175, resolution=5, orient=HORIZONTAL)
    url_scale.grid(row=2, column=2)
    url_scale.set(120)

    global lrl_scale_vvi, lrl_vvir
    lrl_vvir = StringVar()
    lrl_label = Label(VVIR, text="Input the Lower Rate Limit [ppm]", font=('Arial', 12))
    lrl_label.grid(row=3, column=2)
    lrl_scale_vvi = Scale(VVIR, variable=lrl_vvir, length=400, from_=30, to=175, resolution=1, orient=HORIZONTAL)
    lrl_scale_vvi.grid(row=4, column=2)
    lrl_scale_vvi.set(60)

    global va_scale_vvi, va_vvir
    va_vvir = StringVar()
    va_label = Label(VVIR, text="Ventricular Amplitude [V]", font=('Arial', 12))
    va_label.grid(row=5, column=2)
    va_scale_vvi = Scale(VVIR, variable=va_vvir, length=400, from_=0, to=5, resolution=0.1, orient=HORIZONTAL)
    va_scale_vvi.grid(row=6, column=2)
    va_scale_vvi.set(3.5)

    global vrp_vvir
    vrp_vvir = StringVar()
    vrp_label = Label(VVIR, text="Ventrical Refractory Period [ms]", font=('Arial', 12))
    vrp_label.grid(row=7, column=2)
    vrp_input = Scale(VVIR, variable=vrp_vvir, length=400, from_=150, to=500, resolution=10, orient=HORIZONTAL)
    vrp_input.grid(row=8, column=2)
    vrp_input.set(320)

    global current_index_vvir
    current_index_vvir = 4  # Initialize the index to 0

    vpw_label = Label(VVIR, text="Ventricular Pulse Width [ms]", font=('Arial', 12))
    vpw_label.grid(row=9, column=2)
    global value_label_vvir
    value_label_vvir = Label(VVIR, text=str(mode.scale_incs[current_index_vvir]))
    value_label_vvir.grid(row=10, column=2)

    # Create a increment/decrement button
    decrement_button = Button(VVIR, text="<", command=lambda: update_value_vvir(False))
    decrement_button.grid(row=10, column=1)
    increment_button = Button(VVIR, text=">", command=lambda: update_value_vvir(True))
    increment_button.grid(row=10, column=3)

    global msr_vvir
    msr_vvir = StringVar()
    msr_label = Label(VVIR, text="Maximum Sensor Rate [MSR]", font=('Arial', 12))
    msr_label.grid(row=1, column=5)
    msr_input = Scale(VVIR, variable=msr_vvir, length=400, from_=50, to=175, resolution=5, orient=HORIZONTAL)
    msr_input.grid(row=2, column=5)
    msr_input.set(120)

    global reactt_vvir
    reactt_vvir = StringVar()
    reactt_label = Label(VVIR, text="Reaction Time [sec]", font=('Arial', 12))
    reactt_label.grid(row=3, column=5)
    reactt_input = Scale(VVIR, variable=reactt_vvir, length=400, from_=10, to=50, resolution=10, orient=HORIZONTAL)
    reactt_input.grid(row=4, column=5)
    reactt_input.set(30)

    global respfac_vvir
    respfac_vvir = StringVar()
    respfac_label = Label(VVIR, text="Response Factor [min]", font=('Arial', 12))
    respfac_label.grid(row=5, column=5)
    respfac_input = Scale(VVIR, variable=respfac_vvir, length=400, from_=1, to=16, resolution=1, orient=HORIZONTAL)
    respfac_input.grid(row=6, column=5)
    respfac_input.set(8)

    global recovert_vvir
    recovert_vvir = StringVar()
    recovert_label = Label(VVIR, text="Recover Time [min]", font=('Arial', 12))
    recovert_label.grid(row=7, column=5)
    recovert_input = Scale(VVIR, variable=recovert_vvir, length=400, from_=2, to=16, resolution=1, orient=HORIZONTAL)
    recovert_input.grid(row=8, column=5)
    recovert_input.set(5)

    global current_activity_vvir
    current_activity_vvir = 0  # Initialize the index to 0

    actt_label = Label(VVIR, text="Activity Threshold", font=('Arial', 12))
    actt_label.grid(row=9, column=5)
    global actt_label_vvir
    actt_label_vvir = Label(VVIR, text=str(activity_list[current_activity_vvir]))
    actt_label_vvir.grid(row=10, column=5)

    # Create a increment/decrement button
    decrement_activity = Button(VVIR, text="<", command=lambda: update_activity_vvir(False))
    decrement_activity.grid(row=10, column=4)
    increment_activity = Button(VVIR, text=">", command=lambda: update_activity_vvir(True))
    increment_activity.grid(row=10, column=6)

    VVIR_save = ttk.Button(VVIR, text="SAVE", width=10,
                          command=lambda: Save_press(VURL = url_vvir.get(), VLRL = lrl_vvir.get(), VPW=mode.scale_incs[current_index_vvir],
                                                     VA=va_vvir.get(), VMSR=msr_vvir.get(), VREACT=reactt_vvir.get(), 
                                                     VRF=respfac_vvir.get(), VRECOVER=recovert_vvir.get(), VRP=vrp_vvir.get(), frame=VVIR))
    VVIR_save.grid(row=17, column=2, columnspan= 4)

    VVIR_back = ttk.Button(VVIR, text="BACK", width=10, command=lambda: mode.Back_press(modes, VVIR))
    VVIR_back.grid(row=18, column=2, columnspan= 4)

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

def update_activity_aoor(increment):
    global current_activity_aoor
    if increment:
        current_activity_aoor = (current_activity_aoor + 1) % len(activity_list)
    else:
        current_activity_aoor = (current_activity_aoor - 1) % len(activity_list)
    actt_label_aoor.config(text=str(activity_list[current_activity_aoor]))

def update_activity_voor(increment):
    global current_activity_voor
    if increment:
        current_activity_voor = (current_activity_voor + 1) % len(activity_list)
    else:
        current_activity_voor = (current_activity_voor - 1) % len(activity_list)
    actt_label_voor.config(text=str(activity_list[current_activity_voor]))

def update_activity_aair(increment):
    global current_activity_aair
    if increment:
        current_activity_aair = (current_activity_aair + 1) % len(activity_list)
    else:
        current_activity_aair = (current_activity_aair - 1) % len(activity_list)
    actt_label_aair.config(text=str(activity_list[current_activity_aair]))

def update_activity_vvir(increment):
    global current_activity_vvir
    if increment:
        current_activity_vvir = (current_activity_vvir + 1) % len(activity_list)
    else:
        current_activity_vvir = (current_activity_vvir - 1) % len(activity_list)
    actt_label_vvir.config(text=str(activity_list[current_activity_vvir]))

global activity_list
activity_list = ["V-Low", "Low", "Med-Low", "Med", "Med-High", "High", "V-High"]