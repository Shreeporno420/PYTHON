import colorama
from colorama import *
colorama.init()
while True:  
    string = input(Fore.WHITE+"Enter a string: ")
    
    if len(string) % 2 != 0:
        print(Fore.RED+"First word:",string[0])

        mid = int(len(string)/2)
        print(Fore.YELLOW+"Middle word:",string[mid])

        last = len(string)-1
        print(Fore.CYAN+"Last word:",string[last])
        
        condition = int(input(Fore.WHITE+"Do you want to continue? 1.continue or 2.stop: "))

        if condition == 1:
            continue
        else:
            print(Fore.BLUE+"Thanks For use!")
            break

    elif len(string) % 2 == 0:
        print(Fore.RED+"First word:",string[0])

        last = len(string)-1
        print(Fore.GREEN+"Last word:",string[last])
        
        condition = int(input(Fore.WHITE+"Do you want to continue? 1.continue or 2.stop: "))

        if condition == 1:
            continue
        else:
            print(Fore.BLUE+"Thanks For use!")
            break

    break