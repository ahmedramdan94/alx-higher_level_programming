#!/usr/bin/python3
def max_integer(my_list=[]):

    if len(my_list) == 0:
        return None

    # Initialize the biggest integer to the first element of the list.
    biggest = my_list[0]
    for num in my_list[1:]:
        if num > biggest:
            biggest = num

    # Return the biggest integer.
    return biggest
