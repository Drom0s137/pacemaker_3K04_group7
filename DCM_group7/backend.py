import json
import logging
import sys

def exit_system():
    sys.exit()

def log_in(username, password):
    user_verify = False
    data, _ = extract_database()
    if username == "Enter Username" or username == "" or password == "Enter Password" or password == "":
        print("Missing information, please complete both sections before continuing")
        error_msg = "\tMissing information\t"
        return 0, error_msg
    for user in data:
        if user["user_name"] == username:
            user_verify = True
            if user["password"] == password:
                print("log in successful")
                return 1
    
    if user_verify:
        print("incorrect password")
        error_msg = "\tIncorrect password\t"
    else:
        print("no matching user name")
        error_msg = "\tno matching user name\t"
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

def verifyInput(URL, LRL, APW=None, AA=None, RS=None, AS=None, ARP=None, VPW=None, VA=None, VS=None, VRP=None):
    if URL < LRL:  #basic logic limiter since lower limit cant be higher then upper limit
        print("Lower Rate Limit Cannot Be Higher Than the Upper Rate Limit")
        error_msg = "LRL cannot be greater than URL"
        return 0, error_msg
    # elif LRL < 30 or LRL > 175: # These are useless. UI blockes them anyways.
    #     print("LRL out of bounds")
    # elif URL <50 or URL > 175:
    #     print("URL out of bounds")
    else:
        print("pass")
        return 1, "SUCCESS"
    
#input values are now all float instead of string. package data for simulink
def packageData(URL, LRL, APW=-1, AA=-1, RS=-1, AS=-1, ARP=-1, VPW=-1, VA=-1, VS=-1, VRP=-1):
    return 0
    

# for preperation of serical communication
def sendToDevice(data):
    return 0 
#test script
if __name__ == "__main__":
    extract_database()
