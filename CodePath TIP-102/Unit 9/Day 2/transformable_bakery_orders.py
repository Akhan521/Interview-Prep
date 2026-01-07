'''
Problem 4: Transformable Bakery Orders
In your bakery, customer orders are each represented by a binary tree. The value of each node in the tree represents a type of cupcake, 
and the tree structure represents how the order is organized in the delivery box. Sometimes, orders don't get picked up.

Given two orders, you want to see if you can rearrange the first order that didn't get picked up into the second order so as not to waste
any cupcakes. You can swap the left and right subtrees of any cupcake (node) in the order.

Given the roots of two binary trees order1 and order2, write a function can_rearrange_orders() that returns True if the tree represented
by order1 can be rearranged to match the tree represented by order2 by doing any number of swaps of order1’s left and right branches.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the 
stated time complexity.

class TreeNode():
     def __init__(self, flavor, left=None, right=None):
        self.val = flavor
        self.left = left
        self.right = right

def can_rearrange_orders(order1, order2):
    pass

Example Usage:
"""
              Red Velvet                             Red Velvet
             /          \                           /           \
        Vanilla         Lemon                   Lemon            Vanilla
        /      \        /   \                  /     \           /      \
      Ube    Almond  Chai   Carrot       Carrot      Chai    Almond    Ube 
                     /   \        \       /          /   \      
                 Chai   Maple   Smore   Smore    Maple   Chai
"""

# Using build_tree() function included at top of page
flavors1 = ["Red Velvet", "Vanilla", "Lemon", "Ube", "Almond", "Chai", "Carrot", 
            None, None, None, None, "Chai", "Maple", None, "Smore"]
flavors2 = ["Red Velvet", "Lemon", "Vanilla", "Carrot", "Chai", "Almond", "Ube", "Smore", None, "Maple", "Chai"]
order1 = build_tree(flavors1)
order2 = build_tree(flavors2)

can_rearrange_orders(order1, order2)

Example Output:
True
Explanation:
              Red Velvet                             Red Velvet
             /          \                           /           \
        Vanilla         Lemon         ->        Lemon            Vanilla
        /      \        /   \                  /     \           /      \      ->
      Ube    Almond  Chai   Carrot           Chai   Carrot      Ube    Almond
                     /   \        \         /    \       \        
                 Chai   Maple   Smore     Chai   Maple   Smore


              Red Velvet                             Red Velvet
             /          \                           /           \
         Lemon          Vanilla       ->        Lemon            Vanilla
        /     \          /     \               /     \           /      \
   Carrot      Chai    Almond   Ube          Carrot   Chai    Almond    Ube 
       \       /   \                         /        /   \      
      Smore  Chai   Maple                  Smore   Maple   Chai
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

def can_rearrange_orders(order1, order2):
    '''
    General Approach:
    To determine if order1 can be rearranged to match order2, we can use a recursive approach.
    We'll recursively check whether two subtrees are equivalent, either directly or when one tree is a mirror of the other.

    Plan:
    1. If both nodes are None, return True (both subtrees are empty).
    2. If one node is None and the other is not, return False (one subtree is empty, the other is not).
    3. If the values of the two nodes are different, return False (the cupcake types don't match).
    4. Recursively check two scenarios:
       a. The left subtree of order1 matches the left subtree of order2 and the right subtree of order1 matches the right subtree of order2.
       b. The left subtree of order1 matches the right subtree of order2 and the right subtree of order1 matches the left subtree of order2.
    5. If either scenario is True, return True; otherwise, return False.
    '''
    if not order1 and not order2:
        return True
    
    if not order1 or not order2:
        return False
    
    if order1.val != order2.val:
        return False
    
    # Check whether the subtrees match directly or in swapped order
    return (
        (can_rearrange_orders(order1.left, order2.left) and 
        can_rearrange_orders(order1.right, order2.right)) or 
        (can_rearrange_orders(order1.left, order2.right) and
        can_rearrange_orders(order1.right, order2.left))
    )

flavors1 = ["Red Velvet", "Vanilla", "Lemon", "Ube", "Almond", "Chai", "Carrot", 
            None, None, None, None, "Chai", "Maple", None, "Smore"]
flavors2 = ["Red Velvet", "Lemon", "Vanilla", "Carrot", "Chai", "Almond", "Ube", "Smore", None, "Maple", "Chai"]
order1 = build_tree(flavors1)
order2 = build_tree(flavors2)

print(can_rearrange_orders(order1, order2))  # True

'''
Time Complexity:
The time complexity of this function is O(N * M), where N is the number of nodes in order1 and M is the number of nodes in order2.
This is because, in the worst case, we may need to compare each node in order1 with each node in order2 during the recursive checks.

Space Complexity:
The space complexity is O(H1 + H2), where H1 and H2 are the heights of order1 and order2, respectively.
This space is used by the recursion stack during the depth-first traversal of both trees.
'''