'''
Problem 3: Dream Corridor Design
You are an architect designing a corridor for a futuristic dream space. The corridor is represented by 
a list of integer values where each value represents the width of a segment of the corridor. Your goal is to find 
two segments such that the corridor formed between them (including the two segments) has the maximum possible area. 
The area is defined as the minimum width of the two segments multiplied by the distance between them.

You need to return the maximum possible area that can be achieved.

def max_corridor_area(segments):
    pass
    
Example Usage:
print(max_corridor_area([1, 8, 6, 2, 5, 4, 8, 3, 7])) 
print(max_corridor_area([1, 1])) 

Example Output:
49
1
'''

def max_corridor_area(segments):
    # Initialize two pointers and the maximum area variable.
    l, r = 0, len(segments) - 1
    max_area = 0

    # Use a two-pointer approach to find the maximum area.
    while l < r:
        # Calculate the area formed by the two segments at the pointers.
        height = min(segments[l], segments[r])
        width = r - l
        current_area = height * width
        max_area = max(max_area, current_area)

        # Move the pointer pointing to the shorter segment inward (to potentially find a taller segment).
        if segments[l] < segments[r]:
            l += 1
        else:
            r -= 1

    return max_area

print(max_corridor_area([1, 8, 6, 2, 5, 4, 8, 3, 7])) 
print(max_corridor_area([1, 1])) 