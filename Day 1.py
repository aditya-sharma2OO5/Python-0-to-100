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

# 4.find() - used to find starting index of substring (Also case-sensitive)
print(message.find('World'))

#If we try to find a string of characters, which doesnt exist, it would return -1
print(message.find('Universe'))

# 5.replace() - used to replace some characters in our string with other characters (Also case senstitive)
#Replace() takes 2 arguments, first one is the string we want to replace, 2nd is the one we want to replace it with.
message.replace('World' , 'Universe')
print(message)

#This would still print, Hello World. This happens because replace() doesn't do in-place replacement.
#replace() instead returns a new string with those values replaced.

new_message = message.replace('World' , 'Universe')
print(new_message)

#If we want replacement to the original variable, instead of making a new variable. Just set the original variable.
message = message.replace('World' , 'Universe')
print(message)


#String Concatenation
greeting = 'Hello'
name = 'Micheal'

message = greeting + name
print(message)

#This would print HelloMicheal, as the strings were added but without any space between them.
#To solve this, we add a string literal between them.
message = greeting + ', ' + name
print(message)

#Using the + operator for string concatenation is fine, for smaller and simpler strings. But for a larger and more complicated one.
message = greeting + ', ' + name + '. Welcome!' 

#For strings like these, it's better to use a string formatting.


#String Formatting
#String Formatting allos you to write the message as it will appear and put placeholders in place of variables.
message = '{}, {}. Welcome!'.format(greeting, name)
print(message)

#{} acts as the placeholder for string formatting.


#f-strings
#Introduced in python 3.6 and above, we have access to f-strings.
#Idea behind f-strings is to make string formatting as simple as possible.
message = f'{greeting} , {name}. Welcome!'

#f-strings allow you to write code within the placeholder. So if you wanted the name to be upper case.
message = f'{greeting} , {name.upper()}. Welcome!'
print(message)


#Built-in Documentation
#using the dir() function, and passing a variable name as an arg.
print(dir(name))

#This prints all the attirbutes, methods we have access to with that variable.
#To get more info, about string methods, we can use help() function
#To use help() function, we use the string class instead of the variable name.
print(help(str))

#We can also pass a certain method directly into the help() function.
print(help(str.lower))