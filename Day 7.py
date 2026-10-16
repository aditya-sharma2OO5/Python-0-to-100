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
