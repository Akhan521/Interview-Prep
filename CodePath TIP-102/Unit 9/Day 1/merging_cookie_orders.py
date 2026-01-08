'''
Problem 1: Merging Cookie Orders
You run a local bakery and are given the roots of two binary trees order1 and order2 where each node in the binary tree represents 
the number of a certain cookie type the customer has ordered. To maximize efficiency, you want to bake enough of each type of cookie 
for both orders together.

Given order1 and order2, merge the order together into one tree and return the root of the merged tree. To merge the orders, imagine 
that when place one tree on top of the other, some nodes of the two trees are overlapped while others are not. If two nodes overlap, 
then sum node values up as the new value of the merged node. Otherwise, the not None node will be used as the node of the new tree.

Start the merging process from the root of both orders.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the 
stated time complexity. Assume the input tree is balanced when calculating time complexity.

class TreeNode():
     def __init__(self, quantity, left=None, right=None):
        self.val = quantity
        self.left = left
        self.right = right

def merge_orders(order1, order2):
    pass
    
Example Usage:
"""
     1             2         
    /  \         /   \       
   3    2       1     3   
 /               \      \   
5                 4      7   
"""
# Using build_tree() function included at top of page
cookies1 = [1, 3, 2, 5]
cookies2 = [2, 1, 3, None, 4, None, 7]
order1 = build_tree(cookies1)
order2 = build_tree(cookies2)

# Using print_tree() function included at top of page
print_tree(merge_orders(order1, order2))

Example Usage:
[3, 4, 5, 5, 4, None, 7]
Explanation:
Merged Tree:
     3
    /  \      
  4     5  
 / \      \
5   4      7
'''

from collections import deque
class TreeNode():
     def __init__(self, quantity, left=None, right=None):
        self.val = quantity
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

def merge_orders(order1, order2):
    '''
    General Approach:
    We'll perform a pre-order traversal of both trees simultaneously. At each node, we'll sum the values if both nodes exist,
    or take the non-null node if only one exists. We'll return the merged tree's root.

    Plan:
    1. If either order1 or order2 is None, return the other order.
    2. Create a new TreeNode with the sum of order1.val and order2.val.
    3. Recursively merge the left children of both orders and assign to the new node's left.
    4. Recursively merge the right children of both orders and assign to the new node's right.
    5. Return the new merged node.
    '''
    if not order1:
        return order2
    if not order2:
        return order1
    
    # Create a new node with the sum of both nodes' values
    merged_node = TreeNode(order1.val + order2.val)
    # Recursively merge the left and right children
    merged_node.left = merge_orders(order1.left, order2.left)
    merged_node.right = merge_orders(order1.right, order2.right)

    return merged_node

cookies1 = [1, 3, 2, 5]
cookies2 = [2, 1, 3, None, 4, None, 7]
order1 = build_tree(cookies1)
order2 = build_tree(cookies2)

# Using print_tree() function included at top of page
print_tree(merge_orders(order1, order2))

'''
Time Complexity Analysis:
Let N be the number of nodes in the larger of the two trees. The time complexity of this algorithm is O(N) because we visit each 
node exactly once during the merge process.

Space Complexity Analysis:
The space complexity is O(N) in the worst case due to the recursion stack and the space needed to store the merged tree.
If the trees are balanced, the height of the tree would be log(N), leading to O(log N) space complexity for the recursion stack.
However, if the trees are skewed, the height could be N, leading to O(N) space complexity.
'''