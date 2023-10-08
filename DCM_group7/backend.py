import json
import logging
import sys

def exit_system():
    sys.exit()

def log_in(username, password):
    data, _ = extract_database()
    if username == "Enter Username" or username == "" or password == "Enter Password" or password == "":
        print("Missing information, please complete both sections before continuing")
        error_msg = "Unsuccessful Login"
        return 0, error_msg
    for user in data:
        if user["user_name"] == username and user["password"] == password:
            print("log in successful")
            return 1
    
    print("no matching data avaiable")
    error_msg = "No match"
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

<<<<<<< HEAD
def verifyInput(URL, LRL, APW=None, AA=None, RS=None, AS=None, ARR=None, VPW=None, VA=None, VS=None, VRR=None):
    if URL < LRL:  #basic logic limiter since lower limit cant be higher then upper limit
        print("Lower Rate Limit Cannot Be Higher Than the Upper Rate Limit")
        error_msg = "LRL cannot be greater than URL"
        return 0
    elif LRL < 30 or LRL > 175:
        print("LRL out of bounds")
    elif URL <50 or URL > 175:
        print("URL out of bounds")
=======
def verifyInput(URL, LRL, APW=-1, AA=-1, RS=-1, AS=-1, ARR=-1, VPW=-1, VA=-1, VS=-1, VRR=-1):
    #package to float for comparison
    apw = float(APW)
    vpw = float(VPW)
    aa = float(AA)
    va = float(VA)
    rs = float(RS)
    asense = float(AS)
    vsense = float(VS)
    arr = float(ARR)
    vrr = float(VRR)

    #data sheet adheration 
    #actually, the ui's bounds set the limiters for the specific values. we just need to be ware of logical ones
    #if 30 >= LRL >= 175: print("LRL out of bounds") #lrl check
    #elif 50 >= URL >= 175: print("URL out of bounds") #url check
    #elif 0.05 >= apw >= 1.9 or 0.05 >= vpw >= 1.9: print("pulse width our of bounds")
    if URL < LRL: 
        print("Lower Rate Limit Cannot Be Higher Than the Upper Rate Limit") #basic logic limiter since lower limit cant be higher then upper limit
        return 0 #return 0 if it didnt pass
>>>>>>> eddy
    else:
        print("pass")
        return 1
    
#input values are now all float instead of string. package data for simulink
def packageData(URL, LRL, APW=-1, AA=-1, RS=-1, AS=-1, ARR=-1, VPW=-1, VA=-1, VS=-1, VRR=-1):
    return 0
    

# for preperation of serical communication
def sendToDevice(data):
    return 0 
#test script
if __name__ == "__main__":
    extract_database()
