'''
Problem 3: Rearrange Animals and Slogans
You are given a string s that consists of lowercase English letters representing animal names or slogans and brackets. 
The goal is to rearrange the animal names or slogans in each pair of matching parentheses by reversing them, starting from the innermost pair.

After processing, your result should not contain any brackets.

def rearrange_animal_names(s):
  pass
  
Example Usage:
print(rearrange_animal_names("(dribtacgod)"))
print(rearrange_animal_names("(!(love(stac))I)")) 
print(rearrange_animal_names("adopt(yadot(a(tep)))!")) 

Example Output:
dogcatbird
Ilovecats!
adoptapettoday!
'''

def rearrange_animal_names(s):
    # Use a stack to handle nested parentheses and reversals.
    stack = []

    for char in s:
        # When we encounter a closing parenthesis, we need to pop from the stack until we find the matching opening parenthesis.
        if char == ')':
            reversed = ""
            while stack and stack[-1] != '(':
                reversed += stack.pop()
            # Pop the opening parenthesis from the stack.
            if stack:
                stack.pop()

            # Push the reversed string back onto the stack.
            for c in reversed:
                stack.append(c)
        else:
            # For any other character (including opening parenthesis), just push it onto the stack.
            stack.append(char)

    # After processing all characters, the stack will contain the final rearranged string.
    return "".join(stack)

print(rearrange_animal_names("(dribtacgod)"))
print(rearrange_animal_names("(!(love(stac))I)")) 
print(rearrange_animal_names("adopt(yadot(a(tep)))!")) 
