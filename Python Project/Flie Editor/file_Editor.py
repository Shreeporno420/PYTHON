## Create a Simple File System 
## File Creation, Writng data, Modifying File Data, Delete File.
option=int(input("option: 1.File Creation, 2.Writng data, 3.Modifying File Data, 4.Delete File: "))

while True:
    if option == 1:
        FileName=input("Enter File Name: ")
        with open(f"{FileName}.txt",mode="w"):
            print("File Creation Done!")
            break
    
    elif option == 2:
        FileName=input("Enter File Name: ")
        with open(f"{FileName}.txt",mode="w") as f:
            data=input("Enter data: ")
            f.write(f"{data}")
            print("Done!")
            break

    elif option == 3:
        FileName=input("Enter File Name: ")
        with open(f"{FileName}.txt",mode="a") as f:
            data=input("Enter Data: ")
            f.write(f+" "+"{data}")
            print("Modify Done!")
            break

    elif option == 4:
        FileName=input("Enter File Name: ")
        import os
        os.remove(f"{FileName}.txt")
        print("File Remove!") 
        break
    
    else:
        print("Wrong Option!")
        break