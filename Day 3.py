#We will learn about List, Tuples and sets
#Corresponds to video 4 of python playlist

#Lists and tuples allow you to work with sequential data,
#while sets are unordered collection of unique elements

##Lists
#Allows you to work with a list of values.
#Let's say we wanted a list of cources.
cources = ['History', 'Math', 'Physics', 'CompSci']
print(cources)

#use len() to see no. of values in the list
print(len(cources))

#To access individual elements in our list we can do the followin.
print(cources[0])

#We can also use negative indexes, negative indexes start from the end of list.
print(cources[-1])

#This prints the last item in the list, this is the preferred method to access the last item in our list,
#as we don't have to worry about changing list length.


##List Methods
# 1.Append() - used to insert a value at the end of the list.
cources.append('Art')
print(cources)

# 2.Insert() - used to add a item at a specific index in the list. Takes 2 arguments,
#first is the index where we want to insert, followed by the value itself.
cources.insert(0, 'Art')
print(cources)

# 3.Extend() - use extend() when you wanted to add another list into a list.
#Let's say you had another list, you wanted to add to your original list
cources_2 = ['Art', 'Education']

#If we try to use insert or append, this would add ['Art', 'Education'] to the original list, not the values.
cources.insert(0, cources_2)
cources.append(cources_2)
print(cources)
#We have a list within a list.

cources.extend(cources_2)
#This adds the individual values of cources_2 at the last of original list.

# 4.Remove() - used to remove items from lists.
cources.remove('Math')

# 5.Pop() - by default, removes last element, Useful if we want o use list as stack or queue
#pop() returns the value it removes, so we can grab that returned value
popped = cources.pop()
print(popped)
