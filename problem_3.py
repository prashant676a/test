# Loop over a string of arbitrary length, 
# and count the occurrence of each character in the string


def count_string(input_string):
    char_count = {}
    for char in input_string:
        if char in char_count:
            char_count[char] +=1
        else:
            char_count[char] = 1
    
    return char_count

input_str = "hello how are you"
print(count_string(input_str))