'''
Problem 4: Maximum Tiers in Cake II
If you solved max_tiers() in the previous problem using a depth first search approach, reimplement your solution using a breadth first 
search approach. If you implemented it using a breadth first search approach, use a depth first search approach.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the 
stated time complexity. Assume the input tree is balanced when calculating time complexity.

class TreeNode():
     def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def max_tiers(cake):
    pass
    
Example Usage:
"""
        Chocolate
        /        \
    Vanilla    Strawberry
                /     \
         Chocolate    Coffee
"""
# Using build_tree() function included at top of page
cake_sections = ["Chocolate", "Vanilla", "Strawberry", None, None, "Chocolate", "Coffee"]
cake = build_tree(cake_sections)

print(max_tiers(cake))

Example Output:
3
'''

from collections import deque
class TreeNode():
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

def max_tiers(cake):
    '''
    Plan:
    1. If the cake is empty, return 0.
    2. Initialize a queue for BFS and add the root node to it.
    3. Initialize a variable to keep track of the maximum depth (tiers).
    4. While the queue is not empty:
        a. Get the number of nodes at the current level.
        b. For each node at this level, add its children to the queue.
        c. Increment the level counter after processing all nodes at the current level.
    5. Return the maximum depth (tiers).
    '''
    if not cake:
        return 0
    
    queue = deque([cake])
    max_depth = 0

    while queue:
        level_size = len(queue)

        for _ in range(level_size):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        # We have finished processing one level
        max_depth += 1

    return max_depth

cake_sections = ["Chocolate", "Vanilla", "Strawberry", None, None, "Chocolate", "Coffee"]
cake = build_tree(cake_sections)

print(max_tiers(cake))