'''
Problem 7: Calculate Fabric Waste
In the sustainable fashion industry, minimizing waste is crucial. After cutting out patterns for clothing items, there are often 
leftover pieces of fabric that cannot be used. Your task is to calculate the total amount of fabric waste generated after producing 
a collection of clothing items. Each clothing item requires a certain amount of fabric, and the available fabric rolls come in fixed lengths.

Write the calculate_fabric_waste() function, which takes a list of clothing items (each with a required fabric length) and a list of 
fabric rolls (each with a specific length). The function should return the total fabric waste after producing all the items.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution 
has the stated time and space complexity.

def calculate_fabric_waste(items, fabric_rolls):
    pass
    
Example Usage:
items = [("T-Shirt", 2), ("Pants", 3), ("Jacket", 5)]
fabric_rolls = [5, 5, 5]

items_2 = [("Dress", 4), ("Skirt", 3), ("Blouse", 2)]
fabric_rolls = [4, 4, 4]

items_3 = [("Jacket", 6), ("Shirt", 2), ("Shorts", 3)]
fabric_rolls = [7, 5, 5]

print(calculate_fabric_waste(items, fabric_rolls))
print(calculate_fabric_waste(items_2, fabric_rolls))
print(calculate_fabric_waste(items_3, fabric_rolls))

Example Output:
5
3
6
'''

def calculate_fabric_waste(items, fabric_rolls):
    # Sort fabric rolls in descending order to use the largest rolls first.
    fabric_rolls.sort(reverse=True)

    total_waste = 0
    # Iterate through each clothing item's required fabric length and allocate fabric from the rolls.
    for _, required_length in items:
        # Find a fabric roll that can accommodate the required length.
        for i in range(len(fabric_rolls)):
            if fabric_rolls[i] >= required_length:
                # Calculate waste for this item.
                waste = fabric_rolls[i] - required_length
                total_waste += waste
                # Mark this roll as used by setting its length to 0.
                fabric_rolls[i] = 0
                break

    return total_waste

# Time Complexity: O(n log n + m), where n is the number of fabric rolls and m is the number of items.
# Space Complexity: O(1) additional space, as we are modifying the input list in place.

items = [("T-Shirt", 2), ("Pants", 3), ("Jacket", 5)]
fabric_rolls = [5, 5, 5]
print(calculate_fabric_waste(items, fabric_rolls))

items_2 = [("Dress", 4), ("Skirt", 3), ("Blouse", 2)]
fabric_rolls = [4, 4, 4]
print(calculate_fabric_waste(items_2, fabric_rolls))

items_3 = [("Jacket", 6), ("Shirt", 2), ("Shorts", 3)]
fabric_rolls = [7, 5, 5]
print(calculate_fabric_waste(items_3, fabric_rolls))