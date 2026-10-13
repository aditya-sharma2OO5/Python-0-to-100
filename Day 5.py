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

# And Operator - We only want to execute some code if all conditions are true, user is Admin and looged in.
if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Invalid Credentials')

# Or Operator - If we only care about one conditon out of multiple conditions are true, for the code to be executed we use 'or' keyword.

logged_in = False
if user == 'Admin' or logged_in:
    print('Admin Page')
else:
    print('Invalid Credentials')

# Not Operator - Switch boolean values, switches True to False and vice versa.
if not logged_in:
    print('Please Log in')
else:
    print('Hello')


##Object Identity
# Checks if two objects have same ID, which basically means if they are the same object in memory. Two objects can be equal but not be the same object in memory.

a = [1, 2, 3]
b = [1, 2, 3]

# When executed would return true, since the two lists are true
print(a == b)   
# This would return False, as they are two different objects in memory. 
print(a is b)

# We can also print the location of these objects in memory using a built-in function id()
print(id(a))
print(id(b))

# If a and b refer to the same object, then 'a is b' would return true.
b = a
print(a is b)


##Let's now understand, what all things python evaluates to True or False. We will look at False, and everything that doesn't evaluate to False would evaluate to True.

# False Values
    #False
    # None
    # Zero of any numeric type
    # Any empty sequence, for example '', [], () etc
    # Any empty mapping, for example {}

condition = False
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

condition = None
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

condition = 0
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

condition = []
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

condition = {}
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')


##There are also some user defined classes that can evaluate to False.

# 1. Using bool() to return False
class MyClass: 
    def __bool__(self): 
        return False

condition = MyClass()
if condition: 
    print('Evaluated to True') 
else: 
    print('Evaluated to False')

# 2. Using len() to return 0
# If bool() is not defined, Python checks len().
# If len() returns 0, the object evaluates to False.
class MyClass: 
    def __len__(self): 
        return 0

condition = MyClass()
if condition: 
    print('Evaluated to True') 
else: 
    print('Evaluated to False')

# 3. If neither __bool__() nor __len__() is defined, the object evaluates to True by default.
class MyClass: 
    pass

condition = MyClass()
if condition: 
    print('Evaluated to True') 
else: 
    print('Evaluated to False')

# bool() and len() are built-in Python functions.
# bool(obj) determines whether an object evaluates to True or False.
# len(obj) returns the length of an object.

# __bool__() and __len__() are special methods also called a magic method or dunder method that a class can define.
# __bool__() customizes an object's truth value and must return True or False. Returning any other type raises a TypeError.
# __len__() is a special method that a class can define to specify the length of its instances. Must return a non negative integer, otherwise it raise a TypeError.

# When evaluating an object in a Boolean context, Python checks if __bool__() is defined, and if it is uses __bool__() first. 
# If it is not defined, Python checks __len__() if available.
# If __len__() returns 0, the object evaluates to False; otherwise, it evaluates to True. 
# If neither method is defined, the object evaluates to True by default.

# bool(obj) determines the truth value of an object.
# It checks __bool__() first and falls back to __len__() if necessary.

# len(obj) requests the object's length by calling __len__().
# It does not call __bool__() to determine the length.

# Defining bool() or len() inside a class does not replace __bool__() or __len__(), because these are different method names.
