# Problem 2
# This problem was asked by Uber.

# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

# Follow-up: what if you can't use division?

def multiply_arr(list_numbers):
    arrMultiply =  []

    for i in range(len(list_numbers)):
        result = 0
        for j in range(len(list_numbers)):
            if (j != i):
                if result == 0:
                    result = list_numbers[j]
                else:
                    result = result * list_numbers[j]
        arrMultiply.append(result)

    return arrMultiply

numbers = [1, 2, 3, 4, 5]
#numbers = [3,2,1]
print("Numbers:", numbers)
print("Multiplied:", multiply_arr(numbers))
