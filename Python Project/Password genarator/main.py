import random
import colorama
colorama.init() 

# Variables
character = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234556789[]{_!#}"
how_many_password = int(input("How many password you want: ")) 
length = int(input("Enter password Length: "))  

# File creation
f = open("Information.txt", mode="w")

#Getting random password
for i in range(how_many_password):
    password = ""
    for c in range(length):
        password += random.choice(character)   

    # Writing Data 
    f.writelines(password+" |")  

    print(password)