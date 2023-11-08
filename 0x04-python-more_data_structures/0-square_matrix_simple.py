#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    # Create a new matrix to store the squared values.
    new_matrix = []

    # Iterate over the rows of the input matrix.
    for row in matrix:
        # Create a new row to store the squared values for the current row.
        new_row = []

        # Iterate over the elements of the current row.
        for num in row:
            # Compute the square of the current element.
            squared_num = num * num

            # Add the squared value to the new row.
            new_row.append(squared_num)

        # Add the new row to the new matrix.
        new_matrix.append(new_row)

    # Return the new matrix.
    return new_matrix
