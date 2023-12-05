# Write a function named sum_to that accepts a single integer, n, and returns the sum of the integers from 1 to n.

'''
def sum_to(n):
    nums = range(1,(n+1))
    print(sum(nums))

sum_to(6)
'''

# Write a function named largest that takes a list of numbers as an argument and returns the largest number in that list.

'''
def largest (*args):
    nums = sorted(*args)
    largest_num = nums[-1]
    return largest_num

print(largest([1,8,3,4]))
'''

# Write a function named occurrences that takes two string arguments as input and counts the number of occurrences of the second string inside the first string.

'''
def occurrences(x, y):
    num_of_y = x.count(y)
    print(num_of_y)

occurrences('fleep floop', 'e')   # returns 2
occurrences('fleep floop', 'p')   # returns 2
occurrences('fleep floop', 'ee')  # returns 1
occurrences('fleep floop', 'fe')  # returns 0
'''

# Write a function named product that takes an arbitrary number of numbers, multiplies them all together, and returns the product.

def product (*args):
    result = 1
    for num in args:
        result *= num
    print(result)

product(-1, 4) # returns -4
product(2, 5, 5) # returns 50
product(4, 0.5, 5) # returns 10.0