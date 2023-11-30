import serial
import serial.tools.list_ports
import struct

# add default values for AA onwards
# this file is the one you spit data to send
frdm_port = "COM4"
Start = b'\x16'
SYNC = b'\x22'
Fn_set = b'\x55'


def check_connect():
    Start = b'\x16'
    SYNC = b'\x22'
    Signal_echo = Start + SYNC
    i = 0
    Signal_echo = Signal_echo + struct.pack("B", 2)
    while (i < 71):
        Signal_echo = Signal_echo + struct.pack("B", 0)
        i = i + 1
    # frdm_port = "COM6"
    connection = 0
    try:
        with serial.Serial(frdm_port, 115200, timeout=5) as pacemaker:
            pacemaker.write(Signal_echo)
            connection = 0
            # data = pacemaker.read(8)
            connection = 1
            return connection
    except:
        return connection


def read_ecg():
    # frdm_port = "COM6"
    Start = b'\x16'
    SYNC = b'\x22'
    Fn_set = b'\x55'
    Signal_echo = Start + SYNC
    i = 0
    while (i < 72):
        Signal_echo = Signal_echo + struct.pack("B", 0)
        i = i + 1

    with serial.Serial(frdm_port, 115200) as pacemaker:
        pacemaker.write(Signal_echo)
        data = pacemaker.read(88)
        ATR_signal = struct.unpack("d", data[72:80])[0]
        VENT_signal = struct.unpack("d", data[80:88])[0]
        return [ATR_signal, VENT_signal]


