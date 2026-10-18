# We will learn about Importing Modules and Standard Library
# Corresponds to video 9 of python playlist.

# Lets create a cusom module, and learn how to import that module in another module or file.
# We have created a custom module in my_module.py file. Keep the module in the same directory, so it becomes easier to import it.

# Now that we have created a module, when we import this module it runs all the code it contains, this enables it to create all the functions and variables. It also runs all print and return statements.
import my_module 
cources = ['History', 'Math', 'Physics', 'CompSci']

# When we execute this file, python performs the following steps:
    # 1.Finds the module: Python locates my_module.py.
    # 2.Compiles the module: Python compiles its source code into bytecode, an intermediate representation that the Python virtual machine can execute.
    # 3.Caches the bytecode: Python saves the compiled bytecode in a .pyc file inside __pycache__.
    # 4.Executes the module: Python executes the module's top-level statements, including your print() statement, and defines its variable and function.

# The __pycache__ folder contains a single file, my_module.cpython-312.pyc
# my_module refers to the name of the module. cpython is the standard python implementation, CPython.
# 312 is the CPython bytecode cache tag, indicating Python 3.12. 
# .pyc is a compiled Python bytecode file.

# Python needs this cache to primarily speed up future imports.

# Let's say we wanted to work with the functions inside our module, in our case it is find_index function.
# We can't just call our find_index function, we instead have to type our module name first and then what we want to grab from that function.
index = my_module.find_index(cources, 'Math')
print(index)

# You can use an abbrevation for a module name to reduce the hassle of typing long module names
import my_module as mm
index = mm.find_index(cources, 'Math')
print(index)

# We could also straight up import the function itself. However this will only give access to that particular function, and not the test variable. To get the test variable we need to include it along with find_index() function
from my_module import find_index as fi, test
index = fi(cources, 'Math')
print(index)
print(test)

# There is a way to import everything form a module
from my_module import *

# Not preferred because, there is no way to tell which variable, method, function came from that specific module and which didn't.


##Sys Module
# When we import a module how does python know where to find the module, since we didn't pass any path location. 
# Python uses a list of locations called sys.path to help locate modules. The exact search locations and order depend on the Python installation, environment, and how Python was started.
import sys

# Display the list of directories and locations Python searches when looking for importable modules.
print(sys.path)

# Python checks this list sequentially for the module. 
# Directories get added in a particular order. First directory is the directory containing the script we're running.
# It then adds directories listed in the python path environment variable.
# After python python path, it adds the standard library directories.
# Lastly it adds site packages directory for third-party packages.


##Standard Library
# The Python Standard Library is a collection of modules included with a standard Python installation.
# Standard Library allows you to use a module or function without installing anything. Useful if you're performing a common task, then most likely someone has already written functionality for it.
# Many standard library modules are implemented efficiently, but performance depends on the module and operation.
# Let's say we wanted to grab a random element from a collection of items, we could simply use the random module from the Standard Library.
import random
random_cource = random.choice(cources)
print(random_cource)

# Some more useful Standard Library Modules
# 1.Math - if we want to perform some common mathematical operations
import math
rads = math.radians(90)
print(rads)
print(math.sin(rads))

# 2.datetime - work with dates and times.
import datetime
today_date = datetime.date.today()
print(today_date)

# 3.calender - perform calendar-related calculations.
import calendar
print(calendar.isleap(2020))

# 4.os - interact with the operating system
import os
print(os.getcwd())

# You can view the location of a module (like os) by using the Dunder file attribute. Dunder basically means double underscores (__)
print(os.__file__)
