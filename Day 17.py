# We will learn about Inheritance.
# Corresponds to video 43 of python playlist.

# Inheritance allows us to inherit attributes and methods from a parent class. This is useful for creating sub classes. 
# This also allows us to get all the functionality of our parent class and override or add new functionality without affecting parent class.
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

# Let's say we wanted to create different types of employees - developers, managers.
# These would be great candidates for sub classes because both developers and managers are going to have name, email and salary. All things our Employee class already has.
class Developer(Employee):
    pass

dev_1 = Developer('Test', '123', 50000)
dev_2 = Developer('Test@', '1234', 60000)

print(dev_1.email)
print(dev_2.email)

# When we instantiate our developers, it first looked into our developer class for the init method, which wasn't there.
# So Python, walks up the chain of inheritance until it founds the init method. This chain is called Method Resolution Order.
# Using help(), we can visualize this.
#print(help(Developer))


##Customization
# We can customize our sub class without affecting any of the Parent Class instances.
class Developer(Employee):
    raise_amount = 1.10

dev_1 = Developer('Test', '123', 50000)
dev_2 = Developer('Test@', '1234', 60000)

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

# Sometimes we want to initiate our sub class with more info than our parent class can handle.
# Let's say we want to pass programming lang as an attribute.
