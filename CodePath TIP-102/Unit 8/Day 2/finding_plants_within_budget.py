'''
Problem 6: Finding a New Plant Within Budget
You are looking for a new plant and have a max budget. The plant store that you are shopping at stores their inventory in a BST where each node has a 
key representing the price of the plant and value contains the plant's name. Plants are ordered by their prices. You want to find a plant that is close 
to but lower than your budget.

Given the root of the BST inventory and an integer budget, write a function pick_plant() that returns the plant with the highest price below budget. If 
no plant with a price strictly below budget exists, the function should return None.

class TreeNode:
    def __init__(self, key, val, left=None, right=None):
        self.key = key      # Plant price
        self.val = val      # Plant name
        self.left = left
        self.right = right

def pick_plant(inventory, budget):
    pass
    
Example Usage:
"""
               (50, "Fiddle Leaf Fig")
             /                       \
    (25, "Monstera")           (70, "Snake Plant")
       /        \                   /         \
(15, "Aloe")  (40, "Pothos")  (60, "Fern")  (80, "ZZ Plant")
"""

# Using build_tree() function at the top of page
values = [(50, "Fiddle Leaf Fig"), (25, "Monstera"), (70, "Snake Plant"), (15, "Aloe"), 
            (40, "Pothos"), (60, "Fern"), (80, "ZZ Plant")]
inventory = build_tree(values)

print(pick_plant(inventory, 50)) 
print(pick_plant(inventory, 25)) 
print(pick_plant(inventory, 15)) 

Example Output:
Pothos
Aloe
None
'''

from collections import deque
class TreeNode:
    def __init__(self, key, val, left=None, right=None):
        self.key = key      # Plant price
        self.val = val      # Plant name
        self.left = left
        self.right = right

def print_tree(root):
    if not root:
        return "Empty"
    
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    while result and result[-1] is None:
        result.pop()

    print(result)

def build_tree(values):
    if not values:
        return None

    def get_key_value(item):
        if isinstance(item, tuple):
            return item[0], item[1]
        else:
            return None, item

    key, value = get_key_value(values[0])
    root = TreeNode(key, value)
    queue = deque([root])
    index = 1

    while queue:
        node = queue.popleft()
        if index < len(values) and values[index] is not None:
            left_key, left_value = get_key_value(values[index])
            node.left = TreeNode(left_key, left_value)
            queue.append(node.left)
        index += 1
        if index < len(values) and values[index] is not None:
            right_key, right_value = get_key_value(values[index])
            node.right = TreeNode(right_key, right_value)
            queue.append(node.right)
        index += 1

    return root

def pick_plant(inventory, budget):
    '''
    General Approach:
    1. Traverse the BST starting from the root, keeping track of the closest plant found that is below the budget.
    2. If the current node's price is less than the budget, update the closest plant and move to the right subtree.
        - This is because there might be a more expensive plant that is still below the budget in the right subtree.
    3. If the current node's price is greater than or equal to the budget, move to the left subtree.
        - This is because all plants in the right subtree will be more expensive and not within the budget.
    4. Continue this process until you reach a leaf node.
    5. Return the closest plant found that is below the budget, or None if no such plant exists.
    '''
    closest_plant = None
    current_node = inventory
    
    while current_node:
        # Check if the current node's price is less than the budget
        if current_node.key < budget:
            closest_plant = current_node.val 
            current_node = current_node.right  
        else:
            current_node = current_node.left

    return closest_plant

values = [(50, "Fiddle Leaf Fig"), (25, "Monstera"), (70, "Snake Plant"), (15, "Aloe"), 
            (40, "Pothos"), (60, "Fern"), (80, "ZZ Plant")]
inventory = build_tree(values)

print(pick_plant(inventory, 50)) 
print(pick_plant(inventory, 25)) 
print(pick_plant(inventory, 15)) 