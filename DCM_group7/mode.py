from tkinter import *
import customtkinter
import ui
import backend


def Save_press(URL, LRL, APW=None, AA=None, RS=None, AS=None, ARR=None, VPW=None, VA=None, VS=None, VRR=None):
    print("Save Pressed")
    if backend.verifyInput(int(URL), int(LRL), APW=int(APW), AA=int(AA), RS=int(RS), AS=int(AS), ARR=int(ARR), VPW=int(VPW), VA=int(VA), VS=int(VS), VRR=int(VRR)):
        return 1
    else:
        return 0

def Back_press(modes, current):
    print("Back Pressed")
    ui.switch_frame(modes, current)

## A00 Pacing Mode

def AOO_page(AOO,modes):
    label = Label(AOO, text="AOO Page", font=('Arial', 14))
    label.pack(padx=20, pady=20)

    url = StringVar()
    url_label = Label(AOO, text="Input the Upper Rate Limit", font=('Arial', 12))
    url_label.pack()
    url_scale = Scale(AOO, variable=url, length=400, from_=50, to=175, resolution=5, orient=HORIZONTAL)
    url_scale.pack(pady=10)

    lrl = StringVar()
    lrl_label = Label(AOO, text="Input the Lower Rate Limit", font=('Arial', 12))
    lrl_label.pack()
    lrl_scale = Scale(AOO, variable=lrl, length=400, from_=30, to=175, resolution=1, orient=HORIZONTAL)
    lrl_scale.pack(pady=10)

    apw = StringVar()
    apw_label = Label(AOO, text="Atrial Pulse Width", font=('Arial', 12))
    apw_label.pack()
    apw_scale = Scale(AOO, variable=apw, length=400, from_=0.05, to=1.9, resolution=0.01, orient=HORIZONTAL)
    apw_scale.pack(pady=10)

    aa = StringVar()
    aa_label = Label(AOO, text="Atrial Amplitude", font=('Arial', 12))
    aa_label.pack()
    aa_scale = Scale(AOO, variable=aa, length=400, from_=0, to=7, resolution=0.1, orient=HORIZONTAL)
    aa_scale.pack(pady=10)

    AOO_save = Button(AOO, text="SAVE", height=1, width=10, command= lambda: Save_press(url.get(), lrl.get(), APW=apw.get(), AA=aa.get()))
    AOO_save.pack(pady=10)

    AOO_back = Button(AOO, text="BACK", height=1, width=10, command= lambda: Back_press(modes, AOO))
    AOO_back.pack()


## V00 Pacing Mode
def VOO_page(VOO,modes):
    label = Label(VOO, text="VOO Page", font=('Arial', 14))
    label.pack(padx=20, pady=20)

    url = StringVar()
    url_label = Label(VOO, text="Input the Upper Rate Limit", font=('Arial', 12))
    url_label.pack(padx=20, pady=2)
    url_scale = Scale(VOO, variable=url, length=400, from_=50, to=175, resolution=5, orient=HORIZONTAL)
    url_scale.pack(pady=10)

    lrl = StringVar()
    lrl_label = Label(VOO, text="Input the Lower Rate Limit", font=('Arial', 12))
    lrl_label.pack(padx=20, pady=2)
    lrl_scale = Scale(VOO, variable=lrl, length=400, from_=30, to=175, resolution=1, orient=HORIZONTAL)
    lrl_scale.pack(pady=10)

    vpw = StringVar()
    vpw_label = Label(VOO, text="Ventricular Pulse Width", font=('Arial', 12))
    vpw_label.pack(padx=20, pady=2)
    vpw_scale = Scale(VOO, variable=vpw, length=400, from_=0.05, to=1.9, resolution=0.01, orient=HORIZONTAL)
    vpw_scale.pack(pady=10)

    va = StringVar()
    va_label = Label(VOO, text="Ventricular Amplitude", font=('Arial', 12))
    va_label.pack(padx=20, pady=2)
    va_scale = Scale(VOO, variable=va, length=400, from_=0, to=7, resolution=0.1, orient=HORIZONTAL)
    va_scale.pack(pady=10)

    VOO_save = Button(VOO, text="SAVE", height=1, width=10, command=lambda:Save_press(url.get(), lrl.get(), VPW=vpw.get(), VA=va.get()))
    VOO_save.pack(pady=10)

    VOO_back = Button(VOO, text="BACK", height=1, width=10, command=lambda:Back_press(modes, VOO))
    VOO_back.pack()


## AAI Pacing Mode

def AAI_page(AAI,modes):

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

    AAI_save = Button(AAI, text="SAVE", height=1, width=10, command=lambda:Save_press(url_scale))
    AAI_save.pack(pady=7)

    AAI_back = Button(AAI, text="BACK", height=1, width=10, command=lambda:Back_press(modes, AAI))
    AAI_back.pack()

## VVI Pacing Mode

def VVI_page(VVI, modes):

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


    VVI_save = Button(VVI, text="SAVE", height=1, width=10, command=lambda:Save_press)
    VVI_save.pack()

    VVI_back = Button(VVI, text="BACK", height=1, width=10, command=lambda:Back_press(modes,VVI))
    VVI_back.pack()


