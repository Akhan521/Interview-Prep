'''
Problem Description:

    Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements
    of nums except nums[i].The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
    You must write an algorithm that runs in O(n) time and without using the division operation.

Examples:

    Input: nums = [1,2,3,4]
    Output: [24,12,8,6]

    Input: nums = [-1,1,0,-3,3]
    Output: [0,0,9,0,0]

Constraints:

    * 2 <= nums.length <= 105
    * -30 <= nums[i] <= 30
    * The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.

Approach:

    We can solve this by utilizing prefix and suffix products. We'll iterate over our array as we calculate
    the prefix products at every index. Thereafter, we can iterate over our array in reverse to calculate
    the suffix products and multiply them with the corresponding prefix products.

    For example:
    - nums =  [1,  2,  3, 4]:
    - Prefix: [1,  1,  2, 6]
    - Suffix: [24, 12, 4, 1]
'''

from typing import List
def productExceptSelf(nums: List[int]) -> List[int]:
    n = len(nums)
    res = [1] * n

    # Calculate prefix products.
    prefix = 1
    for i in range(n):
        res[i] = prefix
        prefix *= nums[i]

    # Calculate suffix products and multiply with prefix.
    suffix = 1
    for i in reversed(range(n)):
        res[i] *= suffix
        suffix *= nums[i]

    return res