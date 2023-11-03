#!/usr/bin/python3
a = 89
b = 10

# Create a temporary variable to store the value of a.
temp = a

# Assign the value of b to a.
a = b

# Assign the value of the temporary variable to b.
b = temp

print("a={:d} - b={:d}".format(a, b))
