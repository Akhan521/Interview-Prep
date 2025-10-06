'''
Problem 5: Designing a Balanced Room
You are designing a room layout represented by a string s consisting of walls '(', ')', and decorations in the form of lowercase English letters.

Your task is to remove the minimum number of walls '(' or ')' in any positions so that the resulting room layout is balanced and return any valid layout.

Formally, a room layout is considered balanced if and only if:

It is an empty room (an empty string), contains only decorations (lowercase letters), or
It can be represented as AB (A concatenated with B), where A and B are valid layouts, or
It can be represented as (A), where A is a valid layout.
def make_balanced_room(s):
    pass
    
Example Usage:
print(make_balanced_room("art(t(d)e)sign)")) 
print(make_balanced_room("d)e(s)ign")) 
print(make_balanced_room("))((")) 

Example Output:
art(t(d)e)sign
# Note: other outputs such as "art(t(d)esign)" would also be considered balanced and valid
de(s)ign
'''

'''
Approach:
We'll use a stack to keep track of the indices of unmatched opening walls '('.
- As we iterate through the string, we'll push the index of each '(' onto the stack.
- When we encounter a ')', we'll check if there's a matching '(' in the stack. If there is, we pop the stack; if not, we mark this ')' for removal.
- After processing the entire string, any indices left in the stack correspond to unmatched '(' that need to be removed.
'''

def make_balanced_room(s):
    # We'll use a list to allow for modifications.
    s = list(s)
    stack = []

    for i, c in enumerate(s):
        # If we encounter an opening wall, push its index onto the stack.
        if c == '(':
            stack.append(i)
        # If we encounter a closing wall, check for a matching opening wall.
        elif c == ')':
            # If there's a matching '(', pop the stack.
            if stack:
                stack.pop()
            else:
                # No matching '(', mark this ')' for removal.
                s[i] = ''

    # Any indices left in the stack correspond to unmatched '(' that need to be removed.
    while stack:
        s[stack.pop()] = ''

    return ''.join(s)

print(make_balanced_room("art(t(d)e)sign)")) 
print(make_balanced_room("d)e(s)ign")) 
print(make_balanced_room("))((")) 