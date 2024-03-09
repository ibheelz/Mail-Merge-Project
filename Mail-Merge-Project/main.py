#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

import os

name_content = open ("Mail-Merge-Project/Input/Names/invited_names.txt")
names = (name_content.readlines())

for i in range(len(names)):
    names[i]=names[i].replace('\n','')

letter_content = open ("Mail-Merge-Project/Input/Letters/starting_letter.txt")
letter = (letter_content.read())

for i in names:
    x = letter.replace("[name]", i)
    y = open(f"Mail-Merge-Project/Output/ReadyToSend/{i}.txt", "w")
    z = y.write(x)
  

# print(letter)
