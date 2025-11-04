'''
Problem 3: Find First and Last Frequency Positions
The Rebel Alliance has intercepted a crucial sequence of encrypted transmissions from the evil Empire. 
Each transmission is marked with a unique frequency code, represented as integers, and these codes are stored 
in a sorted array transmissions. As a skilled codebreaker for the Rebellion, write a function find_frequency_positions() 
that returns a tuple with the first and last indices of a specific frequency code target_code in transmissions. If target_code 
does not exist in transmissions, return (-1, -1).

Your solution must have O(log n) time complexity.

def find_frequency_positions(transmissions, target_code):
    pass
    
Example Usage:
print(find_frequency_positions([5,7,7,8,8,10], 8))
print(find_frequency_positions([5,7,7,8,8,10], 6))
print(find_frequency_positions([], 0))

Example Output:
(3, 4)
(-1, -1)
(-1, -1)
'''

def find_frequency_positions(transmissions, target_code):
    '''
    Plan:
    1. Use binary search to find the first occurrence of target_code.
    2. Use binary search to find the last occurrence of target_code.
    3. Return the indices as a tuple.
    '''
    def find_first():
        l, r = 0, len(transmissions) - 1
        first_pos = -1
        while l <= r:
            mid = (l + r) // 2
            if transmissions[mid] == target_code:
                first_pos = mid
                # Continue searching in the left half...
                r = mid - 1 
            elif transmissions[mid] < target_code:
                l = mid + 1
            else:
                r = mid - 1

        return first_pos
    
    def find_last():
        l, r = 0, len(transmissions) - 1
        last_pos = -1
        while l <= r:
            mid = (l + r) // 2
            if transmissions[mid] == target_code:
                last_pos = mid
                # Continue searching in the right half...
                l = mid + 1 
            elif transmissions[mid] < target_code:
                l = mid + 1
            else:
                r = mid - 1

        return last_pos
    
    first = find_first()
    last = find_last()

    return (first, last) if first != -1 else (-1, -1)

print(find_frequency_positions([5,7,7,8,8,10], 8))
print(find_frequency_positions([5,7,7,8,8,10], 6))
print(find_frequency_positions([], 0))