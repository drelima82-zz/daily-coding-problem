#Problem #11

# This problem was asked by Twitter.

# Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

# For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

# Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.

def get_autocomplete_strings(inputString):
    autocompletestr = []
    find_size = len(inputString)

    for text in cache_strings:
        if text.find(inputString, 0, find_size) >= 0:
            autocompletestr.append(text)

    return autocompletestr

cache_strings = ["dog", "deer", "deal", "delimiter", "August", "paragraph"]

assert get_autocomplete_strings("de") == ["deer", "deal", "delimiter"]
assert get_autocomplete_strings("limit") == []
assert get_autocomplete_strings("Au") == ["August"]