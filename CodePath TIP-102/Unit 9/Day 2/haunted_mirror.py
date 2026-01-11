'''
Problem 1: Haunted Mirror
A vampire has come to stay at the haunted hotel, but he can't see his reflection! What's more, he doesn't seem to be able to see the 
reflection of anything in the mirror! He's asked you to come to his aid and help him see the reflections of different thngs.

Given the root of a binary tree vampire, return the mirror image of the tree. The mirror image of a tree is obtained by flipping the 
tree along its vertical axis, meaning that the left and right children of all non-leaf nodes are swapped.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the 
stated time complexity.

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def mirror_tree(vampire):
    pass
"""
      🧛‍♂️
     /   \
    💪🏼    🤳
    /      \
   👟       👞
"""
# Using build_tree() function included at the top of the page
body_parts = ["🧛‍♂️", "💪🏼", "🤳", "👟", None, None, "👞"]
vampire = build_tree(body_parts)

"""
      🎃
     /   \
    😈    🕸️
         /  \
       🧟‍♂️    👻
"""
spooky_objects = ["🎃", "😈", "🕸️", None, None, "🧟‍♂️", "👻"]
spooky_tree = build_tree(spooky_objects)

# Using print_tree() function included at the top of the page
print_tree(mirror_tree(vampire))
print_tree(mirror_tree(spooky_tree)) 

Example Output:
['🧛‍♂️', '🤳', '💪🏼', '👞', None, None, '👟']
Example 1 Explanation:
Mirrored Tree:
      🧛‍♂️
    /    \
  🤳     💪🏼
 /         \
👞          👟

['🎃', '🕸️', '😈', '👻', '🧟‍♂️',]
Example 2 Explanation:
Mirrored Tree:
      🎃
    /    \
  🕸️     😈
 /  \
👻  🧟‍♂️
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

def mirror_tree(vampire):
    '''
    General Approach:
    To create the mirror image of a binary tree, we'll use a recursive approach. For each node in the tree, we'll swap its left and 
    right children. We'll continue this process recursively for each child node until we reach the leaf nodes.

    Plan:
    1. If the current node is None, return None.
    2. Swap the left and right children of the current node.
    3. Recursively call the mirror_tree function on the left and right children.
    4. Return the current node after its children have been swapped.
    '''
    if not vampire:
        return None
    
    # Swap the left and right children
    vampire.left, vampire.right = vampire.right, vampire.left

    # Recursively mirror the left and right subtrees
    mirror_tree(vampire.left)
    mirror_tree(vampire.right)
    
    return vampire

body_parts = ["🧛‍♂️", "💪🏼", "🤳", "👟", None, None, "👞"]
vampire = build_tree(body_parts)

"""
      🎃
     /   \
    😈    🕸️
         /  \
       🧟‍♂️    👻
"""
spooky_objects = ["🎃", "😈", "🕸️", None, None, "🧟‍♂️", "👻"]
spooky_tree = build_tree(spooky_objects)

# Using print_tree() function included at the top of the page
print_tree(mirror_tree(vampire))
print_tree(mirror_tree(spooky_tree)) 

'''
Time Complexity Analysis:
The time complexity of the mirror_tree function is O(n), where n is the number of nodes in the binary tree. 
This is because we visit each node exactly once to swap its children.

Space Complexity Analysis:
The space complexity is O(h), where h is the height of the tree.
This space is used by the call stack during the recursive function calls.
'''