# We will learn about Classes and Instances
# Corresponds to video 40 of python playlist.

# We'll learn the basics of creating and instantiating simple classes. 
# Classes are used throughout most modern programming languages and for good reason.
# Classes allow us to logically group our data and functions in a way that is easy to reuse and also easy to build upon.
# When data and functions are associated with a specific class, we call them attributes and methods.

# Suppose we had a company application, and we wanted to represent our employees. 
# This is a great use case for classes because each individual employee is going to have specific attributes and methods.
# Each employee is going to have a name, email address, pay, actions they can perform. We can use a class as a blueprint to create each employee, so we don't have to manually do it from scratch each time for a new employee.
class Employee:
    pass

# A class is basically a blueprint for creating instances and each new employee that will be created using our employee class will be an instance of that class.
emp_1 = Employee()
emp_2 = Employee()

#Both emp_1 and emp_2 are unique instances of the employee class and are employee objects.
print(emp_1)
print(emp_2)
print(emp_1 is emp_2)


##Instance variables (Attributes)
# Instance variables contain data that is unique to that instance.
# We could manually create instance variables for each employee by doing the following.
emp_1.first =  'Test'       # Employee's 1 first name
emp_1.last = '123'          # Employee's 1 last name
emp_1.email = 'test.123@gmail.com'            
emp_1.pay = 50000

emp_2.first =  'Test@'       
emp_2.last = '1234'          
emp_2.email = 'test@.1234@gmail.com'            
emp_2.pay = 70000

print(emp_1.email)
print(emp_2.email)

# Doing this manually for every employee is a hassle. We can set this info for each employee when they are created rather than doing this manually.
# If we do this manually, we don't get any benefit of using classes.
# To set this up automatically, when we create the employee, we are going to use a special method called __init__(). __init__ initializes the instance after it has been created.
class Employee:
    def __init__(self, first, last, pay):       # When we create methods within a class, they receive the instance as the first argument. We should call this instance self
        self.first = first                      # This is the same as emp_1.first = 'Test'.   
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

# When we create employee instance, the instance is passed automatically, so we can leave off self and only fill in the other arguments.
emp_3 = Employee('Test@@', '12345', 65000)
print(emp_3.email)


##Methods
# The names, email and pay are all attributes of our class. 
# Let's say we wanted the ability to perform some kind of action, we can add some methods to our class.
# Let's say we wanted the ability to display the full name of an employee.
# Methods define actions an object can perform
print(f'{emp_1.first} {emp_1.last}')

# Instead of manually doing this everytime we want the full name of an employee, just create a method in our class.
class Employee:
    def __init__(self, first, last, pay):       
        self.first = first                       
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

    def fullname(self):
        return f'{self.first} {self.last}'

# When we redefine the Employee class, Python creates a new class object and makes the name Employee refer to this new class.
# However, existing instances created from the previous class definition remain instances of the old class.
# Since the old class does not have the fullname() method, calling emp_3.fullname() raises an AttributeError.
# To fix this, we need to create emp_3 again after redefining the Employee class so that it becomes an instance of the new class, which contains the fullname() method.
emp_3 = Employee('Test@@', '12345', 65000)
print(emp_3.fullname())
