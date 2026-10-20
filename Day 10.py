# We will learn about slicing Lists and Strings.
# Corresponds to video 19 of python playlist.

# Slicing extracts selected elements from a sequence, such as a list or a string.
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(my_list[0])       


##Negative Indexes
# We can use negative indexes to traverse our sequence.
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#         -10,-9,-8,-7,-6,-5,-4,-3,-2,-1

print(my_list[-1])

# This will print the last element for the variable my_list.


##Accessing Range of Values via Slicing
# We can use positive or negative indexes to access single elements, but how do we access a range of values.
# The syntax for accessing a range of values is list[start:end:step]
print(my_list[0:5])         # Print elements from 0th Index upto but not including 5th Index

# End index is non-inclusive while Start index is inclusive.

# We can also mix postive and negative indexes
print(my_list[-10:5])       # Same as print(my_list[0:5])

# If the start index is omitted, Python will start the slicing from the beginning of the sequence.
print(my_list[5:])

# If the end index is omitted, Python slices to the end of the sequence.
print(my_list[:5])

# If both index are omitted, a new shallow copy of the list is created. Values printed are the same, but the resulting list is a seperate list object.
print(my_list[:])

# Now that we have a basic idea of start and end index, let's go over then step index.
# Step allows us to skip a certain number of values.
# Let's say I wanted to start at index 2, and go till index 8, but I only want to print every second element.
print(my_list[2:-1:2])
# Step value of 2, prints every second value. A step value of n, would print every nth value by skipping (n-1) values. A step value of 3, would print every third value by skipping 2 values.

# You can also have negative values of step, but step can't be zero or else Python will throw an error.
# However for a negative step to be valid, there are some caveats.
print(my_list[2: -1: -1])

# A negative step moves right to left.
# This slice is empty because the start and stop positions are in the wrong order for a negative step.
# But if we were to reverse the values of start and end index
print(my_list[-1: 2: -1])   

# When Step value is -n, it skips (n+1) value. So Step Value of -2, skips -1 or 1 value on going from right to left.


##Slicing Strings
sample_url = 'https://example.com'
print(sample_url)

# Reverse the url
print(sample_url[ : :-1])

# Get top level domain (.com)
print(sample_url[-4: : ])