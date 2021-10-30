## Create a Simple File System 
## Creation, Writng data, Modifying File Data, Reading Data.
import time
import colorama
from colorama import *
colorama.init()
option=int(input(Fore.WHITE+"Enter Option: 1.File creation, 2.Modifying File Data, 3.Writing Data, 4.Delete File, 5.Stop Program: "))

while True:
    #Flie Cretaion
    if option == 1:
        FileName=input("Enter File name: ") 
        print(Fore.GREEN+"processing...")
        time.sleep(0.5)
        with open(f"{FileName}.txt", mode="w") as f:
            print(Fore.WHITE+"File Creation Done!")
            break
   
    #Modify Flie Data
    elif option == 2:
        FileName=input("Enter File name: ") 
        with open(f"{FileName}.txt", mode="a") as f:
            data=input("Enter Data: ")
            print(Fore.GREEN+"processing...")
            time.sleep(0.5)
            f.write(f"{data}")
            break
    
    #Writing Data
    elif option == 3:
        FileName=input("Enter File name: ") 
        with open(f"{FileName}.txt", mode="w") as f:
            data=input("Enter Data: ")
            print(Fore.GREEN+"processing...")
            time.sleep(0.5)
            print("Done!")
            f.write(f"{data}")        
            break

    #Delete File
    elif option == 4:
        FileName=input("Enter File name: ") 
        import os
        os.remove(f"{FileName}.txt")
        break

    #Stop Program
    elif option == 5:
        print(Fore.LIGHTRED_EX+"Program Break")
        break

    else:
        print(Fore.RED+"Invalid option!!!")
        break