import json
import sys
import numpy as np
import matplotlib
import serial 
import struct

USERNAME = ""
USERSETTINGS = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]


def exit_system():
    sys.exit()

def log_in(username, password):
    global USERNAME
    global USERSETTINGS
    
    user_verify = False
    data, _ = extract_database()
    if username == "Enter Username" or username == "" or password == "Enter Password" or password == "":
        print("Missing information, please complete both sections before continuing")
        error_msg = "\tMissing information               "
        return 0, error_msg
    for user in data:
        if user["user_name"] == username:
            user_verify = True
            if user["password"] == password:
                USERNAME = username
                print("log in successful")
                USERSETTINGS[0] = user["AURL"]
                USERSETTINGS[1] = user["VURL"]
                USERSETTINGS[2] = user["ALRL"]
                USERSETTINGS[3] = user["VLRL"]
                USERSETTINGS[4] = user["AA"]
                USERSETTINGS[5] = user["VA"]
                USERSETTINGS[6] = user["ARP"]
                USERSETTINGS[7] = user["VRP"]
                USERSETTINGS[8] = user["APW"]
                USERSETTINGS[9] = user["VPW"]
                USERSETTINGS[10] = user["AMSR"]
                USERSETTINGS[11] = user["VMSR"]
                USERSETTINGS[12] = user["AREACT"]
                USERSETTINGS[13] = user["VREACT"]
                USERSETTINGS[14] = user["ARF"]
                USERSETTINGS[15] = user["VRF"]
                USERSETTINGS[16] = user["ARECOVER"]
                USERSETTINGS[17] = user["VRECOVER"]
                USERSETTINGS[18] = user["AAT"]
                USERSETTINGS[19] = user["VAT"]
                return 1
    
    if user_verify:
        print("incorrect password")
        error_msg = "\tIncorrect password          "
    else:
        print("no matching user name")
        error_msg = "no matching user name"

    return 0, error_msg
    

def register(username, password):
    data, usercount = extract_database()
    if usercount == 10:
        print("too many users, please remove users first")
        error_msg = "Too many users, delete users"
        return 0, error_msg 
    if username == "Enter Username" or username == "" or password == "Enter Password" or password == "":
        print("Missing information, please complete both sections before continuing")
        error_msg = "Missing Information"
        return 0, error_msg
    for user in data:
        if user["user_name"] == username:
            print("user already exists, please log in instead")
            error_msg = "User already exists"
            return 0, error_msg
    
        
    data.append({
    "user_name": username,
    "password": password,
    "AURL" : 120,
    "VURL" : 120,
    "ALRL" : 60,
    "VLRL" : 60,
    "AA" : 3.5,
    "VA" : 3.5,
    "ARP" : 250,
    "VRP" : 320,
    "APW" :0.4,
    "VPW" : 0.4,
    "AMSR": 120,
    "VMSR": 120,
    "AREACT":30,
    "VREACT":30,
    "ARF": 8,
    "VRF": 8,
    "ARECOVER": 5,
    "VRECOVER": 5,
    "AAT": "V-High",
    "VAT": "V-High"
    })
    
    with open("user_data.json", 'w') as json_file:
        json.dump(data, json_file, 
                            indent=4,  
                            separators=(',',': '))
    
    print('Successfully registered, please try logging in')
    return 1, "Success"

def extract_database():
    # user JSON load in 
    user_data = open('user_data.json')
    interperated_user_data = json.load(user_data)
    usercount = len(interperated_user_data)
    return interperated_user_data, usercount

'''
URL: upper rate limit
LRL: Lower rate limit
APW: Atrium Pulse Width
AA: Atrium Amplitude
RS: Rate Smoothing
AS:  Atrial Sensitivity
ARR: Atrial Refractory Period
'''

def verifyInput(settings):
    global USERNAME
    if (float(settings["ALRL"]) !=-1 and float(settings["AURL"]) < float(settings["ALRL"])) or \
        (float(settings["VLRL"]) !=-1 and float(settings["VURL"]) < float(settings["VLRL"])):#basic logic limiter since lower limit cant be higher then upper limit
        print("Lower Rate Limit Cannot Be Higher Than the Upper Rate Limit")
        error_msg = "LRL cannot be greater than URL"
        return 0, error_msg
    else:
        print("pass")
        saveData(USERNAME, settings)
        return 1, "SUCCESS"
    

