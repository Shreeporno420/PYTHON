import random
import colorama
from colorama import *
colorama.init()

words=["about","Python","Javascript","Tutorial","Video","capture","Scratch","Computer","Different","Difficult","Genius","Secret","Hacking","Coding"]

#with open("wordList.txt","r") as f: 
#    words=f.readlines()

word=random.choice(words)[:-1]
allowed_errors=7
guesses=[] 
done= False

while not done:
    for letter in word:
        if letter.lower() in guesses:
            print(letter,end="_")
        else:
            print("_",end=" ") 
    
    print("")

    guess=input(f"Allowed Errors left {allowed_errors}, Next Guess: ")
    guesses.append(guess.lower()) 
    if guess.lower() not in word.lower():
        allowed_errors -= 1
        if allowed_errors == 0:
            break

    done= True
    for letter in word:
        if letter.lower() not in guesses:
            done = False

if done:
    print(f"You found the word! The word in "+Fore.BLUE+word)   

else:
    print(f"Game Over! The word in "+Fore.RED+word) 