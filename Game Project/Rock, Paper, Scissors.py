import random
import colorama
from colorama import *
colorama.init()
letter=["r","p","s"] 
point=0
#Main Game
while True:
    #Declare Variable
    option=input(Fore.WHITE+"Rock(r), Paper(p), Scissors(s): ")
    if option in letter:
        computer_option=random.randint(1,3)
        computer=""
        condition=[option == "r",
                   option == "p",
                   option == "s"
                  ]
        if any(option):
            process= "Y"

        if process == "Y" and computer_option == 1:
            computer="r"

        if process == "Y" and computer_option == 2:
            computer="p"

        if process == "Y" and computer_option == 3:
            computer="s"

        if option == computer:
            correct="Y"
            print(Fore.WHITE+"Player"+Fore.GREEN+" win!") 
            break

        if option != computer:
            correct="Y"
            print(Fore.WHITE+"Computer"+Fore.RED+" win!") 
            break

    break