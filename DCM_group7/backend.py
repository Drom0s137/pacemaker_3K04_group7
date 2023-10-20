import json
import logging
import sys

USERNAME = ""
USERSETTINGS = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]

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
                USERSETTINGS[1] = user["LRL_AOO"]
                USERSETTINGS[2] = user["LRL_VOO"]
                USERSETTINGS[3] = user["LRL_AAI"]
                USERSETTINGS[4] = user["LRL_VVI"]
                USERSETTINGS[5] = user["AA_AOO"]
                USERSETTINGS[6] = user["AA_AAI"]
                USERSETTINGS[7] = user["VA_VOO"]
                USERSETTINGS[8] = user["VA_VVI"]
                USERSETTINGS[9] = user["ARP"]
                USERSETTINGS[10] = user["VRP"]
                USERSETTINGS[11] = user["APW"]
                USERSETTINGS[12] = user["VPW"]
                print(user)
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
    "LRL_AOO" : 60,
    "LRL_VOO" : 60,
    "LRL_AAI" : 60,
    "LRL_VVI" : 60,
    "AA_AOO" : 3.5,
    "AA_AAI" : 3.5,
    "VA_VOO" : 3.5,
    "VA_VVI" : 3.5,
    "ARP" : 250,
    "VRP" : 320,
    "VPW" : 0.4,
    "APW" :0.4
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

def verifyInput(URL, LRL_AOO=-1, LRL_VOO=-1, LRL_AAI=-1, LRL_VVI=-1, APW=-1, AA_AOO=-1, AA_AAI=-1, ARP=-1, VPW=-1, VA_VOO=-1, VA_VVI=-1, VRP=-1):
    global USERNAME
    if (float(LRL_AOO) !=-1 and URL < float(LRL_AOO)) or (float(LRL_VOO) !=-1 and URL < float(LRL_VOO))\
          or (float(LRL_AAI) !=-1 and URL < float(LRL_AAI)) or (float(LRL_VVI) !=-1 and URL < float(LRL_VVI)):#basic logic limiter since lower limit cant be higher then upper limit
        print("Lower Rate Limit Cannot Be Higher Than the Upper Rate Limit")
        error_msg = "LRL cannot be greater than URL"
        return 0, error_msg
    else:
        print("pass")
        saveData(USERNAME, URL, LRL_AOO=LRL_AOO, LRL_VOO=LRL_VOO, LRL_AAI=LRL_AAI, LRL_VVI=LRL_VVI, APW=APW, AA_AOO=AA_AOO, AA_AAI=AA_AAI, ARP=ARP, VPW=VPW, VA_VOO=VA_VOO, VA_VVI=VA_VVI, VRP=VRP)
        return 1, "SUCCESS"
    

def saveData(username, URL, LRL_AOO=-1, LRL_VOO=-1, LRL_AAI=-1, LRL_VVI=-1, APW=-1, AA_AOO=-1, AA_AAI=-1, ARP=-1, VPW=-1, VA_VOO=-1, VA_VVI=-1, VRP=-1):
    data, _ = extract_database()
    print(username)
    for index, user in enumerate(data):
        if user["user_name"] == username:
            data[index]["URL"] = URL
            if LRL_AOO!= -1:data[index]["LRL_AOO"] = LRL_AOO
            if LRL_VOO!= -1:data[index]["LRL_VOO"] = LRL_VOO
            if LRL_AAI!= -1:data[index]["LRL_AAI"] = LRL_AAI
            if LRL_VVI!= -1:data[index]["LRL_VVI"] = LRL_VVI
            if APW!= -1:data[index]["APW"] = APW
            if AA_AOO!= -1:data[index]["AA_AOO"] = AA_AOO
            if AA_AAI!= -1:data[index]["AA_AAI"] = AA_AAI
            if ARP!= -1:data[index]["ARP"] = ARP
            if VPW!= -1:data[index]["VPW"] = VPW
            if VA_VOO!= -1:data[index]["VA_VOO"] = VA_VOO
            if VA_VVI!= -1:data[index]["VA_VVI"] = VA_VVI
            if VRP!= -1:data[index]["VRP"] = VRP

            with open("user_data.json", 'w') as json_file:
                json.dump(data, json_file, 
                                    indent=4,  
                                    separators=(',',': '))
            
            print('User Data Saved')
            return 1, "Success"
    
    print("user does not exist, error")
    return 0
    


#input values are now all float instead of string. package data for simulink
def packageData(URL, LRL, APW=-1, AA=-1, RS=-1, AS=-1, ARP=-1, VPW=-1, VA=-1, VS=-1, VRP=-1):
    return 0
    

# for preperation of serical communication
def sendToDevice(data):
    return 0 

#test script
if __name__ == "__main__":
    extract_database()
