'''
Problem 7: Longest Substring With at Least K Repeating Characters
Given a string s and an integer k, use a divide and conquer approach to return the length of the longest substring of s such that 
the frequency of each character in substring is greater than or equal to k.

If no such substring exists, return 0.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution 
has the stated time and space complexity.

def longest_substring(s, k):
    pass
    
Example Usage:
print(longest_substring("tatooine", 2))
print(longest_substring("chewbacca", 2))

Example Output:
2
Example 1 Explanation: The longest substring is 'oo' as 'o' is repeated 2 times.
4
Example 2 Explanation: The longest substring is 'acca' as both 'a' and 'c' are repeated 2 times.
'''

def longest_substring(s, k):
    '''
    Plan:
    1. Define a helper function that takes in the string and the k value.
        - If the string length is less than k, return 0.
        - Count the frequency of each character in the string.
        - If all characters meet the frequency requirement, return the length of the string.
        - Otherwise, split the string at characters that do not meet the requirement and recursively call the helper function on each substring.
        - The reason we split at characters that do not meet the requirement is that any valid substring cannot contain these characters.
    2. Return the maximum length found from the recursive calls.
    3. Call the helper function with the original string and k value.
    '''
    def divide_and_conquer(s, k):
        if len(s) < k:
            return 0
        
        # Count frequency of each character:
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        # Check if all characters meet the frequency requirement:
        for char in char_count:
            # If a character appears less than k times, we consider substrings that exclude this character:
            if char_count[char] < k:
                # Split the string at this character and recursively check each substring:
                return max(divide_and_conquer(subs, k) for subs in s.split(char))
            
        # If all characters meet the requirement, return the length of the string:
        return len(s)
    
    return divide_and_conquer(s, k)

print(longest_substring("tatooine", 2))
print(longest_substring("chewbacca", 2))