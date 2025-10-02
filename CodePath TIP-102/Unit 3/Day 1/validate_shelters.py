'''
Problem 6: Validate Animal Sheltering Sequence
Given two integer arrays admitted and adopted each with distinct values representing animals in an animal shelter, 
return True if this could have been the result of a sequence of admitting and adopting animals from the shelter, or False otherwise.

def validate_shelter_sequence(admitted, adopted):
  pass
  
Example Usage:
print(validate_shelter_sequence([1,2,3,4,5], [4,5,3,2,1]))
print(validate_shelter_sequence([1,2,3,4,5], [4,3,5,1,2])) 

Example Output:
True
False
'''

def validate_shelter_sequence(admitted, adopted):
    # Use a stack to simulate the shelter's admit and adopt process.
    stack = []

    j = 0  # Pointer for the adopted array (track which animal to adopt next).
    for animal in admitted:
        # Admit the animal into the shelter (push onto the stack).
        stack.append(animal)

        # While the top of the stack matches the next animal to be adopted, adopt it (pop from the stack).
        while stack and stack[-1] == adopted[j]:
            stack.pop()
            j += 1

    # If all adopted animals have been matched, the sequence is valid.
    return j == len(adopted)

print(validate_shelter_sequence([1,2,3,4,5], [4,5,3,2,1]))
print(validate_shelter_sequence([1,2,3,4,5], [4,3,5,1,2])) 