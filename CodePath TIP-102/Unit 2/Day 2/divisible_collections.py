'''
Problem 6: Counting Divisible Collections in the Gallery
You have a list of integers collection_sizes representing the sizes of different art collections 
in your gallery and are trying to determine how to group them to best fit in your space. Given an integer k 
write a function count_divisible_collections() that returns the number of non-empty subarrays (contiguous parts of the array) 
where the sum of the sizes is divisible by k.

def count_divisible_collections(collection_sizes, k):
    pass
    
Example Usage:
nums1 = [4, 5, 0, -2, -3, 1]
k1 = 5
nums2 = [5]
k2 = 9

print(count_divisible_collections(nums1, k1))  
print(count_divisible_collections(nums2, k2))  

Example Output:
7
Example 1 Explanation: There are 7 subarrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]

0
'''

'''
Explanation:
Our approach uses prefix sums and a dictionary to count the occurrences of each prefix sum modulo k.

If 2 prefix sums have the same remainder when divided by k, the subarray between these two indices has a sum that is divisible by k.
In other words, let prefix_sum[i] be the sum of the first i elements and prefix_sum[j] be the sum of the first j elements (j > i).
If prefix_sum[i] % k == prefix_sum[j] % k, then prefix_sum[j] - prefix_sum[i] is divisible by k, where prefix_sum[j] - prefix_sum[i]
is the sum of the subarray from index i+1 to j. The reason is that when we subtract 2 numbers w/ the same remainder, the remainders cancel out.
We're then left with a number that is a multiple of k.

For example, if k = 5 and our array is [4, 5], the prefix sums are [4, 9]. 
We could represent 4 as 5 * 0 + 4 (remainder 4) and 9 as 5 * 1 + 4 (remainder 4).
When we subtract 9 - 4, the remainders (4) cancel out, leaving us with 5 * (1 - 0) = 5, which is divisible by k.

We use a dictionary to keep track of how many times each prefix sum modulo k has been seen so far.
If we see the same modulo again, it means we can form new subarrays ending at the current index that are divisible by k
by subtracting the previous prefix sums with the same modulo from the current prefix sum.

We initialize the dictionary with {0: 1} because a prefix sum of 0 (which is divisible by k) can be considered as a valid starting point for subarrays.
It also accounts for subarrays that start from index 0.
'''

def count_divisible_collections(collection_sizes, k):
    if not collection_sizes or k == 0:
        return 0
    
    # Dictionary to store the frequency of each prefix sum modulo k.
    prefix_mod_count = {0: 1} # To account for the subarray that starts from index 0.
    current_sum = 0
    count = 0

    for size in collection_sizes:
        # Update the current prefix sum and its modulo k.
        current_sum += size
        mod = current_sum % k

        # If the current mod has been seen before, it means there are prefix sums from before that when subtracted
        # from the current prefix sum give a sum divisible by k. Thus, we can form subarrays ending at the current index.
        if mod in prefix_mod_count:
            count += prefix_mod_count[mod]
            prefix_mod_count[mod] += 1
        else:
            prefix_mod_count[mod] = 1

    return count

nums1 = [4, 5, 0, -2, -3, 1]
k1 = 5
nums2 = [5]
k2 = 9

print(count_divisible_collections(nums1, k1))  
print(count_divisible_collections(nums2, k2))  