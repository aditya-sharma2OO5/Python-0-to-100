# We will learn about List, Tuples and sets
# Corresponds to video 4 of python playlist

# Lists and tuples allow you to work with sequential data,
# while sets are unordered collection of unique elements

###Lists
# Allows you to work with a list of values.
# Let's say we wanted a list of cources.
cources = ['History', 'Math', 'Physics', 'CompSci']
print(cources)

#use len() to see no. of values in the list
print(len(cources))

# To access individual elements in our list we can do the followin.
print(cources[0])

# We can also use negative indexes, negative indexes start from the end of list.
print(cources[-1])

# This prints the last item in the list, this is the preferred method to access the last item in our list,
# as we don't have to worry about changing list length.

##List Methods
# 1.Append() - used to insert a value at the end of the list.
cources.append('Art')
print(cources)

# 2.Insert() - used to add a item at a specific index in the list. Takes 2 arguments,
# first is the index where we want to insert, followed by the value itself.
cources.insert(0, 'Art')
print(cources)

# 3.Extend() - use extend() when you wanted to add another list into a list.
# Let's say you had another list, you wanted to add to your original list
cources_2 = ['Art', 'Education']

# If we try to use insert or append, this would add ['Art', 'Education'] to the original list, not the values.
#cources.insert(0, cources_2)
#cources.append(cources_2)
#print(cources)
# We have a list within a list.

cources.extend(cources_2)
# This adds the individual values of cources_2 at the last of original list.

# 4.Remove() - used to remove items from lists.
cources.remove('Math')

# 5.Pop() - by default, removes last element, Useful if we want o use list as stack or queue
# pop() returns the value it removes, so we can grab that returned value
popped = cources.pop()
print(popped)
    
##Sorting Lists
# If we wanted to reverse our lists, we could do so with the help of reverse()
cources.reverse()
print(cources)

# Sorting our list is just as easy, simply use sort()
cources.sort()
print(cources)

# sort() arranges the list in alphabatical order, as it had text data. If the list had numerical data,
# sort() would sort the list in ascending order.
nums = [1,5,2,4,3]
nums.sort()
print(nums)

# What if we wanted to sort our list in descending order, one way that would intuitively come to mind is to use 
# reverse() on a sorted list. Which would work, but there's a easier way to do so.
nums.sort(reverse = True)
print(nums)

# These methods alters the original list in-place. But there's a way to sort the list, 
# without alterting our original list. What if we simply, wanted a sorted version of our nums list
# without altering the original. We can use the sorted function.
sorted(nums)
print(nums)

# The sorted function, doesnt sort the original list in-place, it returns a new sorted list.
nums_sorted = sorted(nums)
print(nums_sorted)

# Useful, when you dont want to alter the original data (list)

# We also have some couple of additional built-in functions to apply on our list
print(min(nums))
print(max(nums))
print(sum(nums))

##Finding values
# If we wanted to find index of a certian value, we could use the index() method
print(cources.index('CompSci'))

# If we try to find index for a value, that doesn't exist, we get a ValueError
#print(cources.index('French'))

# If we only wanted a Yes or No, about whether a value exists in the list or not, we could use 'in' operator
print('French' in cources)

##Looping Values
#For loop
for item in cources:
    print(item)

# Note - Indentation is important in python, this basically says the code is executed within the loop
# be default, this would print each item in a new line, as print statement goes to a new line each time it is executed.

# We can call the item variable as whatever we want
for cource in cources:
    print(cource)

# Sometimes we might need the index along with the value itself. 
# In python, we can access the index and the value using  the enumerate function
for index,cource in enumerate(cources):
    print(cource, index)

 #If we dont want the list to be 0-indexed, we can pass a start value in the enumerate function
for index,cource in enumerate(cources, start = 1):
    print(cource, index)

#List into Strings
# It's pretty common to turn our lists into strings seperated by a certain value.
# We can do this using a string method called join()
cource_str = ', '.join(cources)
print(cource_str)
# The ', ' before join() is used to tell programming languages we want our string values seperated by a comma(,) and space.

#Splitting Values
# We can also do the reverse, turn strings back to list. We can do this by splitting our string on a certain value.
new_list = cource_str.split(' - ')
print(new_list)


###Tuples
# Very similar to lists, but they are immutable i.e. can't be modified
# Let's look at mutable objects like lists
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

list_1[0] = 'Art'

