'''
Problem 8: Fabric Roll Organizer
You need to organize fabric rolls for optimal usage. Each fabric roll has a specific length, and you want to group them into pairs so 
that the difference between the lengths of the rolls in each pair is minimized. If there's an odd number of rolls, one roll will be left out.

Write the organize_fabric_rolls() function, which takes a list of fabric roll lengths and returns a list of pairs of fabric roll lengths, 
where the difference in lengths between the rolls is minimized. If there's an odd number of rolls, the last roll should be returned separately.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has 
the stated time and space complexity.

def organize_fabric_rolls(fabric_rolls):
    pass
    
Example Usage:
fabric_rolls = [15, 10, 25, 30, 22]
fabric_rolls_2 = [5, 8, 10, 7, 12, 14]
fabric_rolls_3 = [40, 10, 25, 15, 30]

print(organize_fabric_rolls(fabric_rolls))
print(organize_fabric_rolls(fabric_rolls_2))
print(organize_fabric_rolls(fabric_rolls_3))

Example Output:
[(10, 15), (22, 25), 30]
[(5, 7), (8, 10), (12, 14)]
[(10, 15), (25, 30), 40]
'''

def organize_fabric_rolls(fabric_rolls):
    # To minimize the difference between lengths, we first sort the list of fabric rolls.
    fabric_rolls.sort()

    pairs = []
    n = len(fabric_rolls)

    # Iterate through the sorted list in steps of 2 to form pairs.
    for i in range(0, n - 1, 2):
        pairs.append((fabric_rolls[i], fabric_rolls[i + 1]))

    # If there's an odd number of rolls, append the last roll separately.
    if n % 2 != 0:
        pairs.append(fabric_rolls[-1])

    return pairs

fabric_rolls = [15, 10, 25, 30, 22]
fabric_rolls_2 = [5, 8, 10, 7, 12, 14]
fabric_rolls_3 = [40, 10, 25, 15, 30]

print(organize_fabric_rolls(fabric_rolls))
print(organize_fabric_rolls(fabric_rolls_2))
print(organize_fabric_rolls(fabric_rolls_3))