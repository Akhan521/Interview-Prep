'''
Problem 1: Find Millenium Falcon Part I
Han Solo's ship, the Millenium Falcon, has broken down and he's searching for a specific replacement part. 
As a repair shop owner helping him out, write a function check_stock() that takes in a sorted list inventory 
where each element is an integer ID of a part you stock in your shop, and an integer part_id representing the 
integer ID of the part Han Solo is looking for. Return True if the part_id is in inventory and False otherwise.

Your solution must have O(log n) time complexity.

def check_stock(inventory, part_id):
    pass
    
Example Usage:
print(check_stock([1, 2, 5, 12, 20], 20))
print(check_stock([1, 2, 5, 12, 20], 100))

Example Ouput:
True
False
'''

def check_stock(inventory, part_id):
    l,r = 0, len(inventory) - 1

    while l <= r:
        mid = (l + r) // 2
        if inventory[mid] == part_id:
            return True
        elif inventory[mid] < part_id:
            l = mid + 1
        else:
            r = mid - 1

    return False

print(check_stock([1, 2, 5, 12, 20], 20))
print(check_stock([1, 2, 5, 12, 20], 100))