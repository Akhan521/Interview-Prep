'''
Problem 4: Dream Building Layout
You are an architect tasked with designing a dream building layout. The building layout is represented by a 
string s of even length n. The string consists of exactly n / 2 left walls '[' and n / 2 right walls ']'.

A layout is considered balanced if and only if:

It is an empty space, or
It can be divided into two separate balanced layouts, or
It can be surrounded by left and right walls that balance each other out.
You may swap the positions of any two walls any number of times.

Return the minimum number of swaps needed to make the building layout balanced.

def min_swaps(s):
    pass
    
Example Usage:
print(min_swaps("][][")) 
print(min_swaps("]]][[[")) 
print(min_swaps("[]"))  

Example Output:
1
2
0
'''

'''
Approach:
We'll iterate through the string while maintaining a balance counter.
- When we encounter a left wall '[', we increment the balance.
- When we encounter a right wall ']', we decrement the balance.
- If at any point the balance becomes negative, it indicates an unmatched right wall, and we need a swap to fix it.

Note: The minimum number of swaps needed to balance the layout is equal to half the number of unmatched right walls encountered during the iteration.
This is because each swap can fix two unmatched walls (one left and one right). Recall that the string has an equal number of left and right walls.
'''

def min_swaps(s):
    balance = 0
    swaps = 0

    # Iterate through each character in the string.
    for c in s:
        if c == '[':
            balance += 1
        else:  # c == ']'
            balance -= 1

        # If our balance goes negative, we have an unmatched right wall.
        if balance < 0:
            swaps += 1
            balance = 0  # Reset balance after a swap

    return (swaps + 1) // 2  # Each swap can fix two unmatched walls.

print(min_swaps("][][")) 
print(min_swaps("]]][[[")) 
print(min_swaps("[]"))