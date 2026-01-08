'''
Problem 6: Find Next Order to Fulfill Today
You store each customer order at your bakery in a binary tree where each node represents a different order. Each level of the tree 
represents a different day's orders. Given the root of a binary tree order_tree and an TreeNode object order representing the order 
you are currently fulfilling, return the next order to fulfill that day. The next order to fulfill is the nearest node on the same level. 
Return None if order is the last order of the day (rightmost node of the level).

Note: Because we must pass in a reference to a node in the tree, you cannot use the build_tree() function for testing. You must manually 
create the tree.

class TreeNode():
     def __init__(self, order, left=None, right=None):
        self.val = order
        self.left = left
        self.right = right

def find_next_order(order_tree, order):
    pass
    
Example Usage:
"""
        Cupcakes
       /       \ 
   Macaron     Cookies      
        \      /      \
      Cake   Eclair   Croissant
"""
cupcakes = TreeNode("Cupcakes")
macaron = TreeNode("Macaron")
cookies = TreeNode("Cookies")
cake = TreeNode("Cake")
eclair = TreeNode("Eclair")
croissant = TreeNode("Croissant")

cupcakes.left, cupcakes.right = macaron, cookies
macaron.right = cake
cookies.left, cookies.right = eclair, croissant

next_order1 = find_next_order(cupcakes, cake)
next_order2 = find_next_order(cupcakes, cookies)
print(next_order1.val)
print(next_order2.val)

Example Output:
Eclair
None
'''

from collections import deque
class TreeNode():
     def __init__(self, order, left=None, right=None):
        self.val = order
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

def find_next_order(order_tree, order):
    '''
    Plan:
    1. Use a queue to perform a level-order traversal (BFS) of the binary tree.
    2. For each level, keep track of the nodes in that level.
    3. When we find the target order, check if there is a next node in the same level.
    4. If there is a next node, return it; otherwise, return None.
    '''
    if not order_tree:
        return None
    
    queue = deque([order_tree])

    while queue:
        level_size = len(queue)
        
        for i in range(level_size):
            current_node = queue.popleft()
            # Once we've found the current order, check for the next one
            if current_node == order:
                # If it's not the last node in this level, return the next node; otherwise, return None
                if i == level_size - 1:
                    return None
                else:
                    return queue.popleft()
                
            # Add child nodes to the queue for the next level
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

    return None # If the order is not found in the tree

cupcakes = TreeNode("Cupcakes")
macaron = TreeNode("Macaron")
cookies = TreeNode("Cookies")
cake = TreeNode("Cake")
eclair = TreeNode("Eclair")
croissant = TreeNode("Croissant")

cupcakes.left, cupcakes.right = macaron, cookies
macaron.right = cake
cookies.left, cookies.right = eclair, croissant

next_order1 = find_next_order(cupcakes, cake)
next_order2 = find_next_order(cupcakes, cookies)
print(next_order1.val)
print(next_order2)

'''
Time Complexity: O(n) - In the worst case, we may need to traverse all nodes in the tree to find the target order.
Space Complexity: O(m) - where m is the maximum number of nodes at any level in the tree (the width of the tree).
'''
                
    
