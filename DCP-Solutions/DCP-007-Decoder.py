# Problem #7

# This problem was asked by Facebook.

# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

# You can assume that the messages are decodable. For example, '001' is not allowed.

def decoding_combinations_andre(alphabet_map, message):
    combinations_list = []
    combinations_list_temp = []
    print("Decoding Message:", message)
    count_message_ones = 0
    for i in range(len(message)):
        if(int(message[i]) > 0):
            count_message_ones += 1
    if count_message_ones <= 1:
        raise Exception ("Invalid Message to Decod!")

    flat_message = ''
    right_order_message = ''
    reverse_order_message = ''
    current_word = ''
    for i in range(len(message)):
        print("i: ", i)
        # print("len(message): ", len(message))
        current_letter = message[i]

        #Get Next Letter from Message (i+1), if there is
        next_letter = getNextLetter(i, message)

        #Get the Letter that will be used for combination(i+2), if there is
        next_letter_combining = getLetterForCombination(i, message)

        print("current_letter: ", current_letter)
        print("next_letter: ", next_letter)
        print("next_letter_combining: ", next_letter_combining)
        if int(current_letter) > 0 and int(current_letter) < 26:
            flat_message = flat_message + current_letter
            if next_letter is not None:
                if is_valid_letter(int(next_letter)):
                    current_word = current_letter + next_letter
                    current_word = decoding_number(alphabet_map, int(current_word))
                    if next_letter_combining is not None:
                        if is_valid_letter(int(next_letter_combining)):
                            right_order_message = current_word + decoding_str(alphabet_map, next_letter_combining)
                            reverse_order_message = decoding_str(alphabet_map, next_letter_combining) + current_word
                            if right_order_message not in combinations_list:
                                combinations_list.append(right_order_message)
                            if reverse_order_message not in combinations_list:
                                combinations_list.append(reverse_order_message)

    print("flat_message:", flat_message)
    decoded_flat_message = decoding_str(alphabet_map, flat_message)
    print("decoded_flat_message:", decoded_flat_message)
    if decoded_flat_message not in combinations_list:
        combinations_list.append(decoded_flat_message)

    print("combinations_list:", combinations_list)
    return len(combinations_list)

def getNextLetter(i, message):
    if (i + 1) < len(message):
        return message[i+1]
    else:
        return None

def getLetterForCombination(i, message):
    if (i + 2) < len(message):
        return message[i+2]
    else:
        return None

def decoding_str(alphabet_map, message):
    decoded_string = ''

    for i in range(len(message)):
        current_key_value = alphabet_map.get(int(message[i]))
        decoded_string = decoded_string + str(current_key_value)

    return decoded_string

def decoding_number(alphabet_map, decode_number):
    decoded_string = ''
    if decode_number < 1 or decode_number > 26:
        return None

    return alphabet_map.get(decode_number)

def is_valid_letter(code):
    return code > 0 and code < 26

def is_char(code):
    return 0 if code > 26 or code < 1 else 1

def decoding_combinations_github(message):
    code_str = str(message)
    if len(code_str) == 1:
        count = 1
    elif len(code_str) == 2:
        count = 1 + is_char(message)
    else:
        count = decoding_combinations_github(int(code_str[1:]))
        if is_char(int(code_str[:2])):
            count += decoding_combinations_github(int(code_str[2:]))

    return count

#########################
# Populate alphabet dict
#########################
alphabet_map = {}
alpha = 'a'
for i in range(1,27):
    alphabet_map[i] = alpha
    alpha = chr(ord(alpha)+1)
print ("alphabet: ", alphabet_map)

assert decoding_combinations_andre(alphabet_map, "111") == 3

assert decoding_combinations_github(81)     == 1
assert decoding_combinations_github(11)     == 2
assert decoding_combinations_github(111)    == 3
assert decoding_combinations_github(1111)   == 5
assert decoding_combinations_github(1311)   == 4
assert decoding_combinations_github("001")  == 1
