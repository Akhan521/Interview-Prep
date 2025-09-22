'''
Problem Statement:
    You are given an array of integers. We define a bitonic subarray as a contiguous subarray that first increases and then decreases.
    Write a function `bitonic_length(arr)` that returns the length of the longest bitonic subarray in the given array.
    Note: A strictly increasing or strictly decreasing subarray is also considered bitonic.

Example Usage:
    arr = [12, 4, 78, 90, 45, 23]
    bitonic_length(arr)

    arr = [20, 4, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    bitonic_length(arr)

Example Output:
    5 -> The longest bitonic subarray is [4, 78, 90, 45, 23]
    9 -> The longest bitonic subarray is [1, 2, 3, 4, 5, 6, 7, 8, 9]
'''

def bitonic_length(arr):
    '''
    Plan:
        1. Create two helper arrays: `inc` and `dec` of the same length as `arr`.
        2. Fill the `inc` array such that `inc[i]` is the length of the longest increasing subarray ending at index `i`.
        3. Fill the `dec` array such that `dec[i]` is the length of the longest decreasing subarray starting at index `i`.
        4. The length of the longest bitonic subarray peaking at index `i` can be found by `inc[i] + dec[i] - 1`.
        5. Iterate through the arrays to find the maximum value of `inc[i] + dec[i] - 1`.
        6. Return this maximum value.

        Note: We subtract by 1 to avoid double counting the element at index `i` (the peak of the bitonic subarray).
        The peak element is the highest point of the bitonic subarray, so it is counted in both increasing and decreasing parts.
    '''
    # Edge case: If the array is empty, return 0.
    if not arr:
        return 0
    
    n = len(arr)
    inc = [1] * n  # Longest increasing subarray lengths
    dec = [1] * n  # Longest decreasing subarray lengths

    # Fill the inc array:
    for i in range(1, n):
        # If the current element is >= the previous element, it can extend the increasing subarray.
        if arr[i] >= arr[i - 1]:
            inc[i] = inc[i - 1] + 1

    # Fill the dec array:
    for i in range(n - 2, -1, -1):
        # If the current element is >= the next element, it can extend the decreasing subarray.
        if arr[i] >= arr[i + 1]:
            dec[i] = dec[i + 1] + 1

    # Find the length of the longest bitonic subarray:
    max_len = 1
    for i in range(n):
        max_len = max(max_len, inc[i] + dec[i] - 1)

    return max_len

arr = [12, 4, 78, 90, 45, 23]
print(bitonic_length(arr))

arr = [20, 4, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(bitonic_length(arr))