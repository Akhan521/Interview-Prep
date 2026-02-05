'''
Problem 3: Sweetness Difference
You are given the root of a binary tree chocolates where each node represents a chocolate in a box of chocolates and each node value 
represents the sweetness level of the chocolate. Write a function that returns a list of the absolute differences between the highest 
and lowest sweetness levels in each row of the chocolate box.

The sweetness difference in a row with only one chocolate is 0.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the 
stated time complexity.

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def sweet_difference(chocolates):
    pass
    
Example Usage:
"""
  3
 / \
9  20
   / \
  15  7
"""
# Using build_tree() function included at top of page
sweetness_levels1 = [3, 9, 20, None, None, 15, 7]
chocolate_box1 = build_tree(sweetness_levels)

"""
    1
   / \
  2   3
 / \   \
4   5   6

"""
sweetness_levels2 = [1, 2, 3, 4, 5, None, 6]
chocolate_box2 = build_tree(sweetness_levels)

print(sweet_difference(chocolatebox1))  
print(sweet_difference(chocolatebox2))  

Example Output:
[0, 11, 8]
[0, 1, 2]
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

def sweet_difference(chocolates):
    '''
    Plan:
    1. Initialize an empty list `result` to store the sweetness differences for each row.
    2. Use a queue to perform a level-order traversal (BFS) of the binary tree.
    3. For each level, track the minimum and maximum sweetness values.
    4. Calculate the absolute difference between the maximum and minimum values for that level and append it to `result`.
    5. Return the `result` list after traversing all levels of the tree.
    '''
    result = []
    if not chocolates:
        return result
    
    queue = deque([chocolates])
    while queue:
        level_size = len(queue)
        min_sweetness = float('inf')
        max_sweetness = float('-inf')

        for _ in range(level_size):
            node = queue.popleft()
            min_sweetness = min(min_sweetness, node.val)
            max_sweetness = max(max_sweetness, node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        sweetness_diff = abs(max_sweetness - min_sweetness)
        result.append(sweetness_diff)

    return result

sweetness_levels1 = [3, 9, 20, None, None, 15, 7]
chocolate_box1 = build_tree(sweetness_levels1)

sweetness_levels2 = [1, 2, 3, 4, 5, None, 6]
chocolate_box2 = build_tree(sweetness_levels2)

print(sweet_difference(chocolate_box1))  
print(sweet_difference(chocolate_box2))

'''
Time Complexity Analysis:
The time complexity of the `sweet_difference` function is O(N), where N is the number of nodes in the binary tree. 
This is because we perform a level-order traversal (BFS) of the tree, visiting each node exactly once.

Space Complexity Analysis:
The space complexity is O(M), where M is the maximum number of nodes at any level in the binary tree (the width of the tree).
This space is used by the queue to store nodes at the current level during the traversal.
'''