'''
Problem 7: Remove Plant
A plant in your houseplant collection has become infested with aphids, and unfortunately you need to throw it out. Given the root of a BST collection 
where each node represents a plant in your collection, and a plant name, remove the plant node with value name from the collection. Return the root of 
the modified collection. Plants are organized alphabetically in the tree by value.

If the node with name has two children in the tree, replace it with its inorder predecessor (rightmost node in its left subtree). You do not need to 
maintain a balanced tree.

Pseudocode has been provided for you.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time 
complexity. Assume the input tree is balanced when calculating time complexity.

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def remove_plant(collection, name):
    # Find the node to remove
    # If the node has no children
        # Remove the node by setting parent pointer to None
    # If the node has one child
        # Replace the node with its child
    # If the node has two children
        # Find the inorder predecessor 
        # Replace the node's value with inorder predecessor value
        # Remove inorder predecessor
    # Return root of updated tree
    pass
    
Example Usage:
"""
              Money Tree
             /         \
           Hoya        Pilea
              \        /   \
             Ivy    Orchid  ZZ Plant
"""

# Using build_tree() function at the top of page
values = ["Money Tree", "Hoya", "Pilea", None, "Ivy", "Orchid", "ZZ Plant"]
collection = build_tree(values)

# Using print_tree() function at the top of page
print_tree(remove_plant(collection, "Pilea"))

Example Output:
['Money Tree', 'Hoya', 'Orchid', None, 'Ivy', None, 'ZZ Plant']

Explanation:
The resulting tree structure:
             Money Tree
            /         \
          Hoya       Orchid
              \          \
              Ivy      ZZ Plant
'''

from collections import deque
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

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

def find_rightmost_node(node):
    '''Find the rightmost node in a subtree (max value node in a BST)'''
    current = node
    while current.right:
        current = current.right
    return current

def remove_plant(collection, name):
    '''
    General Approach:
    We'll traverse the BST to find the node to remove and handle the different cases based on the number of children the node has.

    1. If the node is None, return None.
    2. If the node's value is less than the name, we need to search in the right subtree.
    3. If the node's value is greater than the name, we need to search in the left subtree.
    4. If the node's value matches the name, we need to handle three cases:
        - If the node has no children, we can simply remove it by returning None.
        - If the node has one child, we can replace the node with its child.
        - If the node has two children:
            1. Find the inorder predecessor (the rightmost node in the left subtree).
            2. Replace the node's value with the inorder predecessor's value.
            3. Remove the inorder predecessor node from the left subtree.
    5. Return the root of the modified tree.
    '''
    if not collection:
        return None

    # 1. Find the node to remove
    if collection.val < name:
        collection.right = remove_plant(collection.right, name)
    elif collection.val > name:
        collection.left = remove_plant(collection.left, name)
    else:
        # 2. If the node has no children
        if not collection.left and not collection.right:
            return None
        
        # 3. If the node has one child
        if not collection.left:
            return collection.right
        elif not collection.right:
            return collection.left
        
        # 4. If the node has two children: find the inorder predecessor, replace the node's value, and remove the inorder predecessor
        inorder_predecessor = find_rightmost_node(collection.left)
        collection.val = inorder_predecessor.val
        collection.left = remove_plant(collection.left, inorder_predecessor.val) # Recursively remove the inorder predecessor node

    return collection

values = ["Money Tree", "Hoya", "Pilea", None, "Ivy", "Orchid", "ZZ Plant"]
collection = build_tree(values)

# Using print_tree() function at the top of page
print_tree(remove_plant(collection, "Pilea"))
