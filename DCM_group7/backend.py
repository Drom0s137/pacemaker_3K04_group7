import json
import logging


def main():
    # user JSON load in 
    user_data = open('user_data.json')
    y = json.load(user_data)
    print(y["user_name"])

    # user entry
    username = input("Enter username:")
    return 0




if __name__ == "__main__":
    main()
