'''
Problem 2: Sum of Cookies Sold Each Day
Your bakery stores each customer order in a binary tree, where each node represents a different customer's order and each node value 
represents the number of cookies ordered. Each level of the tree represents the orders for a given day.

Given the root of a binary tree orders, return a list of the sums of all cookies ordered in each day (level) of the tree.

Evaluate the time complexity of your solution. Define your variables and give a rationale as to why you believe your solution has the 
stated time complexity.

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def sum_each_days_orders(orders):
	pass
    
Example Usage:
"""
      4
     / \
    2   6
   / \  
  1   3
"""

# Using build_tree() function included at top of page
order_sizes = [4, 2, 6, 1, 3]
orders = build_tree(order_sizes)

print(sum_each_days_orders(orders))

Example Output:
[4, 8, 4]
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

def sum_each_days_orders(orders):
    '''
    General Approach:
    We'll perform a BFS traversal of the binary tree to visit each level (day) of orders.
    For each level, we'll sum the values of the nodes (orders) and store the sum in a result list.
    Finally, we'll return the list of sums for each day.

    Plan:
    1. Initialize an empty list `result` to store the sum of orders for each day.
    2. If the `orders` tree is empty (None), return the empty `result` list.
    3. Use a queue to perform a level-order traversal (BFS) of the tree.
    4. As we traverse each level, calculate the sum of the node values and append it to `result`.
    '''
    result = []

    if not orders:
        return result
    
    queue = deque([orders])
    while queue:
        # Number of nodes at the current level
        level_size = len(queue)
        level_sum = 0

        for _ in range(level_size):
            node = queue.popleft()
            level_sum += node.val

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level_sum)

    return result

order_sizes = [4, 2, 6, 1, 3]
orders = build_tree(order_sizes)

print(sum_each_days_orders(orders))

'''
Time Complexity:
The time complexity of this solution is O(N), where N is the number of nodes in the binary tree.
This is because we visit each node exactly once during the BFS traversal to calculate the sum of orders for each day.

Space Complexity:
The space complexity is O(M), where M is the maximum number of nodes at any level in the tree (the width of the tree).
This space is used by the queue to store nodes at the current level during the BFS traversal.
'''

