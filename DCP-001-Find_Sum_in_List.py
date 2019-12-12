def find_sum(list_numbers, k):
    found =  False

    for i in range(len(list_numbers)):
        for j in range(len(list_numbers)):
            if (list_numbers[i] + list_numbers[j] == k):
                print("Value found: {} (I={}, J={})".format(list_numbers[i] + list_numbers[j], i+1, j+1))
                found = True
                return found

    return found

numbers = [10,15,3,7]
k = 17
print(find_sum(numbers, k))

