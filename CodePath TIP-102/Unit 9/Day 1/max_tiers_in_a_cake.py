'''
Problem 3: Maximum Tiers in Cake
You have entered your bakery into a cake baking competition and for your entry have decided build a complicated pyramid shape cake, 
where different sections have different numbers of tiers. Given the root of a binary tree cake where each node represents a different 
section of your cake, return the maximum number of tiers in your cake.

The maximum number of tiers is the number of nodes along the longest path from the root node down to the farthest leaf node.

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
    General Approach:
    Use a recursive depth-first search (DFS) approach to traverse the binary tree and calculate the maximum tiers.
    This problem is essentially finding the height of the binary tree.

    Plan:
    1. If the cake (node) is None, return 0 (base case).
    2. Recursively calculate the maximum tiers in the left and right subtrees.
    3. The max tiers for the current node is 1 (for the current node) plus the maximum of the tiers from the left and right subtrees.
    4. Return the calculated max tiers.
    '''
    if not cake:
        return 0
    
    left_tiers = max_tiers(cake.left)
    right_tiers = max_tiers(cake.right)

    return 1 + max(left_tiers, right_tiers)

cake_sections = ["Chocolate", "Vanilla", "Strawberry", None, None, "Chocolate", "Coffee"]
cake = build_tree(cake_sections)

print(max_tiers(cake))

'''
Time Complexity Analysis:
The time complexity of this solution is O(n), where n is the number of nodes in the binary tree.
We visit each node exactly once during our depth-first traversal of the tree.

Space Complexity Analysis:
The space complexity is O(h), where h is the height of the tree.
This space is used by the call stack during the recursive function calls.
'''

