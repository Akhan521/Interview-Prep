'''
Problem 2: Build the Tallest Skyscraper
You are given an array floors representing the heights of different building floors. 
Your task is to design a skyscraper using these floors, where each floor must be placed on top of 
a floor with equal or greater height. However, you can only start a new skyscraper when necessary, 
meaning when no more floors can be added to the current skyscraper according to the rules.

Return the number of skyscrapers you can build using the given floors.

def build_skyscrapers(floors):
    pass
    
Example Usage:
print(build_skyscrapers([10, 5, 8, 3, 7, 2, 9])) 
print(build_skyscrapers([7, 3, 7, 3, 5, 1, 6]))  
print(build_skyscrapers([8, 6, 4, 7, 5, 3, 2])) 

Example Output:
4 -> 10, (5, 8)
4
2
'''

def build_skyscrapers(floors):
    stack = []
    skyscrapers = 0

    # Iterate through each floor:
    for floor in floors:
        # If the stack is empty, we need to start a new skyscraper.
        if not stack:
            skyscrapers += 1
            stack.append(floor)
            
        # We can build on top of the current skyscraper if the new floor is less than or equal to the top floor.
        elif floor <= stack[-1]:
            stack.append(floor)

        # If the new floor is taller than the top floor, we need to pop floors until we can place the new floor or start a new skyscraper.
        else:
            while stack and floor > stack[-1]:
                stack.pop()
            stack.append(floor)
            skyscrapers += 1

    return skyscrapers

print(build_skyscrapers([10, 5, 8, 3, 7, 2, 9])) 
print(build_skyscrapers([7, 3, 7, 3, 5, 1, 6]))  
print(build_skyscrapers([8, 6, 4, 7, 5, 3, 2]))