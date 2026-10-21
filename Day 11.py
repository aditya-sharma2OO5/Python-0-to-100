# We will learn about Comprehensions (List, Dictionary, Sets).
# Corresponds to video 20 of python playlist.


##List Comprehensions
# A list comprehension is a concise way to create a list by iterating over an iterable and optionally transforming or filtering its elements.
# # Let' first see what it would like in a for loop, to better understand list comprehension.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# I want 'n' for each 'n' in nums
my_list = []
for n in nums:
    my_list.append(n)
print(my_list)

# Now let's see how we would do this using a list comprehension.
my_list1 = [n for n in nums]
print(my_list1)

# Now let's see a more advanced form of list comprehension. First we use for loop and then compare it with list comprehension.
# I want 'n*n' for each 'n' in nums
my_list2 = []
for n in nums:
    my_list2.append(n*n)
print(my_list2)

# Now let's see how we can do this using list comprehension.
my_list3 = [n*n for n in nums]
print(my_list3)

# Note - The general pattern for a list comprehension is: [expression for item in iterable]


##Map + Lambda
# There's another way to do what we did in the earlier code, using maps and lambda.
# map() applies a function to each element of an iterable and produces an iterator containing the results.
# lambda creates a small anonymous function (created without giving it a name using def). 
# Here, lambda n: n * n takes n as input and returns n * n.

# map() applies this lambda function to each number in nums.
# In Python 3, map() returns a map iterator, not a list. Python 2's map() returned a list. 
# Also map() is lazy in Python 3, the transformation is performed as the iterator is consumed, rather than building the complete list at the time map() is called.
my_list4 = map(lambda n: n*n, nums)

# Printing the map object directly displays its object representation, not the values it will produce. In CPython, the object representation commonly looks like a memory address.
print(my_list4)

# Convert the iterator to a list to see all the squared values.
print(list(my_list4))

# This workds because my_list4 has not been consumed yet. 
# Once the iterator is exhausted, trying to convert it to a list again will give you an empty list.
print(list(my_list4))

# Let's look at more advanced list comprehensions
# I want 'n' for each 'n' in nums if 'n' is even.
my_list5 = []
for n in nums:
    if n % 2 == 0:
        my_list5.append(n)

print(my_list5)

my_list6 = [n for n in nums if n % 2 == 0]
print(my_list6)


##Filter + Lambda
# Similar to map() + lambda, we can use filter() + lambda.
# However, map() transforms each element, whereas filter() selects elements based on a condition.

# This lambda function checks whether n is even.
my_list7 = filter(lambda n: n % 2 == 0, nums)           # Similar to map(), filter() returns an iterator.
print(my_list7)         
print(list(my_list7))                                   # Convert iterator to a list and print it.
print(list(my_list7))                                   # Once the iterator is consumed, this will print an empty list.

# Let's look at a more difficulat example
# I want a (letter, num) pair for each letter in  'abcd' and each number in '0123'
my_list8 = []
for letter in 'abcd':
    for num in range(4):
        my_list8.append((letter, num))

print(my_list8)

# Let's see how we can use list comprehension for a consise way of doing the above nested loop.
my_list9 = [(letter, num) for letter in 'abcd' for num in range(4)]
print(my_list9)

# We can also do this comprehensions with Dictionary and sets.


##Dictionary Comprehension
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heroes = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

# zip() combines elements from two or more iterables, pairing items by their positions. It returns a zip iterator in Python 3, not a list.
# zip() stops when the shortest input iterable runs out of elements.
print(list(zip(names, heroes)))

# I want a dict{'name' : 'hero'} for each name, hero in zip(names, heroes)
my_dict = {}
for name, hero in zip(names, heroes):
    my_dict[name] = hero
print(my_dict)

# Let's see dictionary comprehension.
my_dict2 = {name : hero for name, hero in zip(names, heroes)}
print(my_dict2)

# Easy to add restrictions onto the ends of these comprehensions.
# Let's say we don't want Peter added in the list.
my_dict3 = {name : hero for name, hero in zip(names, heroes) if name != 'Peter'}
print(my_dict3)


##Set Comprehension
nums = [1, 1, 2, 1, 3, 4, 3, 4, 5, 5, 6, 7, 8, 7, 9, 9]
my_set = set()
for n in nums:
    my_set.add(n)
print(my_set)

# Now let's how we can do the same with set comprehension.
my_set2 = {n for n in nums}
print(my_set2)
