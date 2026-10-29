# We will learn about class and static methods.
# Corresponds to video 42 of python playlist.


##Class Methods
# They take the class as the first argument.
# To turn a normal method to a class method, add a decorator to the top.
class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):       
        self.first = first                       
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1   

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod            # Class method decorator
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    # Alternate Constructors
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)


# You can't pass 'class' as the class argument in a class method, as class is a keyword in python. So we use 'cls' as our class argument name.
emp_1 = Employee('Test', '123', 50000)
emp_2 = Employee('Test@', '1234', 60000)

Employee.set_raise_amount(1.05)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# You can use class methods as alternate constructors.
# We can use these class methods in order to provide multiple ways of creating our objects.
emp_str_1 = 'Test-123-50000'
emp_str_2 = 'Test@-1234-60000'

first, last, pay = emp_str_1.split('-')

new_emp_1 = Employee(first, last, pay)
print(new_emp_1.email)
print(new_emp_1.pay)

# Instead of doing all the manual parsing, then printing the new emp, we can just use our alternate constructor.

new_emp_2 = Employee.from_string(emp_str_2)
print(new_emp_2.email)
print(new_emp_2.pay)


##Static Methods
# Static methods don't pass anything automatically as the first argument. They don't pass the instance or the class.
# They behave just like normal functions. They have a logical connection with the class, they don't depend upon any particular instance or class.
class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):       
        self.first = first                       
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1   

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod            # Class method decorator
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    # Alternate Constructors
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
