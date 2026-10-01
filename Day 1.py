#We will learn about strings. 
#This corresponds to video 2 of the python playlist.

#keep variable names as descriptive as possible
message = 'Hello World'

#message is our variable which holds our textual data and this textual data is called a string.
#We can use this variblae instead of this textual data in our code.

print(message)

#Strings can be created by either using simple quotes ('') or double quotes ("").
#Depending on what type of textual data you have, you can use either or the two.
#If you have, a single quote in the text data

#message = 'bobby's World'

#In this string, the ' before the s completes the string, this throws an error. Ways to mitigate these
# 1. Escape single quote with a backslash
message = 'Bobby \'s World'         #This causes python, to know the single quote before s doesnt close the string.

# 2. Simply use double quotes ("") at the beginning & end of the string.
message = "Booby's World"

#Similarly if text contains double quotes, use single quotes at beginning and end of the string.
