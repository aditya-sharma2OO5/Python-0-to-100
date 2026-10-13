# We will learn about Conditionals and Booleans.
# Corresponds to video 5 of python playlist

# We will learn about conditionals, and how to control which statements to execute, depending on if they evaluate to True or False (Boolean values)
# Let's look at the simplest conditional
if True:
    print('Conditional was True')       #This statement will be executed

if False:
    print('conditional was False')      #This will not be executed.

# The first if block was executed and not the second block, this is because when the condition is True python executes the indented print statement. When the condition is Flase, python skips the indented print statement.
# Conditionals are not hardcoded to have True or False values, we want a code that evaluates to either True or False.

language = 'Python'
if language == 'Python':
    print('Conditional was True')

##Comparision Operators

# 1.Equal : ==
# 2.Not equal : !=
# 3.Grater than : >
# 4.Less than : <
# 5.Greater or Equal to : >=
# 6.Less or Equal to : <=
# 7.Object Identify : is

# Object identify is used to check whether values have same ID or whether they're same object in memory

# Let's look at Else statements, they are used when we want to execute one portion of our code if conditional evaluates to false.

language = 'Jave'

if language == 'Python':
    print('Language is Python')
else:
    print('No Match')

# What if we wanted to check for multiple languages and execute differeent code for each one we encounter, we could use Elif for this.
# Let's check if the language is equal to python, java or if not equal to any of the two then print 'No Match'.
language = 'C++'

if language == 'Python':
    print('Language is Python')
elif language == 'Java':
    print('Language is Java')
else:
    print('No Match')

# Python doesn't have Switch case statement. If we wanted to check for multiple languages, we could keep adding elif statements.

##Boolean Operations
user = 'Admin'
logged_in = True

# We only want to execute some code, user is Admin and looged in. For this we could use the and keyword.
if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Invalid Credentials')




