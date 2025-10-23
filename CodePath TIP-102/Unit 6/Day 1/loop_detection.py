'''
Problem 2: Protein Folding Loop Detection
As a biochemist, you're studying the folding patterns of proteins, which are represented as a sequence of amino acids linked together. 
These proteins sometimes fold back on themselves, creating loops that can impact their function.

Given the head of a linked list protein where each node in the linked list represents an amino acid in the protein, return an array with the 
values of any cycle in the list. A linked list has a cycle if at some point in the list, the node’s next pointer points back to a previous node in the list.

The values may be returned in any order.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has 
the stated time and space complexity.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def cycle_length(protein):
    pass
    
Example Usage:
Linked list with 4 nodes and a cycle where 4th node points to 2nd node

protein_head = Node('Ala', Node('Gly', Node('Leu', Node('Val'))))
protein_head.next.next.next.next = protein_head.next 

print(cycle_length(protein_head))

Example Output:
['Gly', 'Leu', 'Val']
'''

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def cycle_length(protein):
    '''
    Plan:
    1. Initialize two pointers, slow and fast, both starting at the head of the linked list.
    2. Move slow pointer one step at a time and fast pointer two steps at a time.
    3. If there is a cycle, the two pointers will eventually meet. If fast pointer reaches the end, there is no cycle.
    4. Once a cycle is detected, reset one pointer to the head and keep the other at the meeting point.
    5. Move both pointers one step at a time until they meet again. This meeting point is the start of the cycle.
    6. Traverse the cycle starting from the meeting point and collect all node values in a list until we return to the starting point.
    '''
    if not protein:
        return []
    
    # Step 1: Detect cycle using Floyd's Tortoise and Hare algorithm
    slow = fast = protein
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return []  # No cycle detected.
    
    # Step 2: Find the start of the cycle
    slow = protein
    while slow != fast:
        slow = slow.next
        fast = fast.next

    # Step 3: Collect all values in the cycle
    cycle_nodes = []
    cycle_start = slow
    while True:
        cycle_nodes.append(slow.value)
        slow = slow.next
        if slow == cycle_start:
            break

    return cycle_nodes

protein_head = Node('Ala', Node('Gly', Node('Leu', Node('Val'))))
protein_head.next.next.next.next = protein_head.next 

print(cycle_length(protein_head))
