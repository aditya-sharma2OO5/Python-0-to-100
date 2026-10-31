# We will learn about Special (Magic/Dunder) methods.
# Corresponds to video 44 of python playlist.


##Special Methods
# Used within classes.
# Allows us to emulate some built-in behaviour within Python and also how we implement operator overloading.
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

# __init__() is one of the most common Special Methods used when dealing with classes. Let's take a loot at 2 more common special methods. __repr__() and __str__().
# repr() is meant to be an unambigous representation of the object and should be used for debugging and logging. Meant to be seen by other developers.
# str() is meant to be more of a readable representation of an object and is meant to be used as a display to the end user.
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

    # def __str__(self):
    #     pass


emp_1 = Employee('Test', '123', 50000)
emp_2 = Employee('Test@', '1234', 60000)
print(emp_1)