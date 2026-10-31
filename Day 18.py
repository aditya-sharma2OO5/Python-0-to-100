# We will learn about Special (Magic/Dunder) methods.
# Corresponds to video 44 of python playlist.


##Special Methods
# Used within classes.
# Special methods allow us to emulate built-in behaviour in Python 
# and customize how objects behave with built-in operations and operators.
class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):       
        self.first = first                       
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

# __init__() is one of the most common special Methods used when dealing with classes. Let's take a look at 2 more common special methods. __repr__() and __str__().
# In Python, __str__() and __repr__() are special methods (dunder methods) used to control how an object is represented as a string. The main difference is their purpose.
# repr() is meant to be an unambiguous representation of the object and should be used for debugging and logging. Meant to be seen by other developers. Called by repr().
# str() is meant to be more of a readable representation of an object and is meant to be used as a display to the end user. Called by print() and str().
class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):       
        self.first = first                       
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self):
        return f'Employee({self.first}, {self.last}, {self.pay})'

    def __str__(self):
        return f'{self.fullname()} - {self.email}'


emp_1 = Employee('Test', '123', 50000)
emp_2 = Employee('Test@', '1234', 60000)
print(emp_1)

# When we use print(), Python gives priority to __str__(). If we don't have str() defined, Python falls back to repr() when converting an object to a string.
print(repr(emp_1))
print(str(emp_1))


##Arithmetic special Methods.
# We also have lots of special methods for arithmetic operations.
# For example when we do simple addition,
print(1+2)

# This actually uses a special method called Dunder add. 
print(int.__add__(1, 2))

# Strings also use their own Dunder add method when concatenating.
print(str.__add__('a', 'b'))

# We can customize how addition works for our objects by creating that Dunder add method.
# Let's say with our Employee class, we wanted to be able to calculate the total salaries just by adding employees together.
class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):       
        self.first = first                       
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def __add__(self, other):
        return self.pay + other.pay

emp_1 = Employee('Test', '123', 50000)
emp_2 = Employee('Test@', '1234', 60000)

print(emp_1 + emp_2)
# We have all kinds of special methods for arithmetic, special methods for subtraction, multiplication, division etc.


##NotImplemented and __radd__()
# NotImplemented is a special built-in value used inside special methods
# to indicate that the method does not support the given operation or operand type.
# It tells Python that it can try another implementation to handle the operation.

# For example, when we use the + operator, Python initially calls __add__()
# on the left-hand object. If __add__() returns NotImplemented,
# Python may try the reflected method (__radd__()) on the right-hand object.

# __radd__() is the reflected version of __add__().
# It allows the right-hand object to handle the operation when the
# left-hand object's __add__() method cannot handle it.

# If neither object can handle the operation, Python raises a TypeError.
# NotImplemented and __radd__() are particularly useful when implementing operator overloading for different types of objects.

class Employee:

    def __init__(self, first, last, pay):       
        self.first = first                       
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def __add__(self, other):

        # Check whether the other object is also an Employee.
        if isinstance(other, Employee):
            return self.pay + other.pay

        # Return NotImplemented if this method cannot handle the given object type.        
        # Python can then try the reflected operation (__radd__) on the other object
        return NotImplemented

class Developer:

    def __radd__(self, other):

        # __radd__ is the reflected version of __add__.
        # It gives the Developer object an opportunity
        # to handle addition when the Employee object
        # cannot handle the operation.
        return "Developer handled the addition!"

emp_1 = Employee('Test', '123', 50000)
emp_2 = Employee('Test@', '1234', 60000)
dev_1 = Developer()

# Both objects are Employee instances, so __add__ handles addition.
print(emp_1 + emp_2)

# Employee.__add__ returns NotImplemented.
# Python then tries Developer.__radd__.
print(emp_1 + dev_1)  # Developer handled the addition!

# We can use special methods to customize object behaviour, including comparisons, equality checks, arithmetic operations, and other built-in operations.
