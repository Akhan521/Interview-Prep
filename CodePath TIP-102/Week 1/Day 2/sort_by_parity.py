'''
Problem 4: Sort Array by Parity
Given an integer array nums, write a function sort_by_parity() that moves all the even integers to the beginning of the array, 
followed by all the odd integers.

Return any array that satisfies this condition.

def sort_by_parity(nums):
    pass

Example Usage:
nums = [3, 1, 2, 4]
sort_by_parity(nums)

nums = [0]
sort_by_parity(nums)

Example Output:
[2, 4, 3, 1]
[0]
'''

def sort_by_parity(nums):
    l, r = 0, len(nums) - 1
    while l < r:
        # If left is odd and right is even, swap.
        if nums[l] % 2 > nums[r] % 2:
            nums[l], nums[r] = nums[r], nums[l]

        # If left is even, move left pointer to the right.
        if nums[l] % 2 == 0:
            l += 1
        # If right is odd, move right pointer to the left.
        if nums[r] % 2 == 1:
            r -= 1

    return nums

nums = [3, 1, 2, 4]
print(sort_by_parity(nums))

nums = [0]
print(sort_by_parity(nums))