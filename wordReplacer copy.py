word=input("Enter word: ") 
replace_word=input("Enter replacer word: ") 

replace=word.replace(f"{word}", f"{replace_word}")

print("replacing:",replace)  