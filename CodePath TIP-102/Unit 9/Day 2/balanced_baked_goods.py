'''
Problem 1: Balanced Baked Goods Display
Given the root of a binary tree display representing the baked goods on display at your store, return True if the tree is balanced 
and False otherwise.

A balanced display is a binary tree in which the difference in the height of the two subtrees of every node never exceeds one.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has 
the stated time complexity.

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def is_balanced(display):
	pass
    
Example Usage:
"""
      🎂
     /  \
   🥮   🍩
       /  \  
     🥖    🧁

"""
# Using build_tree() function included at top of page
baked_goods = ["🎂", "🥮", "🍩", None, None, "🥖", "🧁"] 
display1 = build_tree(baked_goods)

"""
          🥖
         /  \
       🧁    🧁
       /       \  
      🍪       🍪
     /           \
    🥐           🥐  

"""
baked_goods = ["🥖", "🧁", "🧁", "🍪", None, None, "🍪", "🥐", None, None, "🥐"]
display2 = build_tree(baked_goods)


print(is_balanced(display1)) 
print(is_balanced(display2))  

Example Output:
True
False
'''

from collections import deque 

class TreeNode:
  def __init__(self, value, key=None, left=None, right=None):
      self.key = key
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

def is_balanced(display):
    '''
    General Approach:
    Perform a depth-first search (DFS) traversal of the binary tree to calculate the height of each subtree.
    During the traversal, check if the height difference between the left and right subtrees of each node exceeds one.
    If any node is found to be unbalanced, return False. If the entire tree is traversed without finding unbalanced nodes, return True.

    Plan:
    1. Define a helper function that checks for balance and calculates height.
        - If the node is None, return True (balanced) and height 0.
        - Recursively check the left and right subtrees for balance and height.
        - The current node is balanced if both subtrees are balanced and the height difference is at most 1.
        - The height of the current node is 1 + the maximum height of its subtrees.
    2. Call the helper function on the root of the tree and return whether it is balanced.
    '''
    def check_balance(node):
        if not node:
            return True, 0
        
        is_left_balanced, left_height = check_balance(node.left)
        is_right_balanced, right_height = check_balance(node.right)

        # The current node is balanced if both subtrees are balanced and the height difference is at most 1.
        is_balanced = (is_left_balanced and is_right_balanced and abs(left_height - right_height) <= 1)

        # Height of the current node is 1 + max height of its subtrees.
        height = 1 + max(left_height, right_height)

        # Return whether the current node is balanced and its height.
        return is_balanced, height
    
    balanced, _ = check_balance(display)
    return balanced

"""
      🎂
     /  \
   🥮   🍩
       /  \  
     🥖    🧁

"""
# Using build_tree() function included at top of page
baked_goods = ["🎂", "🥮", "🍩", None, None, "🥖", "🧁"] 
display1 = build_tree(baked_goods)

"""
          🥖
         /  \
       🧁    🧁
       /       \  
      🍪       🍪
     /           \
    🥐           🥐  

"""
baked_goods = ["🥖", "🧁", "🧁", "🍪", None, None, "🍪", "🥐", None, None, "🥐"]
display2 = build_tree(baked_goods)


print(is_balanced(display1)) 
print(is_balanced(display2))  

'''
Time Complexity Analysis:
The time complexity of the `is_balanced` function is O(n), where n is the number of nodes in the binary tree. 
    - Each node is visited exactly once during the depth-first traversal.

Space Complexity Analysis:
The space complexity is O(h), where h is the height of the tree. 
    - The recursion stack can go as deep as the height of the tree in the worst case (for a skewed tree).
    - In a balanced tree, the height h is log(n), leading to O(log n) space complexity.
    - In the worst case (skewed tree), the height can be n, leading to O(n) space complexity.
'''