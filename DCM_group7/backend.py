import json
import sys
import numpy as np
import matplotlib
import serial 
import struct

USERNAME = ""
USERSETTINGS = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
Start = b'\x16'
SYNC = b'\x22'
Fn_set = b'\x55'
comport = "COM8"

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
                USERSETTINGS[0] = user["URL"]
                USERSETTINGS[1] = user["LRL"]
                USERSETTINGS[2] = user["AA"]
                USERSETTINGS[3] = user["VA"]
                USERSETTINGS[4] = user["ARP"]
                USERSETTINGS[5] = user["VRP"]
                USERSETTINGS[6] = user["APW"]
                USERSETTINGS[7] = user["VPW"]
                USERSETTINGS[8] = user["MSR"]
                USERSETTINGS[9] = user["REACT"]
                USERSETTINGS[10] = user["RF"]
                USERSETTINGS[11] = user["RECOVER"]
                USERSETTINGS[12] = user["AT"]
                USERSETTINGS[13] = user["MODE"]
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
    "URL" : 120,
    "LRL" : 60,
    "AA" : 3.5,
    "VA" : 3.5,
    "ARP" : 250,
    "VRP" : 320,
    "APW" :0.4,
    "VPW" : 0.4,
    "MSR": 120,
    "REACT":30,
    "RF": 8,
    "RECOVER": 5,
    "AT": "V-High",
    "MODE" : 1
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
    if (float(settings["LRL"]) !=-1 and float(settings["URL"]) < float(settings["LRL"])):#basic logic limiter since lower limit cant be higher then upper limit
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
            if settings["URL"]!= -1:data[index]["URL"] = int(settings["URL"] )

            if settings["LRL"]!= -1:data[index]["LRL"] = int(settings["LRL"])
            
            if settings["APW"]!= -1:data[index]["APW"] =  float(settings["APW"])
            if settings["AA"]!= -1:data[index]["AA"] = float(settings["AA"])
            
            if settings["VPW"]!= -1:data[index]["VPW"] = float(settings["VPW"])
            if settings["VA"]!= -1:data[index]["VA"] = float(settings["VA"])

            if settings["ARP"]!= -1:data[index]["ARP"] = int(settings["ARP"])
            if settings["VRP"]!= -1:data[index]["VRP"] = int(settings["VRP"])

            if settings["MSR"]!= -1:data[index]["MSR"] = int(settings["MSR"])

            if settings["REACT"]!= -1:data[index]["REACT"] = int(settings["REACT"])

            if settings["RF"]!= -1:data[index]["RF"] = int(settings["RF"])

            if settings["RECOVER"]!= -1:data[index]["RECOVER"] = int(settings["RECOVER"])

            if settings["AT"]!= -1:data[index]["AT"] = settings["AT"]

            if settings["MODE"]!= -1:data[index]["MODE"] = int(settings["MODE"])


            with open("user_data.json", 'w') as json_file:
                json.dump(data, json_file, 
                                    indent=4,  
                                    separators=(',',': '))
            
            print('User Data Saved')
            sendToSimulink(data)    
            return 1, "Success"
        
    
    print("user does not exist, error")
    return 0

'''def createEKG(data_size):
    x = np.random.rand(50)
    y = np.random.rand(50)  
    plt.scatter(x, y, color='blue')'''

# doubles : Activity threshold, atrial amplitude, ventrical amplitude, atrial and ventrical threshold

def sendToSimulink(data):
    data, _ = extract_database()
    for index, user in enumerate(data):
        if user["user_name"] == USERNAME:  # int H double d
            mode = struct.pack("H", data[index]["MODE"])  # int 1-AOO 2-AAI 3-AOOR 4-AAIR 5-VOO 6-VVI 7-VOOR 8-VVIR
            lrl = struct.pack("H", data[index]["LRL"])  #11 int
            url = struct.pack("H", data[index]["URL"])  #11 int
            #PVARP = struct.pack("H", 1) #int
            #av_delay = struct.pack("H", 1) #int 
            reaction_time = struct.pack("H", data[index]["REACT"]) # int11
            response_factor = struct.pack("H",data[index]["RF"]) # int 11
            activity_threshold = struct.pack("d", 1) # double 11
            # response factor, adctivity threshold
            recovery_time = struct.pack("H", data[index]["RECOVER"]) # int 11
            MSR = struct.pack("H", data[index]["MSR"])  #int 11
            atr_amp = struct.pack("d", data[index]["AA"]) # double
            atr_pulse_width = struct.pack("d", data[index]["APW"]) # int
            ARP = struct.pack("H", data[index]["ARP"]) #int
            #atr_threshold = struct.pack("d", 1) #double
            vent_amp = struct.pack("d", data[index]["VA"]) #double
            vent_pulse_width = struct.pack("d",data[index]["VPW"]) #int
            VRP = struct.pack("H", data[index]["VRP"]) #int
            #vent_threshold = struct.pack("d", 1) #double
    # broken up like this for the sake of readability and testing

    Signal_set_order = Start + Fn_set + mode +atr_amp+ atr_pulse_width + ARP  \
                        + vent_amp + vent_pulse_width +  VRP + lrl + url + MSR \
                            + reaction_time +  recovery_time + response_factor + activity_threshold 

    ''' Signal_echo_order = Start + SYNC +  modei +atr_ampi+ atr_pulse_widthi + atr_thresholdi + ARPi + PVARPi \
                        + vent_ampi + vent_pulse_widthi + vent_thresholdi + VRPi + lrli + urli + MSRi \
                            + reaction_timei +  recovery_timei + av_delayi + response_factori + activity_thresholdi''' 

    with serial.Serial(comport, 115200) as pacemaker:
        pacemaker.write(Signal_set_order)
    
    '''with serial.Serial(comport, 115200) as pacemaker:
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
            return False'''



#test script
if __name__ == "__main__":
    extract_database()
