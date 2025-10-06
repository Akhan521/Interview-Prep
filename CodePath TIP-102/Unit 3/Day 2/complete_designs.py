'''
Problem 6: Time to Complete Each Dream Design
As an architect, you are working on a series of imaginative designs for various dreamscapes. Each design takes a certain 
amount of time to complete, depending on the complexity of the elements involved. You want to know how many days it will take 
for each design to be ready for the next one to begin, assuming each subsequent design is more complex and thus takes more time to finish.

You are given an array design_times where each element represents the time in days needed to complete a particular design. For each design, 
determine the number of days you will have to wait until a more complex design (one that takes more days) is ready to begin. If no such design 
exists for a particular design, return 0 for that position.

Return an array answer such that answer[i] is the number of days you have to wait after the i-th design to start working on a more complex design. 
If there is no future design that is more complex, keep answer[i] == 0 instead.

def time_to_complete_dream_designs(design_times):
    pass
    
Example Usage:
print(time_to_complete_dream_designs([3, 4, 5, 2, 1, 6, 7, 3])) 
print(time_to_complete_dream_designs([2, 3, 1, 4]))  
print(time_to_complete_dream_designs([5, 5, 5, 5]))  

Example Output:
[1, 1, 3, 2, 1, 1, 0, 0]
[1, 2, 1, 0]
[0, 0, 0, 0]
'''

'''
Approach:
We can solve this problem using a stack to keep track of the indices of the designs as we iterate through the list.
- Initialize an empty stack and an answer list filled with zeros.
- Iterate through the design_times list:
  - While the stack is not empty and the current design time is greater than the design time at the index stored at the top of the stack:
    - Pop the index from the stack and calculate the difference between the current index and the popped index to determine how many days to wait.
    - Update the answer list at the popped index with this difference.
  - Push the current index onto the stack.

During each iteration, we ensure that we are only keeping indices of designs that have not yet found a more complex design.
We only pop from the stack when we find a design that is more complex than the one at the index stored at the top of the stack.
'''

def time_to_complete_dream_designs(design_times):
    n = len(design_times)
    answer = [0] * n
    stack = []

    for i in range(n):
        while stack and design_times[i] > design_times[stack[-1]]:
            index = stack.pop()
            answer[index] = i - index
        stack.append(i)

    return answer

print(time_to_complete_dream_designs([3, 4, 5, 2, 1, 6, 7, 3])) 
print(time_to_complete_dream_designs([2, 3, 1, 4]))  
print(time_to_complete_dream_designs([5, 5, 5, 5]))  