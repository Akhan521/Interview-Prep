'''
Problem 7: Next Greater Element
You are designing a sequence of dream elements, each represented by a number. The sequence is circular, meaning that 
the last element is followed by the first. Your task is to determine the next greater dream element for each element in the sequence.

The next greater dream element for a dream element x is the first element that is greater than x when traversing the sequence in its 
natural circular order. If no such dream element exists, return -1 for that dream element.

def next_greater_dream(dreams):
    pass
    
Example Usage:
print(next_greater_dream([1, 2, 1])) 
print(next_greater_dream([1, 2, 3, 4, 3])) 

Example Output:
[2, -1, 2]
[2, 3, 4, -1, 4]
'''

'''
Approach:
We can solve this problem using a stack to keep track of the indices of elements that we haven't found a next greater element for yet.
We will iterate through the list twice (to simulate the circular nature) and use the stack to check for the next greater element.
- Initialize an empty stack and a result list filled with -1.
- Iterate through the list twice (using modulo to wrap around):
  - While the stack is not empty and the current element is greater than the element at the index stored at the top of the stack:
    - Pop the index from the stack and update the result list at that index with the current element.
  - If we are in the first pass (i < n), push the current index onto the stack.

This approach ensures that we only keep indices of elements that have not yet found a next greater element in the stack.
We only pop from the stack when we find a greater element than the one at the index stored at the top of the stack.
'''

def next_greater_dream(dreams):
    n = len(dreams)
    result = [-1] * n 
    stack = []

    for i in range(2 * n):
        while stack and dreams[i % n] > dreams[stack[-1]]:
            index = stack.pop()
            result[index] = dreams[i % n]
        if i < n:
            stack.append(i)

    return result

print(next_greater_dream([1, 2, 1])) 
print(next_greater_dream([1, 2, 3, 4, 3])) 