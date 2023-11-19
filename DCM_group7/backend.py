import json
import sys
import numpy as np
import matplotlib
import serial 

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

            print(data)
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


#test script
if __name__ == "__main__":
    extract_database()
