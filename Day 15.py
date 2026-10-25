# We will learn about class variables
# Corresponds to video 41 of python playlist.


##Class Variables
# Instance variables belong to individual instances and can have different values.
# Class variables belong to the class and are shared through attribute lookup, unless an instance defines an attribute with the same name.
class Employee:
    def __init__(self, first, last, pay):       
        self.first = first                       
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return f'{self.first} {self.last}'

# Looking at this Employee class, what kind of data would we want to share among all instances of the Employee class.
# Let's say we had annual raise percentage for every employee. We would want to share this data among all instances of Employee class. 
# One way to do that, would be to hardcode a value like 4% annual raise. However if we wanted to update this value, we would have to update it everywhere.
# So instead let's just create a class variable.
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

# Class variables can be accessed through the class or an instance.
# When we access a class variable through an instance, Python first looks for that attribute in the instance. 
# If it isn't found, Python looks for it in the class (and its inheritance hierarchy).

# Therefore, self.raise_amount accesses the instance's raise_amount if one exists; otherwise, it looks up the attribute in the class and its inheritance hierarchy.
# Alternatively, Employee.raise_amount   looks up the attribute on the Employee class. 
# If the attribute isn't defined directly on Employee, Python may find it in the class's inheritance hierarchy. 
# This lookup is independent of any instance-level raise_amount attribute.

emp_1 = Employee('Test', '123', 50000)

print(emp_1.raise_amount)     # 1.04
print(Employee.raise_amount)  # 1.04

emp_1 = Employee('Test', '123', 50000)
print(emp_1.raise_amount)
print(Employee.raise_amount)


##__dict__
# We use __dict__ to inspect the namespaces of an instance and its class.
# This helps us understand which attributes are stored directly on the instance and which are defined directly on the class, and how Python finds class attributes when we access them through an instance.

print(emp_1.__dict__)
# Returns a dictionary containing the attributes stored directly on emp_1.
# Initially, it contains first, last, pay, and email, but not raise_amount, because raise_amount is defined on the Employee class.

print(Employee.__dict__)
# Returns a mapping containing attributes defined directly on the Employee class, including raise_amount, __init__, fullname, and apply_raise.
# It also contains special attributes Python creates for the class.

# When we access emp_1.raise_amount, Python first looks for raise_amount in emp_1's attributes. 
# If it isn't found, Python looks in the Employee class and its inheritance hierarchy to find the attribute.

Employee.raise_amount = 1.09

# Changing Employee.raise_amount updates the class variable. Instances without their own raise_amount attribute will see the updated value.
print(Employee.raise_amount)
print(emp_1.raise_amount)

# But if we change the raise_amount using an instance instead of using the class. Then only that instance alone would have the changed raise_amount value.
emp_1.raise_amount = 1.15

print(Employee.raise_amount)
print(emp_1.raise_amount)

# This happened because when we made that assignment, it created a raise_amount attribute within emp_1. 
# Since the instance has the attribute in its namespace, it doesn't have to find that attribute in the Employee class namespace
print(emp_1.__dict__)       # Now contains the instance's raise_amount

# Some data should be tracked across the entire class rather than
# separately for each instance. For example, the total number of employees.
# We use Employee.num_of_emps to update the class variable explicitly.
class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):       
        self.first = first                       
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1       # Do this inside the init method, as it runs everytime we create a new employee

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
