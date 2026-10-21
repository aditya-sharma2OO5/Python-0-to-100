# We will learn about using Try/Except Blocks for Error Handling.
# Corresponds to video 31 of python playlist.

# We use try/except, else/finally block to handle errors and exceptions.


##Try/Except Block
# To understand, why we need a try/except block, let's run some code that will throw an error.
#f = open('testfile.txt')
# This will throw a FileNotFoundError. If we can anticipate which line in our code is likely to throw an error, we can use the try/except block to gracefully handle the error.

try:
    f = open('testfile.txt')
except Exception:
    print('No such file exists')

# Python executes the code in the try block first, and that code throws an exception.
# After that, the except block is executed which prints the custom error message.
# This message is vague, when handling exceptions we want to be specific.
# The vague except block will catch any error thrown by the try block, and print the same error message for all.

try:
    f = open('testfile.txt')
    var = bad_var
except FileNotFoundError:
    print('No such file exists')
except Exception:               #Python executes try block line by line and stops as soon as an exception occurs. Since testfile.txt doesn't exists, Python will never execute the 'var = bad_var'
    print('Sorry, Something went wrong')

# Currently, we are printing some custom messages here. But what if we wanted to print the actual exception?
try:
    f = open('testfile.txt')
    var = bad_var
except FileNotFoundError as e:
    print(e)


##Else/finally Block
# Now let's look at the else and finally block.
# The else block runs only when the try block completes without raising an exception
a = 'empty string'
try:
    print(a)
except NameError as e:
    print(e)
else:
    print('a is empty string')


# finally clause runs no matter what happens, whether the code successfully executed or we encountered an exception.
# Useful for making sure, certain resources are released regardless of what happens in the try/except.
# Let's say we were working with a database, finally clause would allow us to close down the database.
a = 'empty string'
try:
    print(a)
except NameError as e:
    print(e)
else:
    print('a is empty string')
finally:
    print('Code executed')

# We can also raise exceptions on our own using raise.
try:
    f = open('corrupt_file.txt')
    if f.name == 'corrupt_file.txt':
        raise Exception
except Exception as e:
    print('Corrupt File')
