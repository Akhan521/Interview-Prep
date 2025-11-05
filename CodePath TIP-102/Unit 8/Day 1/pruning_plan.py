'''
Problem 3: Pruning Plans
You have a large overgrown Magnolia tree that's in desperate need of some pruning. Before you can prune the tree, you need to do a full survey 
of the tree to evaluate which sections need to be pruned.

Given the root of a binary tree representing the magnolia, return a list of the values of each node using a postorder traversal. In a postorder 
traversal, you explore the left subtree first, then the right subtree, and finally the root. Postorder traversals are often used when deleting nodes from a tree.

Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the 
stated time and space complexity. Assume the input tree is balanced when calculating time and space complexity.

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def survey_tree(root):
    pass
    
Example Usage:
"""
        Root
      /      \
    Node1    Node2
  /         /    \
Leaf1    Leaf2  Leaf3
"""

magnolia = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1"))
                        TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

print(survey_tree(magnolia))

Example Output:
['Leaf1', 'Node1', 'Leaf2', 'Leaf3', 'Node2', 'Root']
'''

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def survey_tree(root):
    result = []

    def postorder(node):
        if not node:
            return
        postorder(node.left)
        postorder(node.right)
        result.append(node.val)

    postorder(root)
    return result

"""
        Root
      /      \
    Node1    Node2
  /         /    \
Leaf1    Leaf2  Leaf3
"""

magnolia = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                        TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

print(survey_tree(magnolia))