print(list_1)
print(list_2)
# Now both list_1 & list_2 have been changed as they are the same mutable objects.
# This is fine if want a object we can modify.
# But, if we want values we don't want to change we can use Tuples
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

#tuple_1[0] = 'Art'

# When we try to change the value, similar to lists we this following error - 
# TypeError: 'tuple' object does not support item assignment

# Since tuples are immutable, it doesn't have nearly as many as methods as lists.
# We can't remove, append values. We can loop through values, and access values.


###Sets
# Sets are unordered, unique collection of elements.
cs_cources = {'History', 'Math', 'CompSci', 'Math', 'Phy'}
print(cs_cources)

# When we print, the order of values will be random each time as set is unordered.
# Sets remove duplicate values, so Math will be printed only once.

# Membership Test - Check whether a particular element exists in a sequence or collection like tuples, lists, sets etc.
# Sets do this more efficiently.
print('Math' in cs_cources)

# We can also use sets, to determine what values they share or not share with other sets.
art_cources = {'Art', 'Design', 'History', 'Math'}
commerce_cources = {'Commerce', 'Economics', 'History', 'Math'}

# 1.intersection() - used to return the common values between multiple sets
print(cs_cources.intersection(art_cources, commerce_cources))

# Can also sue the '&' operator
print(cs_cources & art_cources & commerce_cources)

# 2.union() - returns all unique elements from all sets
print(cs_cources.union(art_cources, commerce_cources))

# Can also use the '|' operator
print(cs_cources | art_cources | commerce_cources)

# 3.difference() - returns elements that belong to the first set but not to the rest.
print(cs_cources.difference(art_cources, commerce_cources))

# Can also use the '-' operator
print(cs_cources - art_cources - commerce_cources)

# Note - both intersection and union are commutative i.e. order doesn't matter. Difference is not commutative
print(cs_cources.intersection(art_cources, commerce_cources))
print(art_cources.intersection(cs_cources, commerce_cources)) 

print(cs_cources.union(art_cources, commerce_cources))
print(commerce_cources.union(cs_cources, art_cources))

print(cs_cources.difference(art_cources, commerce_cources))
print(art_cources.difference(cs_cources, commerce_cources))

# union(), intersection(), and difference() return sets, whose element order is not guaranteed.
# Repeated calls may display the same order because Python's set iteration order often remains consistent within a session.
# However, the order can differ in other situations, so identical output order is not guaranteed.

# sorted() arranges the elements of a set in a predictable order and returns them as a list, not a set.
# sorted() doesn't change the original set, it returns a new list containing elements in sorted order.
# syntax is - sorted(iterable, key=None, reverse=False)
print(sorted(cs_cources))

# iterable is the collection of elements we want to sort, like cs_cources.
# key - lets you specify a funtion that determines how python should sort the elements.
# default value of key is None, so python sorts using elements natural ordering.
# we can use key = len, to tell python to sort cources name by their length (shortest to longest)
print(sorted(cs_cources, key = len))

# reverse parameter determines the sorting direction. Default value is False (ascending)
print(sorted(cs_cources, key = len, reverse = True))

# A important observation when we run these two commands, the relative ordering of "History" & "CompSci" may change between different runs as they both have 7 characters.
# One more observation, they dont simply swap positions in descending order. We get outputs - 
# ['Phy', 'Math', 'History', 'CompSci']
# ['History', 'CompSci', 'Math', 'Phy']
# Because reverse=True reverses the sorting direction, not the relative order of elements with equal keys. Python preserves the relative order of tied elements even when sorting in reverse.
# That's why, if "History" appears before "CompSci" in the ascending result, it also appears before "CompSci" in the descending result.

# If we want a predictable/stable order, i.e. sort by length and then alphabetically when lengths are equal, use a tuple as the key:
print(sorted(cs_cources, key=lambda x: (len(x), x)))

# For descending order, use this. We use negative lengths to put longer strings first.
print(sorted(cs_cources, key=lambda x: (-len(x), x)))

# This would always print - ['Phy', 'Math', 'CompSci', 'History']
#                           ['CompSci', 'History', 'Math', 'Phy']


##Empty Lists, Tuples and Sets
# We can either use literal syntax like [], (), or {}. Second option is to use python's built-in functions.

empty_list = []
empty_list = list()

empty_tuple = ()
empty_tuple = tuple()

empty_set = {}
print(type(empty_set))
# This initializes an empty dictionary instead of empty set
# Use python's built-in set() function to initialize an empty set.
empty_set = set()
print(type(empty_set))
