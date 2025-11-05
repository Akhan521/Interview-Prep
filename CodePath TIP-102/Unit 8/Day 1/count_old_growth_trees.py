'''
Problem 7: Count Old Growth Trees
Given the root of a binary tree where each node represents the age of a tree in a forest, write a function count_old_growth() 
that returns the number of old growth trees in the forest. A tree is considered old growth if it has age greater than threshold.

Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution 
has the stated time and space complexity. Assume the input tree is balanced when calculating time and space complexity.

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def count_old_growth(root, threshold):
    pass 
    
Example Usage:
"""
     100
     /  \
    /    \
  1200  1500
  /     /  \
20    700  2600
"""

forest = TreeNode(100, 
                  TreeNode(1200, TreeNode(20))
                          TreeNode(1500, TreeNode(700), TreeNode(2600)))

print(count_old_growth(forest, 1000))

Example Output:
3
'''

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def count_old_growth(root, threshold):
    if not root:
        return 0
    
    count = 1 if root.val > threshold else 0
    
    count += count_old_growth(root.left, threshold)
    count += count_old_growth(root.right, threshold)
    
    return count

"""
     100
     /  \
    /    \
  1200  1500
  /     /  \
20    700  2600
"""

forest = TreeNode(100, 
                  TreeNode(1200, TreeNode(20)),
                          TreeNode(1500, TreeNode(700), TreeNode(2600)))

print(count_old_growth(forest, 1000))