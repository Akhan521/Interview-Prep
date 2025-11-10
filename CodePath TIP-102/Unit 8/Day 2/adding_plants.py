'''
Problem 3: Adding a New Plant to the Collection
You have just purchased a new houseplant and are excited to add it to your collection! Your collection is meticulously organized 
using a Binary Search Tree (BST) where each node in the tree represents a houseplant in your collection, and houseplants are organized 
alphabetically by name (val).

Given the root of your BST collection and a new houseplant name, insert a new node with value name into your collection. Return the root 
of your updated collection. If another plant with name already exists in the tree, add the new node in the existing node's right subtree.

Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution 
has the stated time and space complexity. Assume the input tree is balanced when calculating time and space complexity.

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def add_plant(collection, name):
    pass
    
Example Usage:
"""
            Money Tree
        /              \
Fiddle Leaf Fig    Snake Plant
"""

# Using build_tree() function at the top of page
values = ["Money Tree", "Fiddle Leaf Fig", "Snake Plant"]
collection = build_tree(values)

# Using print_tree() function at the top of page
print_tree(add_plant(collection, "Aloe"))

Example Output:
['Money Tree', 'Fiddle Leaf Fig', 'Snake Plant', 'Aloe']

Explanation: 
Tree should have the following structure:
           Money Tree
        /              \
 Fiddle Leaf Fig   Snake Plant
   /
 Aloe
'''

from collections import deque
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
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
        root = insert_into_bst(root, value)
    
    return root

def add_plant(collection, name):
    # Insert the new plant name into the BST collection.
    return insert_into_bst(collection, name)

values = ["Money Tree", "Fiddle Leaf Fig", "Snake Plant"]
collection = build_bst_tree(values)

# Using print_tree() function at the top of page
print_tree(add_plant(collection, "Aloe"))