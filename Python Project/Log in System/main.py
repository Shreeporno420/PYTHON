import re
import colorama
from colorama import *
colorama.init()

color = Fore.WHITE
while True:
    #User Name
    color = Fore.WHITE
    user_name = input(color+"Enter User Name: ")
    if re.findall(r'^[A-Za-z]',user_name) and len(user_name) > 2:
        color = Fore.GREEN
        print(color+"Correct User Name!")
        
        while True:
            #password
            color = Fore.WHITE
            password = input(color+"Enter Your Password: ")
            if re.findall(r'[A-Za-z][0-9]',password) and int(len(password)) > 5:
                color = Fore.GREEN
                print(color+"Correct Password!")

                while True:
                    # Confirm Password
                    color = Fore.WHITE
                    confirm_password = input(color+"Confirm Password: ")
                    if confirm_password == password:
                        color = Fore.GREEN
                        print(color+"Password Confirm!")
                        color = Fore.BLUE
                        print(color+"File send!")

                        #Creating text information file
                        with open("information.txt", mode="w") as f:
                            f.write(f"Your User Name: {user_name}\nPassword: {password}")
                    else:
                        color = Fore.RED
                        print(color+"Password Didn,t Match!")
                        continue

            else:
                if len(password) < 5:
                    color = Fore.RED
                    print(color+"Password Length Small!")
                    continue
                
                else:
                    color = Fore.RED
                    print(color+"Password Incorrect!")
                    continue
    else:
        color = Fore.RED
        print(color+"User Name Incorrect!")
        continue