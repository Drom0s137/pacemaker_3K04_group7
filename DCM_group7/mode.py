from tkinter import *
import customtkinter

## A00 Pacing Mode
def AOO_page(AOO):

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


## V00 Pacing Mode
def VOO_page(VOO):

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


## AAI Pacing Mode
def AAI_page(AAI):

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


## VVI Pacing Mode
def VVI_page(VVI):

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