def sendToSimulink(mode, lrl, url, AA, APW, AST, VA, VPW, VST, sVRP, sARP, sPVARP, sRS, sMSR, reactionTime,
                   responseFactor, recoveryTime, activityThreshold, HRL):
    ### PLEASE CHANGE THIS VALUE TO WHATEVER PORT IS ON YOUR COMPUTER ###
    ### thank you ###
    modei = struct.pack("B", mode)  # 0-VOO 1-AOO 2-VVI 3-AAI 4-VOOR 5-AOOR 6-VVIR 7-AAIR
    lrli = struct.pack("B", lrl)
    urli = struct.pack("B", url)
    PVARPi = struct.pack("H", sPVARP)
    RSi = struct.pack("B", sRS)
    reaction_timei = struct.pack("H", reactionTime)
    response_factori = struct.pack("B", responseFactor)
    activity_thresholdi = struct.pack("d", activityThreshold)
    # response factor, adctivity threshold
    recovery_timei = struct.pack("H", recoveryTime)
    MSRi = struct.pack("B", sMSR)
    atr_ampi = struct.pack("d", AA)
    atr_pulse_widthi = struct.pack("d", APW)
    ARPi = struct.pack("H", sARP)
    atr_thresholdi = struct.pack("d", AST)
    vent_ampi = struct.pack("d", VA)
    vent_pulse_widthi = struct.pack("d", VPW)
    VRPi = struct.pack("H", sVRP)
    vent_thresholdi = struct.pack("d", VST)
    """
    modei = struct.pack("B", 1)  # 0-VOO 1-AOO 2-VVI 3-AAI 4-VOOR 5-AOOR 6-VVIR 7 VVIR
    lrli = struct.pack("B", 60)
    urli = struct.pack("B", 120)
    PVARPi = struct.pack("H", 100)
    RSi = struct.pack("B", 149)
    reaction_timei = struct.pack("H", 2000)
    response_factori = struct.pack("B", 17)
    activity_thresholdi = struct.pack("d", 1.5)
    # response factori, adctivity threshold
    recovery_timei = struct.pack("H", 2000)
    MSRi = struct.pack("B", 160)
    atr_ampi = struct.pack("d", 3.6)
    atr_pulse_widthi = struct.pack("d", 5)
    ARPi = struct.pack("H", 150)
    atr_thresholdi = struct.pack("d", 3.0)
    vent_ampi = struct.pack("d", 4.1)
    vent_pulse_widthi = struct.pack("d", 5.3)
    VRPi = struct.pack("H", 150)
    vent_thresholdi = struct.pack("d", 2.3)
    """
    # broken up like this for the sake of readability and testing

    Signal_set_order = Start + Fn_set + modei + lrli + urli + PVARPi + RSi + reaction_timei + response_factori + \
                       activity_thresholdi + recovery_timei + MSRi + atr_ampi + atr_pulse_widthi + ARPi + atr_thresholdi \
                       + vent_ampi + vent_pulse_widthi + VRPi + vent_thresholdi

    Signal_echo_order = Start + SYNC + modei + lrli + urli + PVARPi + RSi + reaction_timei + response_factori + \
                        activity_thresholdi + recovery_timei + MSRi + atr_ampi + atr_pulse_widthi + ARPi + atr_thresholdi \
                        + vent_ampi + vent_pulse_widthi + VRPi + vent_thresholdi

    with serial.Serial(frdm_port, 115200) as pacemaker:
        pacemaker.write(Signal_set_order)

    with serial.Serial(frdm_port, 115200) as pacemaker:
        pacemaker.write(Signal_echo_order)
        data = pacemaker.read(88)
        mode_echo = struct.unpack('B', data[0:1])[0]
        lrl_echo = struct.unpack('B', data[1:2])[0]
        url_echo = struct.unpack('B', data[2:3])[0]
        PVARP_echo = struct.unpack("H", data[3:5])[0]
        RS_echo = struct.unpack("B", data[5:6])[0]
        reaction_time_echo = struct.unpack("H", data[6:8])[0]
        response_factor_echo = struct.unpack("B", data[8:9])[0]
        activity_threshold_echo = struct.unpack("d", data[9:17])[0]
        recovery_time_echo = struct.unpack("H", data[17:19])[0]
        MSR_echo = struct.unpack("B", data[19:20])[0]
        atr_amp_echo = struct.unpack("d", data[20:28])[0]
        atr_pulse_width_echo = struct.unpack("d", data[28:36])[0]
        ARP_echo = struct.unpack("H", data[36:38])[0]
        atr_threshold_echo = struct.unpack("d", data[38:46])[0]
        vent_amp_echo = struct.unpack("d", data[46:54])[0]
        vent_pulse_width_echo = struct.unpack("d", data[54:62])[0]
        VRP_echo = struct.unpack("H", data[62:64])[0]
        vent_threshold_echo = struct.unpack("d", data[64:72])[0]
        ATR_signal = struct.unpack("d", data[72:80])[0]
        VENT_signal = struct.unpack("d", data[80:88])[0]

        if mode_echo == mode and lrl_echo == lrl and url_echo == url and PVARP_echo == sPVARP and RS_echo == sRS and reaction_time_echo == reactionTime and response_factor_echo == responseFactor and activity_threshold_echo == activityThreshold and recovery_time_echo == recoveryTime and MSR_echo == sMSR and atr_amp_echo == AA and atr_pulse_width_echo == APW and ARP_echo == sARP and atr_threshold_echo == AST and vent_amp_echo == VA and vent_pulse_width_echo == VPW and VRP_echo == sVRP and vent_threshold_echo == VST:
            return True
        else:
            return False


def read_ecg():
    frdm_port = "COM4"
    Start = b'\x16'
    SYNC = b'\x22'
    Fn_set = b'\x55'
    Signal_echo = Start + SYNC
    i = 0
    while (i < 72):
        Signal_echo = Signal_echo + struct.pack("B", 0)
        i = i + 1
    with serial.Serial(frdm_port, 115200) as pacemaker:
        pacemaker.write(Signal_echo)
        data = pacemaker.read(88)
        ATR_signal = struct.unpack("d", data[72:80])[0]
        VENT_signal = struct.unpack("d", data[80:88])[0]
        return [ATR_signal, VENT_signal]