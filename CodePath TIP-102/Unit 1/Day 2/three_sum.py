'''
Problem 5: Three Sum
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, 
and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

def three_sum(nums):
    pass
    
Example Usage:
nums = [-1, 0, 1, 2, -1, -4]
three_sum(nums)

nums = [0, 1, 1]
three_sum(nums)

nums = [0, 0, 0]
three_sum(nums)

Example Output:
[[-1, -1, 2], [-1, 0, 1]]
[]
[[0, 0, 0]]
'''

def three_sum(nums):
    # We'll sort the array first to make it easier to avoid duplicates and use the two-pointer technique.
    nums.sort()

    result = []
    n = len(nums)
    for i in range(n - 2): # We need at least 3 numbers to have a valid triplet.
        # Skip duplicate values for the 1st number.
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # Next, we use two pointers to find pairs that sum to -nums[i].
        l, r = i + 1, n - 1
        while l < r:
            current_sum = nums[i] + nums[l] + nums[r]
            # If the sum is zero, we found a triplet.
            if current_sum == 0:
                result.append([nums[i], nums[l], nums[r]])
                # Move the left pointer to the right, skipping over duplicates.
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                # Move the right pointer to the left, skipping over duplicates.
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1
                # Move both pointers inward to continue searching.
                l += 1
                r -= 1
            elif current_sum < 0:
                # If the sum is less than zero, we need a larger number, so move the left pointer to the right.
                l += 1
            else:
                # If the sum is greater than zero, we need a smaller number, so move the right pointer to the left.
                r -= 1

    return result

nums = [-1, 0, 1, 2, -1, -4]
print(three_sum(nums))

nums = [0, 1, 1]
print(three_sum(nums))

nums = [0, 0, 0]
print(three_sum(nums))