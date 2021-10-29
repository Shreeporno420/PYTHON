# Design Program for Smart Door
# originalPassword = "open@2021"
# Will take user input as password
# if password is same as original password, show door is opening, Try again
# maxTry = 3, after that if enters wrong password, Door is locked. will stop
# resetting password.
import colorama
from colorama import *
colorama.init() 
originalPassword = "open@2021"
your_try=0
max_try=3
color=Fore.WHITE
while True:
    color=Fore.WHITE
    option=int(input(color+"Choose option: 1.Enter Password, 2.Reset Password: "))
    #Taking Password
    if option == 1:
        while True:
                color=Fore.WHITE 
                password= input(color+"Enter Password: ")
                your_try += 1
                if password == originalPassword:
                    color=Fore.GREEN
                    print(color+"door is opening") 
                    break
                elif  your_try == max_try:
                    color=Fore.RED
                    print(color+"Door Locked! You are a Robber")
                    break
                else:
                    color=Fore.RED
                    print(color+"Password Incorrect!")
                    continue
        break
    #Reset Password
    elif option == 2:
            color=Fore.WHITE
            new_password=input(color+"Enter old password: ")
            if new_password == originalPassword:
                    color=Fore.GREEN 
                    print(color+"Your Old password is Correct") 
                    color=Fore.WHITE 
                    new_password1=input(color+"Enter New password: ")
                    new_password2=input(color+"Confirm password Again: ")  
                    if new_password1 == new_password2:
                        color=Fore.GREEN
                        print(color+"Password Reset done!")
                        originalPassword = new_password2
                    else:
                        color=Fore.RED
                        print(color+"Your password isn,t correct") 
                        continue
            else:
                color=Fore.RED
                print(color+"Your Old password isn,t correct") 
                continue               