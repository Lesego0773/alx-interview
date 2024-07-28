#!/usr/bin/python3
def pascal_triangle(n):
    """
    Returns a list of lists representing the Pascal's Triangle of n.
    """
    if n <= 0:
        return []

    # Initialize the top of the triangle
    triangle = [[1]]

    # Build the triangle row by row
    for i in range(1, n):
        # Start the row with a '1'
        row = [1]

        # Compute the intermediate values
        for j in range(1, i):
            # The value at position j is the sum of the values at positions
            # j-1 and j in the previous row
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])

        # End the row with a '1'
        row.append(1)
        
        # Add the row to the triangle
        triangle.append(row)
    
    return triangle

# Test the function with a specific value of n
if __name__ == "__main__":
    pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

    def print_triangle(triangle):
        """
        Print the triangle
        """
        for row in triangle:
            print("[{}]".format(",".join([str(x) for x in row])))

    print_triangle(pascal_triangle(5))