def saveData(username, settings):
    data, _ = extract_database()
    print(username)
    for index, user in enumerate(data):
        if user["user_name"] == username:
            if settings["AURL"]!= -1:data[index]["AURL"] = settings["AURL"]
            if settings["VURL"]!= -1:data[index]["VURL"] = settings["VURL"]

            if settings["ALRL"]!= -1:data[index]["ALRL"] = settings["ALRL"]
            if settings["VLRL"]!= -1:data[index]["VLRL"] = settings["VLRL"]
            
            if settings["APW"]!= -1:data[index]["APW"] = settings["APW"]
            if settings["AA"]!= -1:data[index]["AA"] = settings["AA"]
            
            if settings["VPW"]!= -1:data[index]["VPW"] = settings["VPW"]
            if settings["VA"]!= -1:data[index]["VA"] = settings["VA"]

            if settings["ARP"]!= -1:data[index]["ARP"] = settings["ARP"]
            if settings["VRP"]!= -1:data[index]["VRP"] = settings["VRP"]

            if settings["AMSR"]!= -1:data[index]["AMSR"] = settings["AMSR"]
            if settings["VMSR"]!= -1:data[index]["VMSR"] = settings["VMSR"]

            if settings["AREACT"]!= -1:data[index]["AREACT"] = settings["AREACT"]
            if settings["VREACT"]!= -1:data[index]["VREACT"] = settings["VREACT"]

            if settings["ARF"]!= -1:data[index]["ARF"] = settings["ARF"]
            if settings["VRF"]!= -1:data[index]["VRF"] = settings["VRF"]

            if settings["ARECOVER"]!= -1:data[index]["ARECOVER"] = settings["ARECOVER"]
            if settings["VRECOVER"]!= -1:data[index]["VRECOVER"] = settings["VRECOVER"]

            if settings["AAT"]!= -1:data[index]["AAT"] = settings["AAT"]
            if settings["VAT"]!= -1:data[index]["VAT"] = settings["VAT"]

            with open("user_data.json", 'w') as json_file:
                json.dump(data, json_file, 
                                    indent=4,  
                                    separators=(',',': '))
            
            print('User Data Saved')
            return 1, "Success"
    
    print("user does not exist, error")
    return 0

'''def createEKG(data_size):
    x = np.random.rand(50)
    y = np.random.rand(50)  
    plt.scatter(x, y, color='blue')'''

def sendToSimulink(mode, data, ser):
    data, _ = extract_database()
    for index, user in enumerate(data):
        if user["user_name"] == USERNAME:
            modei = struct.pack("B", mode)  # 0-VOO 1-AOO 2-VVI 3-AAI 4-VOOR 5-AOOR 6-VVIR 7-AAIR
            lrli = struct.pack("B", data[index]["ALRL"])  #11
            urli = struct.pack("B", data[index]["AURL"])  #11
            PVARPi = struct.pack("H", sPVARP)
            RSi = struct.pack("B", sRS)
            reaction_timei = struct.pack("H", data[index]["AREACT"]) #11
            response_factori = struct.pack("B", responseFactor)
            activity_thresholdi = struct.pack("d", data[index]["AAT"]) #11
            # response factor, adctivity threshold
            recovery_timei = struct.pack("H", data[index]["ARECOVER"]) #11
            MSRi = struct.pack("B", data[index]["AMSR"])  #11
            atr_ampi = struct.pack("d", data[index]["AA"])
            atr_pulse_widthi = struct.pack("d", data[index]["APW"])
            ARPi = struct.pack("H", data[index]["ARP"])
            atr_thresholdi = struct.pack("d", AST)
            vent_ampi = struct.pack("d", data[index]["VA"])
            vent_pulse_widthi = struct.pack("d",data[index]["VPW"])
            VRPi = struct.pack("H", data[index]["VRP"])
            vent_thresholdi = struct.pack("d", VST)
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



#test script
if __name__ == "__main__":
    extract_database()
