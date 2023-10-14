# import tkinter as tk

# # List of values
# scale_incs = [0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9]
# current_index = 0  # Initialize the index to 0

# def update_value(increment):
#     global current_index
#     if increment:
#         current_index = (current_index + 1) % len(scale_incs)
#     else:
#         current_index = (current_index - 1) % len(scale_incs)
#     value_label.config(text=str(scale_incs[current_index]))

# # Create a Tkinter window
# root = tk.Tk()
# root.title("Value Grid")

# # Create a label to display the value
# value_label = tk.Label(root, text=str(scale_incs[current_index]))
# value_label.grid(row=0, column=1)

# # Create a decrement button
# decrement_button = tk.Button(root, text="<", command=lambda: update_value(False))
# decrement_button.grid(row=0, column=0)

# # Create an increment button
# increment_button = tk.Button(root, text=">", command=lambda: update_value(True))
# increment_button.grid(row=0, column=2)

# # Start the Tkinter main loop
# root.mainloop()

#_________________________________________________________________________________

# Do not touch
# ## V00 Pacing Mode
# def VOO_page(VOO):
#     label = Label(VOO, text="VOO Page", font=('Arial', 14))
#     label.pack(padx=20, pady=20)

#     url_label = Label(VOO, text="Input the Upper Rate Limit", font=('Arial', 12))
#     url_label.pack(padx=20, pady=2)
#     url_scale = Scale(VOO, length=400, from_=50, to=175, resolution=5, orient=HORIZONTAL)
#     url_scale.pack(pady=10)

#     global lrl_scale_voo
#     lrl_label = Label(VOO, text="Input the Lower Rate Limit", font=('Arial', 12))
#     lrl_label.pack(padx=20, pady=2)
#     lrl_scale_voo = Scale(VOO, length=400, from_=30, to=175, resolution=1, orient=HORIZONTAL)
#     lrl_scale_voo.pack(pady=10)

#     global vpw_scale_voo
#     vpw_label = Label(VOO, text="Ventricular Pulse Width", font=('Arial', 12))
#     vpw_label.pack(padx=20, pady=2)
#     # vpw_scale_voo = Scale(VOO, length=400, from_=0.05, to=1.9, orient=HORIZONTAL)
#     # vpw_scale_voo.pack(pady=10)

#     global va_scale_voo
#     va_label = Label(VOO, text="Ventricular Amplitude", font=('Arial', 12))
#     va_label.pack(padx=20, pady=2)
#     va_scale_voo = Scale(VOO, length=400, from_=0, to=5, resolution=0.1, orient=HORIZONTAL)
#     va_scale_voo.pack(pady=10)

#     VOO_save = ttk.Button(VOO, text="SAVE", width=10, command=Save_press)
#     VOO_save.pack(pady=10)

#     VOO_back = ttk.Button(VOO, text="BACK", width=10, command=Back_press)
#     VOO_back.pack()

#     global scale_incs
#     scale_incs = [0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9]
#     current_index = 0  # Initialize the index to 0

#     global value_label
#     value_label = Label(VOO, text=str(scale_incs[current_index]))
#     value_label.grid(row=0, column=1)

#     # Create a decrement button
#     decrement_button = Button(VOO, text="<", command=lambda: update_value(False))
#     decrement_button.grid(row=0, column=0)

#     # Create an increment button
#     increment_button = Button(VOO, text=">", command=lambda: update_value(True))
#     increment_button.grid(row=0, column=2)

#     # vpw_scale_voo.bind("<Motion>", on_scale_motion)
#     # vpw_scale_voo.config(command=lambda e: vpw_slider_mod(vpw_scale_voo)) # Dynamically updates the slider resolution
#     va_scale_voo.config(command=lambda e: va_slider_mod(va_scale_voo)) # Dynamically updates the slider resolution
#     lrl_scale_voo.config(command=lambda e: lrl_slider_mod(lrl_scale_voo)) # Dynamically updates the slider resolution

#________________________________________________________________________________________________

# def vpw_slider_mod(scale):
#     current = float(scale.get())
#     print(current)
#     print(direction)
#     # if current < 0.1:
#     #     scale.config(from_=0.05, to=1.9, resolution=(0.05), digits=3)
#     if current <= 0.1:
#         scale.config(from_=0.05, to=1.9, resolution=(0.01), digits=3)
#         print("sliding left")
#     # elif current >= 0.1 and current <0.15 and direction == "right":
#     #     scale.config(from_=0.05, to=1.9, resolution=(0.1), digits=4)
#     #     print("sliding right")
#     else:
#         scale.config(from_=0.05, to=1.9, resolution=(0.1), digits=3)
#         print("out of worry zone")

#________________________________________________________________________________________________

# # Initialize variables
# previous_x = None

# def on_scale_motion(event):
#     global previous_x
#     current_x = event.x_root  # Get the current x position of the mouse
    
#     if previous_x is not None:
#         global direction
#         if current_x > previous_x:
#             direction = "right"
#         elif current_x < previous_x:
#             direction = "left"
#         else:
#             direction = "no change"
        
#         # print(f"Sliding {direction}")
    
#     # Update the previous_x for the next event
#     previous_x = current_x


#________________________________________________________________________________________________

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

#________________________________________________________________________________________________

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

    # pvarp_label = Label(AAI, text="PVARP", font=('Arial', 12))
    # pvarp_label.pack(padx=20, pady=2)
    # pvarp_input = Scale(AAI, length=400, from_=150, to=500, resolution=10, orient=HORIZONTAL)
    # pvarp_input.pack()