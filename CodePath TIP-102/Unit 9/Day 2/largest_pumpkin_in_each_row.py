'''
Problem 3: Largest Pumpkin in each Row
Given the root of a binary tree pumpkin_patch where each node represents a pumpkin in the patch and each node value represents the pumpkin's size, 
return an array of the largest pumpkin in each row of the pumpkin patch. Each level in the tree represents a row of pumpkins.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity.

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def largest_pumpkins(pumpkin_patch):
    pass
    
Example Usage:
"""
    1
   /  \
  3    2
 / \    \   
5   3    9
"""
# Using build_tree() function included at the top of the page
pumpkin_sizes = [1, 3, 2, 5, 3, None, 9]
pumpkin_patch = build_tree(pumpkin_sizes)

print(largest_pumpkins(pumpkin_patch))

Example Output:
[1, 3, 9]
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

def largest_pumpkins(pumpkin_patch):
    '''
    Plan:
    1. Initialize an empty list `largest_pumpkins` to store the largest pumpkin size at each level.
    2. Use a queue to perform a level-order traversal (BFS) of the binary tree.
    3. For each level, track the maximum pumpkin size found.
    4. Append the maximum size of each level to the `largest_pumpkins` list.
    5. Return the `largest_pumpkins` list after traversing all levels.
    '''
    if not pumpkin_patch:
        return []
    
    largest_pumpkins = []
    queue = deque([pumpkin_patch])

    while queue:
        level_size = len(queue)
        max_size = float('-inf')
        
        for _ in range(level_size):
            node = queue.popleft()
            max_size = max(max_size, node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        largest_pumpkins.append(max_size)

    return largest_pumpkins

pumpkin_sizes = [1, 3, 2, 5, 3, None, 9]
pumpkin_patch = build_tree(pumpkin_sizes)

print(largest_pumpkins(pumpkin_patch))