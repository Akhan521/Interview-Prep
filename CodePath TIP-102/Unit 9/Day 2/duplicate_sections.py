'''
Problem 3: Duplicate Sections of the Hotel
On one of your shifts at the haunted hotel, you find that you keep stumbling upon the same rooms in different halls. It's almost as if some parts of 
the hotel are being duplicated...

Given the root of a binary tree hotel where each node represents a room in the hotel, return a list of the roots of all duplicate subtrees. For each 
duplicate subtree, you only need to return the root node of any one of them. Two trees are duplicate if they have the same structure and the same node values.

Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated 
time and space complexity. Evaluate the complexities for both a balanced and unbalanced tree.

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def find_duplicate_subtrees(hotel):
    pass
    
Example Usage:
"""
        Lobby
      /       \
    101      123
    /        /  \ 
  201      101  201
          /
         201
"""
# Using build_tree() function included at top of page
rooms = ["Lobby", 101, 123, 201, None, 101, 201, None, None, 201]
hotel = build_tree(rooms)

# Using print_tree() function included at top of page
subtree_lst = find_duplicate_subtrees(hotel)
for subtree in subtree_lst:
    print_tree(subtree)

Example Output:
[101, 201]
[201]

Explanation: 
Subtrees:
   Subtree 1   Subtree 2
     101         201
     /
   201
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

def find_duplicate_subtrees(hotel):
    '''
    General Approach:
    We'll use a hash map to keep track of all subtrees we've seen so far (serialized subtrees as keys). This helps us identify duplicates efficiently.
    We'll use a post-order traversal to serialize each subtree. If we encounter a serialized subtree that we've seen before, we add it to our result list.

    Plan:
    1. Define a helper function to serialize subtrees using post-order traversal.
        - Our method will be called `get_id(node)`, which returns a unique identifier for each subtree.
        - We'll serialize the subtree as a tuple: (node value, left subtree id, right subtree id).
        - If the serialized subtree is already in our hash map, we add the root node to our result list.
    2. Use a hash map to count occurrences of each serialized subtree.
        - Our hash map will have the form: {serialized_subtree: (subtree_id, count)}.
    3. If a serialized subtree appears more than once, add the root node of that subtree to the result list.
    4. Return the list of duplicate subtree roots.
    '''
    def get_id(node):
        if not node:
            return 0 # Using 0 to represent null nodes
        
        serialized_subtree = (node.val, get_id(node.left), get_id(node.right))

        # Check if we've seen this subtree before
        if serialized_subtree not in subtree_map:
            subtree_id = len(subtree_map) + 1
            subtree_map[serialized_subtree] = (subtree_id, 1)
        else:
            subtree_id, count = subtree_map[serialized_subtree]
            subtree_map[serialized_subtree] = (subtree_id, count + 1)

        # If this is the second time we've seen this subtree, add the duplicate root to the result
        if subtree_map[serialized_subtree][1] == 2:
            result.append(node)

        # Return the unique id for this subtree
        return subtree_map[serialized_subtree][0]
    
    subtree_map = {}
    result = []
    get_id(hotel)
    return result
            
rooms = ["Lobby", 101, 123, 201, None, 101, 201, None, None, 201]
hotel = build_tree(rooms)

# Using print_tree() function included at top of page
subtree_lst = find_duplicate_subtrees(hotel)
for subtree in subtree_lst:
    print_tree(subtree)

'''
Time Complexity:
The time complexity is O(N), where N is the number of nodes in the binary tree. This is because we perform a post-order traversal of the tree, 
visiting each node exactly once to serialize its subtree.

Space Complexity:
The space complexity is O(N) in the worst case because the hash map stores serialized representations of all unique subtrees. In the worst case, all 
subtrees could be unique.
'''