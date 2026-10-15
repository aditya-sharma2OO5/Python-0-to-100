# We will learn about Loops and Iterations.
# Corresponds to video 6 of python playlist.


##For Loops
# Let's see a simple for loop example
nums = [1, 2, 3, 4, 5]
for num in nums:
    print(num)

# Let's look at two important keywords assiciated with loops. break and continue keywords
# break - completely breaks out of the loop, or stops further execution of the loop and its indented code.
# continue - moves forward, towards the enxt iteration of the loop.

# Let's say, we want to only loop through until a given condition isn't satisfied and when the condition is satisfied, then stop. We will use break statement for this.
for num in nums:
    if num == 2:
        print('Found!')
        break
        print('Will this print?, No')
    print(num)      # Will only print 1 before printing 'Found'

# In this code, if we only wanted to print 'Found' when the number was found and not completely stop the execution of loop, we could use continue statement.
for num in nums:
    if num == 2:
        print('Found!')
        continue
        print('This will also not print')
    print(num)

# We can also have loop within a loop (nested loops)
for num in nums:
    for letter in 'abc':
        print(num, letter)

# There might arrise a situation, where we only want to iterate through a loop only for a given no, of terms/times. For this we have a built-in function called range().
for i in range(10):
    print(i)
# We start from 0 (first index) and upto but not including the no. we pass as the argument in range, in this case 10 so we only go till 9 (10th index).

# We can also specify the starting value, if we don't want to start with 0.
for i in range(1,11):
    print(i)


##While Loops
# For loops iterate through a certain no. of values, while loops on the other hand iterate until a certain condition is met or a break statement is executed. 
x = 0
while x < 10:
    if x == 5:
        break
    print(x)
    x += 1

# We can also create a infinite loop, which keeps on running until you get your desired output.
# Simply replace comparision with True. For our code, we have added a break statement, to stop execution of infinite loop, If we replaced break with continue, it would continue to run indefinetly,
x = 0
while True:
    if x == 5:
        break
    print(x)
    x += 1