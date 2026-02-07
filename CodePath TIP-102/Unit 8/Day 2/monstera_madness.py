'''
Problem 1: Monstera Madness
Given the root of a binary tree where each node represents the number of splits in a leaf of a Monstera plant, return the number of Monstera leaves 🍃 
that have an odd number of splits.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity.

Note: The term leaf in this problem refers to the plant leaf 🍃 of a Monstera plant, not the type of node leaf nodes which are nodes with no children.

class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right
         
def count_odd_splits(root):
    pass
    
Example Usage:
"""
      2
     / \
    /   \
   3     5
  / \     \
 6   7     12
"""

# Using build_tree() function included at top of page
values = [2, 3, 5, 6, 7, None, 12]
monstera = build_tree(values)

print(count_odd_splits(monstera))
print(count_odd_splits(None))

Example Output:
3
Example 1 Explanation: Three Monstera leaves (nodes) have an odd number of fenestrations (3, 5, and 7).
0
'''

from collections import deque
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(values):
    if not values:
        return None

    def get_key_value(item):
        if isinstance(item, tuple):
            return item[0], item[1]
        else:
            return None, item

    key, value = get_key_value(values[0])
    root = TreeNode(value, key)
    queue = deque([root])
    index = 1

    while queue:
        node = queue.popleft()
        if index < len(values) and values[index] is not None:
            left_key, left_value = get_key_value(values[index])
            node.left = TreeNode(left_value, left_key)
            queue.append(node.left)
        index += 1
        if index < len(values) and values[index] is not None:
            right_key, right_value = get_key_value(values[index])
            node.right = TreeNode(right_value, right_key)
            queue.append(node.right)
        index += 1

    return root

def count_odd_splits(root):
    '''
    Counts the number of nodes in a binary tree that have an odd value.

    General Approach:
    1. If the root is None, return 0 (base case).
    2. Initialize a count variable to 0.
    3. If the value of the current node is odd, increment the count by 1.
    4. Recursively call the function on the left and right subtrees and add their results to the count.
    5. Return the total count.
    '''
    if not root:
        return 0
    
    count = 1 if root.val % 2 != 0 else 0
    count += count_odd_splits(root.left)
    count += count_odd_splits(root.right)

    return count

values = [2, 3, 5, 6, 7, None, 12]
monstera = build_tree(values)

print(count_odd_splits(monstera))
print(count_odd_splits(None))