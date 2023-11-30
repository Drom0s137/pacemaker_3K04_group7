import numpy as np
import os
import global_vars as glb
import serial_comm as comm



#setup ensure that time and day lists are only created once
setup = 0
offset = [5, 0.1, 1, 0.1, 10, 10, 10, 1, 1, 5, 2]
lrloffset = [5, 1, 5]
mainsizex = 800
mainsizey = 600
modeindex = 0


def main_app(on_close=None):
    global window
    window = Tk()

    class modes():
        def __init__(self, Lower_Rate_Limit, Upper_Rate_Limit,
                    Maximum_Sensor_Rate,
                    A_or_V_Pulse_Amplitude_Regulated,
                    A_or_V_Pulse_Amplitude_Unregulated,
                    A_or_V_Pulse_Width, A_or_V_Sensitivity,
                    Ventricular_Refractory_Period,
                    Atrial_Refractory_Period, Hysteresis_Rate_Limit,
                    Rate_Smoothing, Activity_Threshold,
                    Reaction_Time, Response_Factor,
                    Recovery_Time):
            self.Lower_Rate_Limit = Lower_Rate_Limit
            self.Upper_Rate_Limit = Upper_Rate_Limit
            self.Maximum_Sensor_Rate = Maximum_Sensor_Rate
            self.A_or_V_Pulse_Amplitude_Regulated = A_or_V_Pulse_Amplitude_Regulated
            self.A_or_V_Pulse_Amplitude_Unregulated = A_or_V_Pulse_Amplitude_Unregulated
            self.A_or_V_Pulse_Width = A_or_V_Pulse_Width
            self.A_or_V_Sensitivity = A_or_V_Sensitivity
            self.Ventricular_Refractory_Period = Ventricular_Refractory_Period
            self.Atrial_Refractory_Period = Atrial_Refractory_Period
            self.Hysteresis_Rate_Limit = Hysteresis_Rate_Limit
            self.Rate_Smoothing = Rate_Smoothing
            self.Activity_Threshold = Activity_Threshold
            self.Reaction_Time = Reaction_Time
            self.Response_Factor = Response_Factor
            self.Recovery_Time = Recovery_Time

            self.done_change = None
            self.p1 = self.p1plus = self.p1minus = None
            self.p2 = self.p2plus = self.p2minus = None
            self.p3 = self.p3plus = self.p3minus = None
            self.p4 = self.p4plus = self.p4minus = None
            self.p5 = self.p5plus = self.p5minus = None
            self.p6 = self.p6plus = self.p6minus = None
            self.p7 = self.p7plus = self.p7minus = None
            self.p8 = self.p8plus = self.p8minus = None
            self.p9 = self.p9plus = self.p9minus = None
            self.p10 = self.p10plus = self.p10minus = None
            self.p11 = self.p11plus = self.p11minus = None
            self.p12 = self.p12plus = self.p12minus = None
            self.p13 = self.p13plus = self.p13minus = None
            self.p14 = self.p14plus = self.p14minus = None
            self.p15 = self.p15plus = self.p15minus = None

        def change(mode):

            def del_change():
                if mode is None:
                    return
                elif mode.done_change is None:
                    return
                elif mode.done_change is not None:
                    mode.done_change.destroy()
                    mode.p1plus.destroy()
                    mode.p1minus.destroy()
                    mode.p1.destroy()
                    mode.p2plus.destroy()
                    mode.p2minus.destroy()
                    mode.p2.destroy()
                    mode.p3plus.destroy()
                    mode.p3minus.destroy()
                    mode.p3.destroy()
                    mode.p4plus.destroy()
                    mode.p4minus.destroy()
                    mode.p4.destroy()
                    mode.p5plus.destroy()
                    mode.p5minus.destroy()
                    mode.p5.destroy()
                    mode.p6plus.destroy()
                    mode.p6minus.destroy()
                    mode.p6.destroy()
                    mode.p7plus.destroy()
                    mode.p7minus.destroy()
                    mode.p7.destroy()
                    mode.p8plus.destroy()