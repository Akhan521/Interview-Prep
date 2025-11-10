'''
Problem 2: Flower Finding
You are looking to buy a new flower plant for your garden. The nursery you visit stores its inventory in a binary search tree (BST) 
where each node represents a plant in the store. The plants are organized according to their names (vals) in alphabetical order in the BST.

Given the root of the binary search tree inventory and a target flower name, write a function find_flower() that returns True if the 
flower is present in the garden and False otherwise.

Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution 
has the stated time and space complexity. Assume the input tree is balanced when calculating time and space complexity.

class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right
         
def find_flower(inventory, name):
    pass
    
Example Usage:
"""
         Rose
        /    \
      Lily   Tulip
     /  \       \
  Daisy  Lilac  Violet
"""

# using build_tree() function at top of page
values = ["Rose", "Lily", "Tulip", "Daisy", "Lilac", None, "Violet"]
garden = build_tree(values)

print(find_flower(garden, "Lilac"))  
print(find_flower(garden, "Sunflower")) 

Example Output:
True
False
'''

from collections import deque
class TreeNode():
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def insert_into_bst(root, value):
    # Helper function to insert a value into the BST.
    
    # Base case: found a spot to insert the new node.
    if root is None:
        return TreeNode(value)
    
    if value < root.val:
        # Insert into the left subtree and assign it back to root.left to maintain the tree structure.
        root.left = insert_into_bst(root.left, value)
    else:
        # Insert into the right subtree and assign it back to root.right to maintain the tree structure.
        root.right = insert_into_bst(root.right, value)
    
    return root

def build_bst_tree(values):
    # Build a BST from a list of values.
    root = None
    for value in values:
        if value is not None:
            root = insert_into_bst(root, value)

    return root

def find_flower(inventory, name):
    if inventory is None:
        return False
    
    if inventory.val == name:
        return True
    elif name < inventory.val:
        return find_flower(inventory.left, name)
    else:
        return find_flower(inventory.right, name)
"""    
Time Complexity: 
O(H) where H is the height of the tree. In the worst case, this is O(N) for a skewed tree, but in the average case for a balanced BST, it's O(log N).

Space Complexity: 
O(H) due to the recursive call stack, which is also O(N) in the worst case and O(log N) in the average case.
"""
    
values = ["Rose", "Lily", "Tulip", "Daisy", "Lilac", None, "Violet"]
garden = build_bst_tree(values)

print(find_flower(garden, "Lilac"))  
print(find_flower(garden, "Sunflower"))