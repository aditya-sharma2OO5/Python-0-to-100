# We will learn about Duck Tying and EAFP.
# Corresponds to video 32 of python playlist.

# Duck typing and EAFP are two Python concepts that encourage writing clean, readable, and flexible code in the Pythonic style.

##Duck Tying
# In this concept, we assume that if an object walks like a duck, quacks like a duck then it's a duck.
# That basically means, we don't care what type of object we are working with, we only care if our object can do what we ask it to do.
# In programming, this means we care more about what an object can do than about its specific type. If an object provides the methods or behaviors our code needs, we can use it without checking its exact class.

class Duck:

    def quack(self):
        print('Quack, quack')

    def fly(self):
        print('Flap, Flap!')

class Person:

    def quack(self):
        print('I am Quacking like a duck')

    def fly(self):
        print('I am Flapping my arms')

def quack_and_fly (thing):
    # Not Duck-typed (non Pythonic). Explicitly check the object's type.
    if isinstance(thing, Duck):
        thing.quack()
        thing.fly()
    else:
        print('This has to be a duck')

    print()

d = Duck()
quack_and_fly(d)

p = Person()
quack_and_fly(p)

# In this example, Duck works, but Person is rejected because it is not an instance of the Duck class, even though it has both required methods.

# Using duck typing: Instead of checking the object's type, we can simply call the methods we need.
def quack_and_fly (thing):
    # Duck typing: focus on behavior, not type.
    thing.quack()
    thing.fly()
    
    print()

d = Duck()
quack_and_fly(d)

p = Person()
quack_and_fly(p)
# Now both objects work because both provide the quack() and fly() methods.
# If an object does not provide these methods, Python raises an AttributeError.
# Note -  Duck typing does not guarantee that the methods will work correctly. It allows us to use objects based on their behavior rather than their class.


##EAFP and LBYL
# With duck typing, we can pass any object to our function.
# However, if the object does not support the required methods, calling them may raise an AttributeError.

# One approach is to check whether the required methods exist before calling them. This is known as LBYL (Look Before You Leap).

# Another approach is EAFP (Easier to Ask Forgiveness than Permission),
# where we try to perform the operation and handle any expected
# exceptions if it fails.

def quack_and_fly (thing):
    # LBYL (Non Pythonic)
    if hasattr(thing, 'quack'):
        if callable(thing.quack):
            thing.quack()

    if hasattr(thing, 'fly'):
            if callable(thing.fly):
                thing.fly()

    print()

d = Duck()
quack_and_fly(d)

p = Person()
quack_and_fly(p)

# Here, we check whether the methods exist and are callable before attempting to call them.
# However, these checks do not guarantee that the method calls will succeed. A method could still raise an exception, or the object's state could change between the check and the operation.

def quack_and_fly(thing):
    # EAFP (Pythonic)
    try:
        thing.quack()
        thing.fly()
    except AttributeError as e:
        print(e)

    print()

d = Duck()
quack_and_fly(d)

p = Person()
quack_and_fly(p)

# Instead of checking whether the methods exist, we try calling them directly. If an AttributeError occurs, we handle it.


##EAFP in Data Structures
#Let's use a dictionary to understand how EAFP and LBYL work with data structures.

#person = {'name' : 'Jess', 'age' : 23, 'job' : 'Programmer'}
person = {'name' : 'Jess', 'age' : 23}                  
# The 'job' key is intentionally missing.

# LBYL (Non-Pythonic)
if 'name' in person and 'age' in person and 'job' in person:
    print(f"I'm {person['name']}. I'm {person['age']} years old and I am a {person['job']}")
else:
    print('Missing some keys')
# Here, we check whether all the required keys exist before accessing their values.

# EAFP (Pythonic)
try:
    print("I'm {name}. I'm {age} years old and I am a {job}".format(**person))
except KeyError as e:
    print("Missing {} key".format(e))

# EAFP has many benefits over LBYL. It is much faster in situations where you don't expect a lot of exceptions.


##Race Condition
# A race condition can occur when the result of an operation depends on the timing or order of concurrent operations.
# One example is a TOCTOU (Time Of Check To Time Of Use) race condition. This occurs when we check whether an operation is possible and then perform that operation separately, leaving time for the situation to change between the check and the action.

import os
my_file = "/tmp/test.txt"

# Race Condition (LBYL)
if os.access(my_file, os.R_OK):
    with open(my_file) as f:
        print(f.read())
else:
    print('File can not be accessed')

# The problem is that the file's accessibility could change after os.access() returns but before open() is called.
# For example, another process could remove the file or change its permissions between those two operations.

# No Race Condition (EAFP).
try:
    f = open(my_file)
except IOError as e:
    print('File can not be accessed')
else:
    with f:
        print(f.read())

# Here, we attempt to open and read the file directly. If the operation fails, we handle the resulting OSError.
# The with statement automatically closes the file when the block finishes, even if an exception occurs.
# This approach avoids the separate accessibility check and its associated check-then-act race condition.
# Note -  EAFP does not eliminate every possible race condition. It avoids relying on a separate check when the operation itself can tell us whether it succeeded.
