'''
Problem 4: Sum Inventory
A local flower shop stores its inventory in a binary tree, where each node represents their current stock of a flower variety. 
Given the root of a binary tree inventory, return the sum of all the flower stock in the store.

Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution 
has the stated time and space complexity. Assume the input tree is balanced when calculating time and space complexity.

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def sum_inventory(inventory):
    pass
    
Example Usage:
"""
     40
    /  \
   5   10
  /   /  \
20   1   30
"""

inventory = TreeNode(40, 
                    TreeNode(5, TreeNode(20)),
                            TreeNode(10, TreeNode(1), TreeNode(30)))

print(sum_inventory(inventory))

Example Output:
106
'''

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def sum_inventory(inventory):
    if not inventory:
        return 0
    
    left_sum = sum_inventory(inventory.left)
    right_sum = sum_inventory(inventory.right)

    return inventory.val + left_sum + right_sum

"""
     40
    /  \
   5   10
  /   /  \
20   1   30
"""

inventory = TreeNode(40, 
                    TreeNode(5, TreeNode(20)),
                            TreeNode(10, TreeNode(1), TreeNode(30)))

print(sum_inventory(inventory))