# Scoring or Grading System
# Take user Input
# Score them according average marks A++(90-100), A+(75-89), A(60-74), B(45-59), C(30-44),D(0-29)

grade=int(input("Enter your Grade "))

if grade >= 90 and grade <= 100:
    print("You Got A++") 

elif grade >= 75 and grade <=89:
    print("You got A+")

elif grade >= 60 and grade <= 74:
    print("You got A")  

elif grade >= 45 and grade <=59:
    print("You got B")

elif grade >= 30 and grade <= 44:
    print("You got C")  

elif grade <= 29: 
    print("You got D")   

elif grade > 100:
    print("Value Error!!!")
