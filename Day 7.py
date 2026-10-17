# We will learn about functions
# Corresponds to video 8 of python playlist.

# Functions are basically instructions packaged together that perform a particular action/task.
# Created using a def (defination) keyword
def hello_func():
    pass

# You pass parameters inside the () next to function name.
# You can have no code inside a function, but can't leave it completely empty. Use a pass() method inside the function block
# This pass() says, we basically don't want to do anything with the function right now, but we might visit the function later, so don't throw any error.
# We can execute the function by calling it
print(hello_func())

# You need to have the parenthesis after the function, in order to execute it. If we don't have parenthesis, it would refer to the function object itself and python would print it's representation.
print(hello_func)
# When we execute this code, we simply get <function hello_func at [memory location of function]>

def hello_func():
    print('Hello Function')

print(hello_func())

# Since our print() is within the hello_func() function, we can simply call it instead of printing the output of the function.
hello_func()

# When we execute the second, print(hello_func()), we get an interesting result - Hello Function, followed by None in the second line.
# This happens because when the python executes print(hello_func()), first the function executes its body: print('Hello Function)
# The function finishes, since we didn't write a return statement, python automatically returns None.
# When the outer print() executes, it receives the function's return value (None) and prints it.


##Difference between print and return
# Lets see a simple code snippet, to understand the difference between print() and return
def hello():
    print("Hello")

print(hello())
# This would print both Hello and None.

def hello():
    return('Hello')

print(hello())
# This would only print Hello.

# print() displays a value on the screen but doesn't return that value.
# return sends a value back to the code that called the function.

# Also, in python there's no difference return("Hello") and return "Hello".
# This works, because in Python, return is a keyword, not a function. Parentheses are optional when returning a single value.
def func1():
    return("Hello")

def func2():
    return "Hello"

print(func1()) 
print(func2()) 

# One important distinction, when working with return keyword, is comma(,)
def hello():
    return ('Hello', )

print(hello())
print(type(hello()))
# Executing this, returns a tuple containing a single element ('Hello', )

# Now let's look at how print() function handles commas in parenthesis
def hello():
    print(('Hello', ))      # Prints the tuple, but does not return it

print(hello())              # Prints the tuple, then prints None because the hello() returns None.
print(type(hello()))        # Prints the tuple again, hello() function returns None implicitly. type(None) evaluates to <class 'NoneType'>.

# Functions allows us to reuse the code at multiple locations, keeps the code DRY (Don't Repeat Yourself)

# Functions can take one data type and return another data type, for example the len() function, it takes a string as input and gives integer as output.
# We can treat the returned value just like the data type it is, this enables us to chain together different functionalities.
# We know our hello_func() returns a string, so we can treat that executed function just like a string.
# This only happens when we use return statement in our function, since using print() will also return None.

def hello_func():
    return 'Hello Function'
print(hello_func().upper())

##Passing Arguments
# To be able to pass arguments in our fucntion, we need to create some parameters within our parenthesis
# Let's saw we wanted to customize the greeting our function used, so le'ts create a parameter called greeting.
def hello_func(greeting):
    return f'{greeting} Function'

# If we print the function, without passing in parameters, we will get an error
print(hello_func('Hi'))

# This greeting variable doesnt affect any variables outside the funciton, it's scope is local to only the function.
# The greeting parameter is a required argument, since it doesn't have a default value to fall back to when argument isn't passed.
def hello_func(greeting, name = 'You'):
    return f'{greeting}, {name}'

# We passed a second argument, into our function and gave it a default value. So if we don't provide a name parameter, it won't throw an error.
print(hello_func('Hi'))


##Positional Keyword
# Your required positional arguments have to come before your keyword arguments.
# If we try to create a function, with those out of order, we will get a error

# We might run into a function which looks like this
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

# *args and **kwargs allos us to accept a arbitrary number of postitional and keyword arguments.
# So let's say out student_info() function takes positional arguments that represents the classes that the student is taking, and the keyword aguments will be random information about the students.
# In both of those examples, we don't know how many of these positional and keyword arguments will be, and for that reason we use *args and **kwargs. Names don't neccassary have to be args or kwargs, it's just a common convention.
student_info('Math', 'Art', name = 'John', age = 32)

# args are a tuple filled with all our positional arguments.
# kwargs are a dictionary filled with all our keyword arguments.