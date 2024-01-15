# Code block for solving max sum for subsequence where selecting adjacement elements
# is not allowed
# This is solved using DP in constant space.

A = [3,2,5,10,7]

def find_max_sum(A):
    n = len(A)
    # Initialize a and b with the first two elements
    a = A[0]
    b = max(A[0], A[1])

    for i in range(2, n):
        # Calculate the new value for c
        c = max(A[i] + a, b)
        # Update a and b for the next iteration
        a = b
        b = c
    return c

print(find_max_sum(A))