# We will learn about Property Decorators.
# Corresponds to video 45 of python playlist.

# Property Decorators allows us to give our class attributes getter, setter and deleter functionality.
class Employee:

    def __init__(self, first, last):       
        self.first = first                       
        self.last = last
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return f'{self.first} {self.last}'

emp_1 = Employee('Test', '123')
emp_2 = Employee('Test@', '1234')

emp_1.first = 'Te'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname())

# When we print emp_1.first, we get the newest first name.
# But when we print email. we still get the old name
# the fullname() method also uses the newer first name. As everytime we run it, it grabs the current first name and last name.
# No we don't want to manually change email, everytime we update first and last name. The email should be automatically updated.
# We could use a email() method, but for that, we would have to change every instance of email attribute in the code with email method.
# This is where, getters and setters really come in handy. We can do this in Python, using property decorators.
# Property decorator, allows us to define a method but we can access it like an attribute.
class Employee:

    def __init__(self, first, last):       
        self.first = first                       
        self.last = last

    @property           # Getters
    def email(self):
            return f'{self.first}.{self.last}@company.com'
    
    def fullname(self):
        return f'{self.first} {self.last}'

emp_1 = Employee('Test', '123')

emp_1.first = 'Te'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname())

# Now let's saw we wanted something else. We wanted to pass a value as fullname, and change first, last name and email according to the new fullname.
class Employee:

    def __init__(self, first, last):       
        self.first = first                       
        self.last = last

    @property
    def email(self):
            return f'{self.first}.{self.last}@company.com'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

emp_1 = Employee('Test', '123')

emp_1.fullname = 'Te 12'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

# We can also make a deleter in the same way. 
class Employee:

    def __init__(self, first, last):       
        self.first = first                       
        self.last = last

    @property
    def email(self):
            return f'{self.first}.{self.last}@company.com'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name')
        self.first = None
        self.last = None

emp_1 = Employee('Test', '123')

emp_1.fullname = 'Te 12'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname
    