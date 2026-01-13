'''
Problem 2: Pumpkin Patch Path
Leaning into the haunted hotel aesthetic, you've begun growing a pumpkin patch behind the hotel for the upcoming Halloween season. Given the root of 
a binary tree where each node represents a section of a pumpkin patch with a certain number of pumpkins, find the root-to-leaf path that yields the 
largest number of pumpkins. Return a list of the node values along the maximum pumpkin path.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity.

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def max_pumpkins_path(root):
    pass
    
Example Usage:
"""
    7
   / \
  3   10
 /   /  \
1   5    15
"""
# Using build_tree() function includedd at the top of the page
pumpkin_quantities = [7, 3, 10, 1, None, 5, 15]
root1 = build_tree(pumpkin_quantities)

"""
    12
   /  \
  3     8
 / \     \
4   50    10
"""
pumpkin_quantities = [12,3, 8, 4, 50, None, 10]
root2 = build_tree(pumpkin_quantities)

print(max_pumpkins_path(root1)) 
print(max_pumpkins_path(root2))  

Example Output:
[7, 10, 15]
[12, 3, 50]
'''

from collections import deque
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
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

def max_pumpkins_path(root):
    '''
    General Idea:
    We'll recursively explore all root-to-leaf paths in the binary tree. For each node, we'll determine the max pumpkin path from the current node
    by comparing the max paths from its left and right children. We'll keep track of the path with the maximum sum of pumpkins and return that path.

    Plan:
    1. If root is None, return an empty list.
    2. Recursively find the max pumpkin path for the left and right subtrees.
    3. Compare the sums of the left and right paths, and choose the one with the greater sum.
    4. Prepend the current node's value to the chosen path and return it.
    '''
    if root is None:
        return []
    
    left_path = max_pumpkins_path(root.left)
    right_path = max_pumpkins_path(root.right)

    left_sum = sum(left_path)
    right_sum = sum(right_path)
    if left_sum > right_sum:
        return [root.val] + left_path
    else:
        return [root.val] + right_path
    
pumpkin_quantities = [7, 3, 10, 1, None, 5, 15]
root1 = build_tree(pumpkin_quantities)

"""
    12
   /  \
  3     8
 / \     \
4   50    10
"""
pumpkin_quantities = [12,3, 8, 4, 50, None, 10]
root2 = build_tree(pumpkin_quantities)

print(max_pumpkins_path(root1)) 
print(max_pumpkins_path(root2))  