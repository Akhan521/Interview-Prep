'''
Problem 2: Icing Cupcakes in Zigzag Order
You have rows of cupcakes represented as a binary tree cupcakes where each node in the tree represents a cupcake. To ice them efficiently, 
you are icing cupcakes one row (level) at a time, in zig zag order (i.e., from left to right, then right to left for the next row and alternate between).

Return a list of the cupcake values in the order you iced them.

Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the 
stated time and space complexity. Assume the input tree is balanced when calculating time complexity.

class TreeNode():
     def __init__(self, flavor, left=None, right=None):
        self.val = flavor
        self.left = left
        self.right = right

def zigzag_icing_order(cupcakes):
    pass
    
Example Usage:
"""
            Chocolate
           /         \
        Vanilla       Lemon
       /              /    \
    Strawberry   Hazelnut   Red Velvet   
"""

flavors = ["Chocolate", "Vanilla", "Lemon", "Strawberry", None, "Hazelnut", "Red Velvet"]
cupcakes = build_tree(flavors)
print(zigzag_icing_order(cupcakes))

Example Output:
['Chocolate', 'Lemon', 'Vanilla', 'Strawberry', 'Hazelnut', 'Red Velvet']
'''

from collections import deque
class TreeNode():
     def __init__(self, flavor, left=None, right=None):
        self.val = flavor
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

def zigzag_icing_order(cupcakes):
    '''
    Plan:
    1. Use a deque to facilitate level order traversal.
    2. Maintain a boolean flag to indicate the direction of traversal for each level.
    3. For each level, collect the cupcake values in a temporary list.
    4. If the current level is to be traversed from right to left, reverse the temporary list before adding it to the result.
    5. Toggle the direction flag for the next level.
    '''
    if not cupcakes:
        return []
    
    result = []
    q = deque([cupcakes])
    left_to_right = True

    while q:
        level_size = len(q)
        current_level = []
        
        for _ in range(level_size):
            node = q.popleft()
            current_level.append(node.val)
            
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        if not left_to_right:
            current_level.reverse()
        
        result.extend(current_level)
        left_to_right = not left_to_right

    return result

flavors = ["Chocolate", "Vanilla", "Lemon", "Strawberry", None, "Hazelnut", "Red Velvet"]
cupcakes = build_tree(flavors)
print(zigzag_icing_order(cupcakes))