'''
Problem 4: Append Animals to Include Preference
You are managing an animal adoption center. You have:

A string available, representing the animals currently available for adoption.
A string preferred, representing a customer's preferred sequence of animals.
You want to make sure the preferred sequence appears as a subsequence of available. 
A subsequence means the characters appear in order, but not necessarily consecutively.

To achieve this, you are allowed to append characters to the end of available. You cannot remove characters or insert them elsewhere.

Return the minimum number of characters you need to append to the end of available so that preferred becomes a subsequence.

def append_animals(available, preferred):
  pass
  
Example Usage:
print(append_animals("catsdogs", "cows")) 
print(append_animals("rabbit", "r")) 
print(append_animals("fish", "bird"))

Example Output:
2
0
4

Explanation:
available = "catsdogs" preferred = "cows"
'c' → found at index 0
'o' → found at index 5
'w' → not present
's' → not present

You need to append "ws" to the end to complete the subsequence. Minimum characters to append: 2
'''

def append_animals(available, preferred):
    # Initialize pointers for both strings.
    i, j = 0, 0

    while i < len(available) and j < len(preferred):
        # If the characters match, we've found a part of the subsequence.
        if available[i] == preferred[j]:
            j += 1 # Move to the next character in preferred.
        # Always move to the next character in available.
        i += 1 

    # If we reached the end of preferred, it means we found a subsequence (j == len(preferred)).
    # Otherwise, we need to append the remaining characters in preferred.
    return max(0, len(preferred) - j)

print(append_animals("catsdogs", "cows")) 
print(append_animals("rabbit", "r")) 
print(append_animals("fish", "bird"))