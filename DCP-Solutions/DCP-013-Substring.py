"""
Problem #13

This problem was asked by Amazon.

Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".

"""

'''
largest = ''

abcba

[position 0]
a
set([a])

ab
set([a b])

abc
set([a b c])

> if len(set) > len(largest): largest = 'ab'


[position 1]
a
set([a])


qwertyuabccbccccbcba
'''
def get_longest_substring_andre2(word, k):
    largest_string = ''
    current_string = ''
    current_k_map = []

    index = 0
    for current_letter in word:
        current_k_map = []
        current_string = ''
        current_k_map.append(current_letter)
        current_string += current_letter
        for letter_for_substring in word[index+1:]:
            if letter_for_substring not in current_k_map:
                if len(current_k_map) < k:
                    current_k_map.append(letter_for_substring)
                    current_string += letter_for_substring
                else:
                    break
            else:
                current_string += letter_for_substring
        
        #Checking if current substring is larger than previous one
        if len(largest_string) < len(current_string):
            largest_string = current_string

        index += 1

    return largest_string

def get_longest_substring_andre1(word, k):
    if k < 0 or k >= len(word):
        raise Exception("Invalid value for k:", k)

    element_at_k = word[k-1]
    #print("element_at_k:", element_at_k)
    subs = word

    subs = element_at_k
    for i in range(k,len(word)):
        if word[i] == element_at_k:
            subs += word[i]
            return subs
        else:
            subs += word[i]

    return subs

def get_longest_sub_with_k_dist(s, k):
    if not s:
        return ""
    elif len(s) <= k:
        return s
    elif k == 1:
        return s[0]

    distinct_char_count = 0
    seen_chars = set()
    candidate = None
    remaining_string = None

    # to keep track of where the second character occurred
    first_char = s[0]
    second_char_index = 0
    while s[second_char_index] == first_char:
        second_char_index += 1

    candidate = s
    for index, char in enumerate(s):
        if char not in seen_chars:
            seen_chars.add(char)
            distinct_char_count += 1

        if distinct_char_count > k:
            candidate = s[:index]
            remaining_string = s[second_char_index:]
            break
            
    longest_remaining = get_longest_sub_with_k_dist(remaining_string, k)
    
    longest_substring = None
    if len(candidate) < len(longest_remaining):
        longest_substring = longest_remaining
    else:
        longest_substring = candidate
    return longest_substring


assert get_longest_substring_andre1("abcba", 2) == "bcb"
assert get_longest_substring_andre1("abcbadcfebg", 3) == "cbadc"
assert get_longest_substring_andre1("abcbafcarc", 5) == "afca"

assert get_longest_substring_andre2("abcba", 2) == "bcb"
assert get_longest_substring_andre2("abccbba", 2) == "bccbb"
assert get_longest_substring_andre2("abcbbbabbcbbadd", 2) == "bbbabb"
assert get_longest_substring_andre2("abcbbbaaaaaaaaaabbcbbadd", 1) == "aaaaaaaaaa"
assert get_longest_substring_andre2("abccbba", 3) == "abccbba"

assert get_longest_sub_with_k_dist("abcba", 2) == "bcb"
assert get_longest_sub_with_k_dist("abccbba", 2) == "bccbb"
assert get_longest_sub_with_k_dist("abcbbbabbcbbadd", 2) == "bbbabb"
assert get_longest_sub_with_k_dist("abcbbbaaaaaaaaaabbcbbadd", 1) == "a"
assert get_longest_sub_with_k_dist("abccbba", 3) == "abccbba"
