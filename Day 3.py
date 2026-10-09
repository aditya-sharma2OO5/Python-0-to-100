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
#cources.insert(0, cources_2)
#cources.append(cources_2)
#print(cources)
#We have a list within a list.

cources.extend(cources_2)
#This adds the individual values of cources_2 at the last of original list.

# 4.Remove() - used to remove items from lists.
cources.remove('Math')

# 5.Pop() - by default, removes last element, Useful if we want o use list as stack or queue
#pop() returns the value it removes, so we can grab that returned value
popped = cources.pop()
print(popped)
    

##Sorting Lists
#If we wanted to reverse our lists, we could do so with the help of reverse()
cources.reverse()
print(cources)

#Sorting our list is just as easy, simply use sort()
cources.sort()
print(cources)

#sort() arranges the list in alphabatical order, as it had text data. If the list had numerical data,
#sort() would sort the list in ascending order.
nums = [1,5,2,4,3]
nums.sort()
print(nums)

#What if we wanted to sort our list in descending order, one way that would intuitively come to mind is to use 
#reverse() on a sorted list. Which would work, but there's a easier way to do so.
nums.sort(reverse = True)
print(nums)

#These methods alters the original list in-place. But there's a way to sort the list, 
#without alterting our original list. What if we simply, wanted a sorted version of our nums list
#without altering the original. We can use the sorted function.
sorted(nums)
print(nums)

#The sorted function, doesnt sort the original list in-place, it returns a new sorted list.
nums_sorted = sorted(nums)
print(nums_sorted)

#Useful, when you dont want to alter the original data (list)

#We also have some couple of additional built-in functions to apply on our list
print(min(nums))
print(max(nums))
print(sum(nums))


##Finding values
#If we wanted to find index of a certian value, we could use the index() method
print(cources.index('CompSci'))

#If we try to find index for a value, that doesn't exist, we get a ValueError
#print(cources.index('French'))

#If we only wanted a Yes or No, about whether a value exists in the list or not, we could use 'in' operator
print('French' in cources)


##Looping Values
#For loop
for item in cources:
    print(item)

#Note - Indentation is important in python, this basically says the code is executed within the loop
#be default, this would print each item in a new line, as print statement goes to a new line each time it is executed.

#We can call the item variable as whatever we want
for cource in cources:
    print(cource)

#Sometimes we might need the index along with the value itself. 
#In python, we can access the index and the value using  the enumerate function
for index,cource in enumerate(cources):
    print(cource, index)

#If we dont want the list to be 0-indexed, we can pass a start value in the enumerate function
for index,cource in enumerate(cources, start = 1):
    print(cource, index)

