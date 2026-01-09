'''
Problem 5: Can Fulfill Order
At your bakery, you organize your current stock of baked goods in a binary tree with root inventory where each node represents the 
quantity of a baked good in your bakery. A customer comes in wanting a random assortment of baked goods of quantity order_size. Given 
the root inventory and integer order_size, return True if you can fulfill the order and False otherwise. You can fulfill the order if 
the tree has a root-to-leaf path such that adding up all the values along the path equals order_size.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the 
stated time complexity. Assume the input tree is balanced when calculating time complexity.

class TreeNode():
     def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def can_fulfill_order(inventory, order_size):
    pass
    
Example Usage:
"""
             5
           /   \
          4     8
        /      /  \
       11     13   4
      /  \          \
     7   2           1   
"""

# Using build_tree() function included at top of the page
quantities = [5,4,8,11,None,13,4,7,2,None,None,None,1]
baked_goods = build_tree(quantities)

print(can_fulfill_order(baked_goods, 22))
print(can_fulfill_order(baked_goods, 2))

Example Output:
True
Example 1 Explanation: 5 + 4 + 11 + 2 = 22

False
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

def can_fulfill_order(inventory, order_size):
    '''
    General Idea:
    We will perform a depth-first search (DFS) on the binary tree to explore all root-to-leaf paths.
    At each node, we will subtract the node's value from the remaining order size.
    Recursively check if we can fulfill the order in either the left or right subtree.

    Plan:
    1. If the inventory is None, return False.
    2. If the current node is a leaf (no left or right children), check if the remaining order size equals the node's value.
    3. Subtract the current node's value from order_size to get the new remaining size.
    4. Recursively call can_fulfill_order on the left and right children with the updated order size.
    5. Return True if either subtree can fulfill the order, otherwise return False.
    '''
    if not inventory: 
        return False
    
    # Check if it's a leaf node
    if not inventory.left and not inventory.right:
        # Check if the remaining order size matches the leaf node's value
        return order_size == inventory.val 
    
    # Update the remaining order size
    remaining_size = order_size - inventory.val
    # Recursively check left and right subtrees
    return (can_fulfill_order(inventory.left, remaining_size) or
            can_fulfill_order(inventory.right, remaining_size))

quantities = [5,4,8,11,None,13,4,7,2,None,None,None,1]
baked_goods = build_tree(quantities)

print(can_fulfill_order(baked_goods, 22))
print(can_fulfill_order(baked_goods, 2))