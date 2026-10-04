#We will learn about Integers and Floats
##This corresponds to video 3 of the python playlist.

#Numbers are most commonly represented by Integers and Floats
#Integer - represents whole numbers, with no fractional or decimal part. Can be -ve, +ve or zero.
#Float - numbers with decimal parts. Can be -ve, +ve or zero.

#Python integers (unlike in languages like C++ or Java) have unlimited length, they are only limited by your computer memory.
#There is no int overflow error for this reason.

num = 3
#Using python's built-in function type(), we can see the data type of an object
print(type(num))    #this would return, <class 'int'>
num = 3.1
print(type(num))


##Arithmetic Operations
# 1.Addition
print(3 + 2)

# 2. Subtraction
print(3 - 2)

# 3.Multiplication
print(3 * 2)

# 4. Division
print(3 / 2)
#In python 2, this would print 1. As the decimal part would be truncated and the value shifted towards 0.
#In python 3, this would print the correct answer of 1.5

# 5.Floor Division
print(3 // 2)

# 6.Exponential
print(3 ** 2)

#Modulus
print(3 % 2)
#This gives remainder after division.


##Order of operations
#order of operations, works correctly within python.
print(3*2+1)
print(3 * (2 + 1))


##Incrementing a variable
num = 1
# 1. num = num + 1
num = num + 1
print(num)

# 2. num +=1
num += 1
print(num)

#Also works with other operations.
num *= 10
print(num)


##Built-in number functions
# 1.abs() - removes sign for any negative numbers
print(abs(-3))

# 2. round() - round your value to the nearest integer ( by default )
print(round(3.75))

#We can also pass a second argument in the round() func, that tells it how many digits we want to round to
print(round(3.75, 1))
#This means we are rounding up to the first digit after the decimal.

#When we are rounding up, .5. The result depends upon the digit in the ones place
print(round(3.5))
print(round(4.5))

#If the digit, before the decimal, is odd. The result is rounded up. And if the digit is even, the result is rounded down
