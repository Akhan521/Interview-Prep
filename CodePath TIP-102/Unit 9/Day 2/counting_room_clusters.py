'''
Problem 2: Counting Room Clusters
Given the root of a binary tree hotel where each node represents a room in the hotel and each node value represents the theme of the room, return the 
number of distinct clusters in the hotel. A distinct cluster is defined as a group of connected rooms (connected by edges) where each room has the same 
theme (val).

Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated 
time and space complexity. Evaluate the complexities for both a balanced and unbalanced tree.

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def count_clusters(hotel):
    pass
    
Example Usage:
"""
     👻
   /    \
  👻     🧛🏾
 /  \      \
👻  🧛🏾      🧛🏾
"""
# Using build_tree() function included at the top of the page
themes = ["👻", "👻", "🧛🏾", "👻", "🧛🏾", None, "🧛🏾"]
hotel = build_tree(themes)

print(count_clusters(hotel))

Example Output:
3
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

def count_clusters(hotel):
    '''
    Note: DFS is useful for finding all connected components in a graph.

    General Approach:
    We'll use DFS to traverse the binary tree and count distinct clusters of rooms with the same theme. A new cluster is found when we encounter a room
    with a different theme from its parent. We'll recursively explore each room's left and right children to accumulate the cluster count.

    Plan:
    1. Define a helper function `dfs` that takes a node and the theme of its parent room.
        - If the node is None, return 0 (no cluster).
        - Check if the current node is part of a new cluster (i.e., its theme is different from the parent's theme).
        - If it's a new cluster, increment the cluster count by 1.
        - Recursively check the left and right subtrees, passing the current node's theme as the parent's theme.
    2. In the main function, call the `dfs` function starting from the root of the tree with no parent theme.
    3. Return the total cluster count.
    '''
    def dfs(node, parent_theme):
        if not node:
            return 0 # No cluster
        
        # Check if current node is part of a new cluster (increment count if theme differs from parent)
        current_theme = node.val
        is_new_cluster = True if current_theme != parent_theme else False
        cluster_count = 1 if is_new_cluster else 0 

        # Recursively check left and right subtrees (passing current node's theme as parent theme)
        cluster_count += dfs(node.left, current_theme)
        cluster_count += dfs(node.right, current_theme) 

        return cluster_count
    
    return dfs(hotel, None)

themes = ["👻", "👻", "🧛🏾", "👻", "🧛🏾", None, "🧛🏾"]
hotel = build_tree(themes)

print(count_clusters(hotel))