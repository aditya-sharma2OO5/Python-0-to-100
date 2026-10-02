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

#Multi Line quotes
#For multi line quotes, use triple quotes (''' ''') at the starting & end of the message.
#These triple quotes, can be single quotes (''' ''') or double quotes (""" """)

#Think of strings as a string of individual characters & we can access these characters as well.
#Use len() func to find out how many characters a string has.
message = 'Hello World'
print(len(message))

#This would print 11 = Hello (5) + World (5) + Spacebar 


#To access each character we can use square brackets after the string and pass in location of the character we want.
print(message[0])

#0 represents the index, we are trying to print.

#Range of index - 0 to N-1, N being length of the string.
#If we try to access a index that doesn't exist, we get an IndexError: string index out of range.
#print(message[11])

#We can also access a range of characters.
print(message[0:5])         #First index is starting index, last one is stopping index.

#Starting index is inclusive, but stopping index is not.
#If we leave the starting index as empty, python assumes we want to start from the beginning.
print(message[:5])

#Similarly, if we leave the stopping index as empty, python assumes we want to go till the end.
print(message[0:])

#This is know as slicing.


#Methods are function that belongs to an object.
#String Methods.
# 1.lower() - converts the whole string to lower case.
print(message.lower())

# 2.upper() - converts the whole string to upper case
print(message.upper())

# 3.count() - gives the no. of times a particular char, appears in a string
#This takes string as an argument.
print(message.count('Hello'))

#count() method is case sensitive when used with strings.
print(message.count('L'))       #This would give 0
