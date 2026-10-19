# We will learn about Variable Scope in python
# Corresponds to video 18 of python playlist.

# Videos 10-17 have been intentionally skipped, as they involve downloading Jupyter Notebook, Anaconda etc and deals with terminal centric features like pip (python package manager) and venv (virtual environment)

# Variable Scope determines where our variables can be accessed from within the program and what values those variables hold in different contexts
# There's a common abbreviation to understand scoping rules within python. That abbreviation is LEGB.
# LEGB is Local, Enclosing, Global, Built-in.
# Local refers to variables defined within a function.
# Enclosing are variables in the local scope of enclosing functions.
# Global names are defined in a module's global scope. 
# The global keyword tells Python that assignments to a name inside a function should target the module-level name. It does not create a global variable by itself.

# LEGB is the order Python generally follows when looking up a name:
# Local, Enclosing, Global, Built-in.
# Python searches these scopes in order to resolve a name.


##Global and Local Scope
x = 'global x'      # x is a global variable, since it's in the main body of the file

def test():
    y = 'Local y'
    print(y)        
    print(x)

test()

# Since, y was a variable with local scope within the function, it was printed and x had global scope so it was also printed. However this doesn't go both ways.
# If we try to print y outside the function, it will throw an error.
#print(y)

# Let's try to make a local x variable.
def test():
    x = 'local x'
    print(x)

test()          # This will print local x
print(x)        # This will print global x

# When we defined x within the function, it didn't override the global x variable, instead it just created a local x variable that lives only within the function. Outside the local scope of the function, we still see global x variable.
# If we did want to set a new value for that global x variable from within the test function, we can explicitly tell python that the x variable we want to work with is the global x variable.
def test():
    global x
    x = 'local x'
    print(x)

# Both prints local x
test()          
print(x)

# Let's see how local scope works with parameters.
def test(z):
    x = 'local x'
    print(z)

# z is a parameter of test(), so it is local to the function.
# The argument passed to test() becomes the value of z.
test('local z')

# When test() is called, Python binds the argument 'local z' to
# the parameter z. Since z is local to test(), print(z) displays
# the value passed to the function.


##Built-in Scope
# The built-in namespace contains predefined names, including functions, exceptions, and types.
# For example, min() is a built-in function in python used to find the smallest value.
m = min([1, 6, 9, 4])
print(m)

# If we would like to view the variables that are within built-in scope
import builtins
print(dir(builtins))

# One thing to take care while working with built-ins is not to accidentally override them, as python doesn't prevent it.
# The below min() function will override the built-in min().
# def min():
#     pass
# m = min([1, 6, 9, 4])
# print(m)
# When we run this, this time python will throw an error because of LEGB sequence. Python found the min() function in the global scope before it fell back to the built-in scope.

# But, if we change the name of the global min function, it will work.
def my_min():
    pass
m = min([1, 6, 9, 4])
print(m)

# Avoid naming your variables or functions after built-ins.
# A global name takes precedence over the built-in name.


##Enclosing Scope
# Enclosing Scope has to do with nested functions, which is a function within a function.
def outer():
    x = 'outer x'

    def inner():
        x = 'inner x'
        print(x)

    inner()
    print(x)

outer()

# This will print inner x first then outer x.

# However if we never defined any value of x in the inner() function, the inner() would have no local binding for x. 
# Since inner() has no local binding for x, Python looks in the enclosing function's scope and finds x in outer(). 
def outer():
    x = 'outer x'

    def inner():
        #x = 'inner x'
        print(x)

    inner()
    print(x)

outer()

# Similar to how, we could use a global keyword in order to explicitly tell python we wanted to work with global x variable, we have something similar for enclosing scope. The nonlocal keyword
def outer():
    x = 'outer x'

    def inner():
        nonlocal x
        x = 'inner x'
        print(x)

    inner()
    print(x)

outer()

# The nonlocal x statement tells Python to use the nearest enclosing function's existing x binding rather than create a local one.
# Unlike global, which targets the module-level binding, nonlocal targets an existing binding in an enclosing function scope. A matching enclosing binding must exist; otherwise, Python raises a SyntaxError.
