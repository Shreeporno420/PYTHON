import colorama
from colorama import *
colorama.init()
num1 = int(input("Enter first number: "))
condition = input("What mathematical operator Would you like to use: \n\t\t+ for addition,\n\t\t- for substraction, \n\t\t* for multiplication,\n\t\t/ for diviition,\n\t\t% for Modulus, \n\t\t** for the power oparator \n\t\t")
num2 = int(input("Enter second number: "))

if condition == "+":
    print("result: ",num1+num2)
elif condition == "-":
    print("result: ",num1-num2)
elif condition == "*":
    print("result: ",num1*num2)
elif condition == "/":
    print("result: ",num1/num2)
elif condition == "%":
    print("result: ",num1&num2)
elif condition == "**":
    print("result: ",num1**num2)
else:
    print(Fore.RED+"You Choose Invalid Option!")