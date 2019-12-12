# Problem 4
# This problem was asked by Stripe.

# Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

# You can modify the input array in-place.

def find_first_positive(list_Numbers):
    ordered_list = []

    for num in list_Numbers:
        ordered_list.append(num)

    ordered_list.sort()
    print("ordered_list: ", ordered_list)
    #return ordered_list

    missing_positive = 0
    i = 0
    for element in ordered_list:
        #print("i: ", i)
        #print("element: ", element)
        if element > 0:
            #print("element+1: ", element+1)
            #print("ordered_list[i+1]: ", ordered_list[i+1])
            if (element+1 == ordered_list[i+1]):
                continue
            else:
                return element+1
        i+=1

list_n = [3, 4, -1, 1]
#list_n = [1, 2, 0]

print("List: ", list_n)
print("First Missing Positive Integer: ", find_first_positive(list_n))