#Take input of a word
string = input("Please enter your own word or sentence : ")

#take input of a character
char = input("Pleas enter your own Character : ")

i = 0
count = 0

#loop will find the occurence of character
while(i < len(string)): #string operation
    if(string[i] == char): #check each letter of the word whether it'sthe same as the charecter we want to find
        count = count + 1

    i = i + 1 

print("The total Number ",char, "character has occurred = ",count, "times")