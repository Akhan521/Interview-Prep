'''
Problem 2: Find Millenium Falcon Part II
If you implemented your check_stock() function from the previous problem iteratively, implement it recursively. 
If you implemented it recursively, implement it iteratively.

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
    def binary_search(l, r):
        # Base case: If the search range is invalid...
        if l > r:
            return False
        
        mid = (l + r) // 2
        if inventory[mid] == part_id:
            return True
        elif inventory[mid] < part_id:
            return binary_search(mid + 1, r)
        else:
            return binary_search(l, mid - 1)
        
    return binary_search(0, len(inventory) - 1)

print(check_stock([1, 2, 5, 12, 20], 20))
print(check_stock([1, 2, 5, 12, 20], 100))