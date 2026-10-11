# We will learn about Dictionaries.
# Corresponds to video 5 of python playlist

###Dictionaries
# Dictionaries are also called hashmaps or associate arrays in other programming languages.
# Dictionaries operate in key-value pairs, where key is a unique identifier where we can find our data and value is that data.
# Let's say we wanted to represent a student using a dictionary.
student = {'name' : 'John', 'age' : 25, 'cources' : ['math', 'CompSci']}

# Key is the first field followed by the Value field, both seperated by a colon (:). Each pair of key-value is seperated by comma (,).
print(student)

# If we wanted only a value for a specific key
print(student['name'])

# If we try to access a key that doesn't exist, we get a KeyError.
#print(student['phone'])

# Sometimes we don't want to get an error when key doesn't exist. We might just want to return None or a default value. To do this, we can use the get() method.
print(student.get('name'))

# Works normally/similar to before, when we access a key that exists. But if we try to access a key that doesn't exist.
print(student.get('phone'))

# By default this returns None, we can specify a default value to be returned by passing it as second parameter.
print(student.get('phone', 'Not Found'))


##Adding new Entries and Updating Entries
# We can add new entries into a dictionary (adds to the end)
student['phone'] = '111-1111'
print(student)

# If a entry already exists, this will update the value field
student['name'] = 'Jane'
print(student)

# We can also update values using the update() method. Useful when we want to update multiple values at a time.
student.update({'name' : 'Janis', 'age' : 26, 'phone' : '555-5555'})

# update() takes dictionary as an argument, which includes everything we want to update or add.
print(student)


##Deleting Entries
del student['age']
print(student)

# We can also use pop(), and as we discussed earlier pop() removes and returns the value, which we can grab using a variable.

name = student.pop('name')
print(student)
print(name)

##Looping through values

print(len(student))             # Returns no. of keys in your dictionary
print(student.keys())           # Prints all keys in our dictionary
print(student.values())         # Prints all values in our dictionary
print(student.items())          # Prints all keys & values in our dictionary

# If we tried to loop through a dictionary, the same way as do with list, tuples etc
for i in student:
    print(i)

# This only loops through keys not values. Use items() method to loop through both keys and values
for i, j in student.items():
    print(i, j)


##Unpacking 
# We cannot add, a new entry at index 0 using student['key'] = 'value' or by using update() method. As dictionary preservers Insertion Order
# You can use dictionary unpacking (**) to insert a new key-value pair at the beginning of a dictionary.
student = {'name' : 'John', 'age' : 25, **student}
print(student)

# Dictionary unpacking doesn't insert into the original dictionary. It creates a new dictionary in the order you specify and assigns it back to student.

# You can unpack multiple dictionaries.
new_student = {'name': 'Rahul', 'age': 20}
extra = {'phone': '99999-99999', 'city': 'Delhi'}

new_student = {**extra, **new_student}
print(new_student)

# Note - When the same key occurs in multiple dictionaries, the value from the rightmost dictionary wins. 
# Its position, however, follows the key's first insertion.
# This is useful, if a dictionary is missing certain keys. We can provide default values and then override them with actual values.
defaults = {'theme': 'light', 'language': 'English', 'font_size': 12}
user_settings = {'theme': 'dark', 'font_size': 16}
settings = {**defaults, **user_settings}
print(settings)


## Passing a dictionary to a function.
# One of the most important uses of unpacking (**) is passing dictionary entries as keyword arguments to a function.
def student_info(name, age, city, phone):
    print(name, age, city, phone)

student_info(**new_student)
