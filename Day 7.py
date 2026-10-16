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

# You need to have the parenthesis after the function, in order to execute it. If we don't have parenthesis, it will be equal to the function being there.
print(hello_func)
# When we execute this code, we simply get <function hello_func at [memory location of function]>

def hello_func():
    print('Hello Function')

print(hello_func())

# Since our print() is within the hello_func() function, we can simply call it instead of printing the output of the function.
hello_func()