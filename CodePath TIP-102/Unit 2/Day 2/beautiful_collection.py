'''
Problem 5: Beautiful Collection
Your gallery has entered a competition for the most beautiful collection. Your collection is represented by a 
string collection where each artist in your gallery is represented by a character. The beauty of a collection is 
defined as the difference in frequencies between the most frequent and least frequent characters.

For example, the beauty of "abaacc" is 3 - 1 = 2.
Given a string collection, write a function beauty_sum() that returns the sum of beauty of all of its substrings 
(subcollections), not just of the collection itself.

def beauty_sum(collection):
    pass
    
Example Usage:
print(beauty_sum("aabcb")) 
print(beauty_sum("aabcbaa"))

Example Output:
5
Example 1 Explanation: The substrings with non-zero beauty are 
["aab","aabc","aabcb","abcb","bcb"], each with beauty equal to 1.

17
'''

def beauty_sum(collection):
    if not collection:
        return 0
    
    total_beauty = 0
    n = len(collection)

    # Iterate over all possible substrings:
    for i in range(n):
        # Dictionary to count frequency of characters in the current substring.
        freq = {}
        for j in range(i, n):
            # Update the frequency of the current character.
            char = collection[j]
            freq[char] = freq.get(char, 0) + 1
            # Calculate the beauty of the current substring.
            max_freq = max(freq.values())
            min_freq = min(freq.values())
            total_beauty += max_freq - min_freq

    return total_beauty

print(beauty_sum("aabcb")) 
print(beauty_sum("aabcbaa"))