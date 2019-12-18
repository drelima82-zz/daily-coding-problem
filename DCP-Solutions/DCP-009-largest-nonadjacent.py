#Problem #9

# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

# Follow-up: Can you do this in O(N) time and constant space?

# def get_largest_non_adj_sum_andre(list_n):
#     total_sum = 0

#     for i in range(len(list_n)):
#         print("i:", i)
#         print("list_n[i]:", list_n[i])
#         if i == 0:
#             print("Total_sum will get first element")
#             total_sum += list_n[i]
#         else:
#             if i+1 < len(list_n):
#                 print("Total_sum will get meximum between current and next")
#                 total_sum += max(list_n[i], list_n[i+1])

#     return total_sum

###########################
# GITHUB SOLUTION
###########################
def get_largest_non_adj_sum(array):
    previous, largest = 0, 0
    for amount in array:
        print("amount: {}; previous: {}; largest: {}".format(amount, previous, largest))
        previous, largest = largest, max(largest, previous + amount)
        print("new_previous: {}; new_largest: {}".format(previous, largest))
    return largest

list_numbers = [2, 4, 6, 2, 5]
print("Total_Sum: ", get_largest_non_adj_sum(list_numbers))

list_numbers = [5, 1, 1, 5]
print("Total_Sum: ", get_largest_non_adj_sum(list_numbers))
