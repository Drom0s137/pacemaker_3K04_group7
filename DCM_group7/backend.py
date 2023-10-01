import json
import logging
import sys

def exit_system():
    sys.exit()

def log_in(username, password):
    data = extract_database()
    if username == "Enter Username" or password == "Enter Password":
        print("Missing information, please complete both sections before continuing")
        return 0
    for user in data:
        if user["user_name"] == username and user["password"] == password:
            print("log in successful")
            return 1
    
    print("no matching data avaiable")
    return 0
    

def register(username, password):
    data = extract_database()
    if username == "Enter Username" or password == "Enter Password":
        print("Missing information, please complete both sections before continuing")
        return 0
    for user in data:
        if user["user_name"] == username:
            print("user already exists, please log in instead")
            return 0
    
        
    data.append({
    "user_name": username,
    "password": password,
    })
    
    with open("user_data.json", 'w') as json_file:
        json.dump(data, json_file, 
                            indent=4,  
                            separators=(',',': '))
    
    print('Successfully registered, please try logging in')
    return 1

def extract_database():
    # user JSON load in 
    user_data = open('user_data.json')
    return json.load(user_data)
    print(data[0]["user_name"])

'''
URL: upper rate limit
LRL: Lower rate limit
APW: Atrium Pulse Width
AA: Atrium Amplitude
RS: Rate Smoothing
AS:  Atrial Sensitivity
ARR: Atrial Refractory Period
'''

def verifyInput(URL, LRL, APW=None, AA=None, RS=None, AS=None, ARR=None, VPW=None, VA=None, VS=None, VRR=None):
    if URL < LRL:
        print("error with input values, please try again")
        return 0 
    else:
        return 1
    
if __name__ == "__main__":
    extract_database()
