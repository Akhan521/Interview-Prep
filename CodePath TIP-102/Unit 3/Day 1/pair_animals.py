'''
Problem 2: Pair Up Animals for Shelter
In an animal shelter, animals are paired up to share a room. Each pair has a discomfort level, which is the sum of their 
individual discomfort levels. The shelter's goal is to minimize the maximum discomfort level among all pairs to ensure 
that the rooms are as comfortable as possible.

Given a list discomfort_levels representing the discomfort levels of n animals, where n is even, pair up the animals into n / 2 pairs such that:

Each animal is in exactly one pair, and
The maximum discomfort level among the pairs is minimized. Return the minimized maximum discomfort level after optimally pairing up the animals.
Return the minimized maximum comfort level after optimally pairing up the animals.

def pair_up_animals(discomfort_levels):
  pass
  
Example Usage:
print(pair_up_animals([3,5,2,3]))  
print(pair_up_animals([3,5,4,2,4,6])) 

Example Output:
7
8
'''

def pair_up_animals(discomfort_levels):
    # Sort the discomfort levels to facilitate optimal pairing.
    discomfort_levels.sort()

    max_discomfort = 0
    n = len(discomfort_levels)

    # To minimize the maximum discomfort, pair the least uncomfortable animal with the most uncomfortable one.
    l, r = 0, n - 1
    while l < r:
        pair_discomfort = discomfort_levels[l] + discomfort_levels[r]
        max_discomfort = max(max_discomfort, pair_discomfort)
        l += 1
        r -= 1

    return max_discomfort

print(pair_up_animals([3,5,2,3]))  
print(pair_up_animals([3,5,4,2,4,6])) 