#Weight Converter
from time import sleep
while True:
    option=int(input("Do you want to start: 1.Yes or 2.No => "))
    if option == 1:
        unit=int(input("Which unit you want to convert: 1.kilogram to gram, 2. Gram to kilogram, 3.Kilograms to pound, 4.kilogram to tons, 5.milligram to gram: "))
        if unit == 1:
            num1=int(input("Enter the Kilogram amount: "))
            sleep(1)
            result= num1 * 1000
            print("result:", result,'gram')
            break
        
        if unit == 2:
            num1=int(input("Enter the Gram amount: "))
            sleep(1)
            result= num1 / 1000
            print("result:", result,'kilogram')
            break
        
        if unit == 3:
            num1=int(input("Enter the Kilogram amount: "))
            pound= 2.20462
            sleep(1)
            result= num1 * pound
            print("result:", result,'pound')
            break

        if unit == 4:
            num1=int(input("Enter the Kilogram amount: "))
            sleep(1)
            result= num1 / 1000
            print("result:", result,'ton')
            break

        if unit == 5:
            num1=int(input("Enter the milligrams amount: "))
            sleep(1)
            result= num1 / 1000
            print("result:", result,'gram')
            break        

    if option == 2:
        print("Thanks") 
        break